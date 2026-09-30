#!/usr/bin/env python3
"""Read-only, offline consistency checks for the three promotion drafts."""

import argparse
import html
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


FIELDS = ("Episode", "Speaker", "Affiliation", "Topic", "Moderator", "Date", "Time", "Zoom", "Website")
CHANNELS = ("LinkedIn", "INFORMS", "Email")
URL = re.compile(r"https?://[^\s<>\"`]+", re.I)
H2 = re.compile(r"^ {0,3}##\s+(.+?)\s*#*\s*$")
REFERENCE = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*(.*)$")


class InputError(Exception):
    pass


def read_lines(path):
    try:
        return list(enumerate(Path(path).read_text(encoding="utf-8-sig").splitlines(), 1))
    except (OSError, UnicodeError) as exc:
        raise InputError(f"Cannot read {path}: {exc}") from None


def section(lines, name):
    """Use exact H2 names; ignore headings inside fenced code blocks."""
    matches, current, fence = [], None, None
    for number, line in lines:
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = marker[1][0]
            elif marker[1][0] == fence:
                fence = None
            continue
        if fence:
            continue
        heading = H2.match(line)
        if heading:
            current = [] if heading[1].casefold() == name.casefold() else None
            if current is not None:
                matches.append(current)
        elif current is not None:
            current.append((number, line))
    if len(matches) != 1:
        raise InputError(f"Expected exactly one '## {name}' section; found {len(matches)}.")
    if not any(line.strip() for _, line in matches[0]):
        raise InputError(f"The '## {name}' section is empty.")
    return matches[0]


def normalize(value):
    value = html.unescape(value).casefold()
    value = re.sub(r"\b(?:professor|prof|dr)\.?\s+", "", value)
    return " ".join(re.findall(r"\w+", value))


def contains(text, expected):
    return f" {normalize(expected)} " in f" {normalize(text)} "


def clean_url(value):
    value = html.unescape(value)
    # Closing Markdown punctuation is not part of a destination; balanced
    # parentheses within a URL remain significant.
    while value.endswith(")") and value.count(")") > value.count("("):
        value = value[:-1]
    return value


def url_key(value):
    parsed = urlsplit(value)
    if not parsed.hostname or parsed.username or parsed.password:
        raise InputError("A URL is malformed or contains account credentials.")
    # Only scheme/hostname are case-insensitive. Paths, queries, fragments,
    # trailing slashes and query order must match the supplied verified URL.
    return (parsed.scheme.lower(), parsed.netloc.lower(), parsed.path, parsed.query, parsed.fragment)


def urls_in(text):
    return [clean_url(match[0]) for match in URL.finditer(text)]


def read_facts(lines):
    facts, allowed = {}, []
    for number, line in section(lines, "Expected facts"):
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip().replace(r"\|", "|") for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if len(cells) != 2:
            raise InputError(f"Expected a two-column fact table at line {number}.")
        field, value = cells
        if normalize(field) == "field" and normalize(value) == "value":
            continue
        if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        key = next((name for name in (*FIELDS, "Allowed links") if name.casefold() == field.casefold()), None)
        if key is None:
            raise InputError(f"Unknown expected-facts field '{field}' at line {number}.")
        if key in facts or not value:
            raise InputError(f"Duplicate or empty expected-facts field '{field}' at line {number}.")
        facts[key] = value
    missing = [field for field in FIELDS if field not in facts]
    if missing:
        raise InputError("Missing expected-facts fields: " + ", ".join(missing))
    if not re.fullmatch(r"\d+", facts["Episode"]):
        raise InputError("Episode must contain digits only.")
    for field in ("Zoom", "Website"):
        found = urls_in(facts[field])
        if len(found) != 1:
            raise InputError(f"{field} must contain exactly one full HTTP(S) URL.")
        facts[field] = found[0]
        url_key(found[0])
    if not is_zoom(facts["Zoom"]):
        raise InputError("Zoom must be a full URL on zoom.us or a subdomain of zoom.us.")
    if "Allowed links" in facts:
        allowed = urls_in(facts["Allowed links"])
        if not allowed and normalize(facts["Allowed links"]) not in ("none", "not applicable"):
            raise InputError("Allowed links must list verified HTTP(S) URLs or 'None'.")
        for value in allowed:
            url_key(value)
    return facts, allowed


def is_zoom(value):
    host = urlsplit(value).hostname or ""
    return host == "zoom.us" or host.endswith(".zoom.us")


def visible_text(text):
    text = re.sub(r"\[([^\]]+)\]\([^\n]*?\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\1", text)
    return text.replace("**", "").replace("__", "").replace("`", "")


def draft_content(lines):
    # Recipient values are outside this checker's scope and never quoted.
    return [(n, line) for n, line in lines if not re.match(r"^\s*(?:[-*>]\s*)?(?:\*\*)?(?:to|cc|bcc)\s*(?:\*\*)?\s*:", line, re.I)]


def get_links(lines):
    definitions, destinations, unresolved = {}, [], []
    for number, line in lines:
        match = REFERENCE.match(line)
        if match:
            values = urls_in(match[2])
            if values:
                definitions[normalize(match[1])] = values[0]
    for number, line in lines:
        if REFERENCE.match(line):
            continue
        # Exclude visible inline-link labels: only their targets are links.
        line = re.sub(r"!?\[[^\]\n]*\]\(\s*", "(", line)

        def reference(match):
            label, identifier = match[1], match[2] or match[1]
            key = normalize(identifier)
            if key in definitions:
                destinations.append((number, definitions[key]))
            else:
                unresolved.append(number)
            return ""

        line = re.sub(r"\[([^\]\n]+)\]\[([^\]\n]*)\]", reference, line)
        # Shortcut reference links, e.g. [event], also resolve if defined.
        def shortcut(match):
            key = normalize(match[1])
            if key in definitions:
                destinations.append((number, definitions[key]))
                return ""
            return match[0]

        line = re.sub(r"\[([^\]\n]+)\]", shortcut, line)
        destinations.extend((number, value) for value in urls_in(line))
    return destinations, unresolved


def brief(text):
    return text.strip().replace("|", r"\|")[:180]


def labeled_match(field, value, facts):
    actual, expected = normalize(value), normalize(facts[field])
    if actual == expected:
        return True
    if field == "Speaker":
        return actual == normalize(facts["Speaker"] + " " + facts["Affiliation"])
    # Date and time may share a labeled line, in either order.
    if field in ("Date", "Time"):
        return actual in (normalize(facts["Date"] + " " + facts["Time"]), normalize(facts["Time"] + " " + facts["Date"]))
    return False


def labeled_value(line, field):
    # Permit leading presentation punctuation, bullets and emoji, but not words.
    match = re.match(rf"^[^\w]*{field}\s*:\s*(.*)$", line, re.I)
    return match[1] if match else None


def check_draft(channel, path, raw_lines, facts, allowed):
    lines = draft_content(raw_lines)
    text_lines = [(n, visible_text(line)) for n, line in lines if not REFERENCE.match(line)]
    findings, covered = [], []

    def issue(status, number, message):
        location = f"{path}:{number}" if number else str(path)
        findings.append((status, channel, location, message))

    occurrences = [(n, match[1]) for n, line in text_lines for match in re.finditer(r"\bepisode\s*(?:no\.?\s*|[#:]\s*)?(\d+)\b", line, re.I)]
    if not occurrences:
        issue("FAIL", None, "Episode is missing (use 'Episode N').")
    else:
        covered.append("Episode")
        for number, value in occurrences:
            if int(value) != int(facts["Episode"]):
                issue("FAIL", number, f"Episode {value}; expected Episode {facts['Episode']}.")

    for field in ("Speaker", "Affiliation", "Topic", "Moderator", "Date", "Time"):
        labeled = []
        for number, line in text_lines:
            value = labeled_value(line, field)
            if value is not None:
                labeled.append((number, value))
        matches = [(n, line) for n, line in text_lines if contains(line, facts[field])]
        if matches:
            covered.append(field)
        if labeled:
            for number, value in labeled:
                if not labeled_match(field, value, facts):
                    issue("FAIL", number, f"{field}: '{brief(value)}'; expected '{brief(facts[field])}'.")
        elif not matches:
            issue("FAIL", None, f"Required {field} not found in the supplied wording: '{brief(facts[field])}'. Check missing content or alternative formatting manually.")

    links, unresolved = get_links(lines)
    for number in unresolved:
        issue("REVIEW", number, "Unresolved Markdown reference link; actual destination could not be checked.")
    known = {url_key(facts[field]) for field in ("Zoom", "Website")}
    known.update(url_key(value) for value in allowed)
    seen_keys = set()
    for number, value in links:
        try:
            key = url_key(value)
        except (ValueError, InputError):
            issue("REVIEW", number, "Malformed HTTP(S) link; inspect its destination manually.")
            continue
        seen_keys.add(key)
        if is_zoom(value) and key != url_key(facts["Zoom"]):
            issue("FAIL", number, f"Zoom destination differs from expected Zoom: `{brief(value)}`.")
        elif key not in known:
            issue("REVIEW", number, f"Unverified link: `{brief(value)}`. Verify it and add the exact URL to Allowed links, or remove it.")
    for field in ("Zoom", "Website"):
        for number, line in text_lines:
            if labeled_value(line, field) is not None:
                targets = [value for n, value in links if n == number]
                try:
                    match = bool(targets) and all(url_key(value) == url_key(facts[field]) for value in targets)
                except (ValueError, InputError):
                    match = False
                if not match:
                    issue("FAIL", number, f"Labeled {field} must point to the expected full {field} URL.")
        if url_key(facts[field]) in seen_keys:
            covered.append(field)
        else:
            issue("FAIL", None, f"Required {field} destination is missing or differs from the expected full URL.")
    return findings, (channel, len(covered), len(links))


def main():
    parser = argparse.ArgumentParser(description=__doc__, epilog="Checks numeric 'Episode N' occurrences, expected wording, labeled facts and HTTP(S) links. Whitespace, case, punctuation and common honorifics are normalized for text only. Alternate date/time formats, paraphrases, HTML links and contradictions in unlabeled prose need human review. No networking, writes or account actions. Exit codes: 0 no mechanical findings; 1 findings; 2 invalid input.")
    parser.add_argument("--run", metavar="run-N.md", help="Read Expected facts, LinkedIn, INFORMS and Email H2 sections from one file.")
    parser.add_argument("--facts", help="Read an Expected facts H2 table from this file.")
    parser.add_argument("--linkedin", help="LinkedIn draft file (use with --facts).")
    parser.add_argument("--informs", help="INFORMS draft file (use with --facts).")
    parser.add_argument("--email", help="Email draft file (use with --facts).")
    args = parser.parse_args()
    separate = [args.facts, args.linkedin, args.informs, args.email]
    if bool(args.run) == bool(any(separate)) or (not args.run and not all(separate)):
        parser.error("Use --run alone, or all four: --facts --linkedin --informs --email.")
    try:
        if args.run:
            lines = read_lines(args.run)
            facts, allowed = read_facts(lines)
            drafts = [(channel, args.run, section(lines, channel)) for channel in CHANNELS]
        else:
            facts, allowed = read_facts(read_lines(args.facts))
            drafts = [(channel, path, read_lines(path)) for channel, path in zip(CHANNELS, separate[1:])]
            if any(not any(line.strip() for _, line in lines) for _, _, lines in drafts):
                raise InputError("Every draft file must contain text.")
        findings, coverage = [], []
        for channel, path, lines in drafts:
            result, counts = check_draft(channel, path, lines, facts, allowed)
            findings.extend(result)
            coverage.append(counts)
    except (InputError, ValueError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2
    print("### Promotion consistency check\n")
    print("Read-only comparison against the supplied expected facts; no files or accounts changed.\n")
    if findings:
        for status, channel, location, message in findings:
            print(f"- **{status} · {channel}** — {location}: {message}")
    else:
        print("No mechanical discrepancies found in the supported checks.")
    print("\n### Coverage\n\n| Draft | Expected values found | HTTP(S) destinations checked |\n|---|---:|---:|")
    for channel, covered, links in coverage:
        print(f"| {channel} | {covered}/{len(FIELDS)} | {links} |")
    print("\nPresence counts are not a pass score: supported labels at the start of a line (optionally preceded by bullets, punctuation or emoji), numeric 'Episode N' mentions and detected URLs are checked even when a correct copy also appears.")
    print("\nLimits: text must preserve the supplied fact wording (punctuation, whitespace, case and common honorifics may differ). Different date/time formats and paraphrases may be flagged. Use full URLs on their own or as Markdown targets; URL punctuation is significant. Contradictions in unlabeled prose, semantic research claims, source truth, HTML links, attachments and live account state are not checked. Verify calendar-link event details manually even when its URL is allowed. This report never authorizes Post or Send.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

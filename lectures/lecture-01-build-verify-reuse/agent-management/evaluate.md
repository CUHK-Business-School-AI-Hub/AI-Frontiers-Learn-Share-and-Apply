# Evaluate: assess the outputs against the selected input

Read the run's source record and inspect the underlying sources when needed. Assess all three messages produced through [delegate.md](delegate.md). In example mode, assess against the selected brief in examples/, not the current inputs/ data.

## Mechanical check

Use [check_promotion.py](check_promotion.py) before filling the accounts and after revising the messages. It reads local files and prints a report. It does not browse, edit files, operate accounts, or post/send anything.

In the run file, use this structure. Replace every placeholder with verified current facts and actual draft text. Keep the expected-facts and current-message headings exactly as shown, once each. Record source links and the access date in a separate source-record section.

```markdown
## Expected facts

| Field | Value |
|---|---|
| Episode | <episode number> |
| Speaker | <speaker name> |
| Affiliation | <speaker affiliation> |
| Topic | <full talk title> |
| Moderator | <moderator name and affiliation> |
| Date | <event date> |
| Time | <start–end time and time zone> |
| Zoom | <full verified Zoom URL, including password parameters> |
| Website | <verified event website URL> |

## LinkedIn
<current LinkedIn message>

## INFORMS
<current INFORMS message>

## Email
<current email subject and body>
```

An optional `Allowed links` row may list additional verified URLs, separated by spaces. Leave it out when there are none. Expected facts come from inputs/ and the verified event source, or the fixed brief in example mode. Preserve the previous facts and explain any source correction. Never change an expected value merely to make a draft pass.

From this demo folder, run:

```sh
python3 check_promotion.py --run run-1.md
```

Replace `run-1.md` with the current run filename. Copy the report under a separate `## Mechanical check — initial` or reassessment heading, with the command and checked draft version. Do not paste the report inside one of the three current-message sections.

- Exit `0`: no mechanical findings within the checker's coverage. Continue the agent assessment below.
- Exit `1`: discrepancies or items requiring review. Resolve each `FAIL` or `REVIEW`, or record a supported explanation for a formatting-related finding.
- Exit `2`: invalid or missing input. Correct the file structure or identify missing facts, then rerun. This is not a completed check.

The checker compares expected values with draft text, repeated episode references, labeled fields, and link destinations. Different wording or date/time formats may need manual assessment. It cannot establish source truth, interpret research claims, exhaustively detect contradictory prose, or verify an app's live draft. Do not convert a mechanical pass into an overall approval.

For the original failure exercise, use the example command in README.md. After coaching, put the corrected copies and fixed case facts in the run file and use `--run` to reassess them. Keep examples/ unchanged.

## Criteria

| Criterion | Assessment |
|---|---|
| Event facts | Episode, speaker, affiliation, title, moderator, date, time, and time zone match the selected source wherever they appear. |
| Links | Actual destinations match the intended event or series resource. Inspect hyperlink targets as well as display text, including calendar-event details if present. |
| Research meaning | Claims follow the source and retain its qualifications. Unsupported conclusions or invented results require revision. |
| Channel fit | Each message retains its reference template's purpose, structure, tone, and appropriate level of detail. |
| Consistency | The subjects, bodies, event blocks, and three channel versions agree. |
| Completeness and handoff | Required details are present or explicitly unresolved. Destination information matches the selected input. |
| Live drafts (current assignment only) | After filling the apps, inspect the personal account identity, LinkedIn group, every requested INFORMS community, and Outlook From/recipient/Cc fields. Check subjects, bodies, formatting, and link targets against the assessed messages and inputs. Record whether each item is a saved draft, an open composer, or blocked. Nothing is posted, sent, or scheduled. |

Write the actual findings in the run file:

| Message / criterion | Pass, Revise, Needs information, Pending, or N/A | Observed evidence | Expected value / source |
|---|---|---|---|

Cover each criterion across the three messages. Use the mechanical report as evidence, then assess meaning, qualifications, tone, and completeness yourself. Assess content before filling the apps, then check every live destination on screen. Mark the live-draft criterion pending until that inspection, and not applicable in example mode. Group shared passes, but give each distinct failure its own row. Quote the problematic text or destination and cite the source that establishes the discrepancy. Separate observations from hypotheses about their causes. Distinguish the script's mechanical findings from the agent's judgments. Neither is an independent guarantee.

## Decision and reassessment

- **Needs revision:** pass the findings to [coach.md](coach.md).
- **Needs information:** identify the missing or conflicting source detail and the question that would resolve it. Correct supported errors while leaving that gap open.
- **Content ready:** the messages satisfy the content criteria. For the current assignment, proceed to fill the accounts according to delegate.md, then assess the live drafts. In example mode, proceed directly to human review of local outputs.
- **Ready for human review:** all requested live drafts have been filled and checked, with their locations and statuses recorded. In example mode, only local outputs are required. This does not authorize posting or sending.
- **Partially prepared:** content is available, but an account, destination, or recipient detail prevents completion of one or more live drafts. Identify the exact gap and completed items.

After coaching, reread all three messages against the same source record. Show whether earlier failures are resolved and whether new errors appeared. Retain the earlier assessment. If source data changes during a run, record the change explicitly and reassess all affected messages; do not silently change the expected answer.

## Additional checks from coaching

No additional checks yet. coach.md may add checks justified by diagnosed failures. Keep them reusable and preserve the base criteria above.

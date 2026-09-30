# Maintain the training resources

All documentation, navigation, file descriptions, and exercise instructions are written in English. These training materials are approved for public sharing.

## Naming and file roles

- Display lecture numbers as `Lecture 01`, `Lecture 02`, and so on.
- Use `lectures/lecture-NN-short-topic/` for each lecture. Use lowercase file names with hyphens, except `README.md` and conventional Python names such as `check_promotion.py`.
- Put the date and full title in the lecture README and brief. Avoid repeating them in every file name.
- Each lecture has a README resource map, a brief, slides where available, and descriptive exercise folders.
- Each exercise guide explains its purpose, prerequisites, starting prompt or steps, every supplied file, and expected outputs.
- Keep instructor instructions separate from learner quick starts. Clearly label deliberately flawed examples and answer keys.
- Use relative links within the repository. Use website URLs for online slides and explicit download links for attachments.
- Preserve exact checker-required headings such as `## Expected facts`, `## LinkedIn`, `## INFORMS`, and `## Email`.

## Add or update a lecture

1. Create its folder under lectures/ and add its resource guide and brief.
2. Add exercises and describe every supplied file in their guides. Keep each exercise usable on its own.
3. Add canonical `slides.html` if available. Update file references in slide text and speaker notes when files move.
4. Add the lecture to the root README and docs/index.html. Create or update its website event page with links to the resource guide, exercises, and online slides.
5. Run `python3 scripts/build_site.py` to copy the canonical slides into docs/. Do not edit those generated copies directly.
6. Check Markdown links and website links. Open the website and slides in a browser. Run documented checker commands; the intentionally flawed example set should return findings, not a clean result.
7. Commit the source materials and generated website files together, then push to the configured GitHub Pages source branch.

## Website deployment

The existing site files live in docs/. In the repository's **Settings → Pages**, use **Deploy from a branch**, select the intended publication branch (normally main), and select **/docs**. Confirm these settings in GitHub before the first publication; local files alone do not establish the remote configuration. GitHub publishes the site after a push to that configured source.

Keep docs/events/2026-09-29-build-verify-reuse.html available: previously distributed links use this address. The updated page also serves as the Lecture 01 resource entry point.

The build script copies lecture slides only. The website index, event pages, and stylesheet are maintained in docs/. After a deployment, check the online index, lecture resource links, slide navigation, and downloads.

## Repository or Google Drive?

Keep Markdown, scripts, small Word templates, and HTML slides in the repository. Current Lecture 01 materials fit this arrangement; Google Drive is not required for them.

Use Google Drive for future recordings and large attachments. Set every shared training file to **General access → Anyone with the link → Viewer**, as approved for this series. Check the actual file link in a signed-out browser before adding it to the lecture guide. Describe the content, format, and size or duration beside the link. No sign-in or access request should be needed.

Maintain one canonical copy of each resource: repository files are edited here; Drive-hosted attachments are maintained in Drive. Do not upload duplicate copies of small exercise files merely to provide a second location.

[← Series resources](README.md)

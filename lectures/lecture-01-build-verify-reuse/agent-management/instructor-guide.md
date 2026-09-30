# Instructor guide: managing a real promotion task

[← Learner guide](README.md) · [Lecture 01](../README.md)

This folder is self-contained. The default workflow creates promotional messages for the event selected in inputs/, evaluates them, and automatically improves the local procedure when it diagnoses a failure. It then uses computer use to fill posts in your personal LinkedIn and INFORMS accounts and an email draft in your personal Outlook account. It stops before Post or Send for your review. It needs document access, browsing, and computer use. One small Python checker assists with factual and link comparisons. It requires Python 3, with no extra packages.

## Files and folders

| Item | Role |
|---|---|
| [playbook.md](playbook.md) | Agent entry point and complete execution loop. |
| [delegate.md](delegate.md) | Procedures and success standard. |
| [evaluate.md](evaluate.md) | Evidence-based assessment and reassessment. |
| [coach.md](coach.md) | Automatic, targeted improvements to procedures and outputs. |
| [check_promotion.py](check_promotion.py) | Read-only mechanical checks against the current run's verified facts. |
| [inputs/assignment.md](inputs/assignment.md) | Current episode selection, source website, destinations, and email routing information. |
| `inputs/*.docx` | Reference messages for the three channel styles. |
| [examples/case-brief.md](examples/case-brief.md) | Optional fixed case with problematic drafts and its own reference facts. |

## Run the current assignment

Open this folder as the agent's working folder. Make your signed-in LinkedIn, INFORMS, and Outlook sessions available, together with access to the email list linked in inputs/assignment.md. Then give the agent this prompt:

> Follow playbook.md to complete the current assignment in inputs/. Read inputs/assignment.md and the three Word templates, retrieve the requested event's information from the specified source, and prepare the three promotional messages. Run check_promotion.py as described in evaluate.md, assess the remaining criteria, automatically apply justified coaching improvements, and reassess. Use computer use in my personal LinkedIn, INFORMS, and Outlook accounts to fill the LinkedIn group post, a post for every specified INFORMS community, and the email with its recipients, Cc, subject, and body. Check the filled drafts on screen and leave them available for my review. Keep the work, checker reports, exact process changes, and draft locations/statuses in the next unused run-N.md. Stop before clicking Post or Send. Do not publish or schedule anything.

The agent should produce one new `run-N.md` containing the source record, initial findings, any process changes, current messages, checker reports, destination information, live-draft locations/statuses, and reassessment. evaluate.md provides the short facts-table and message-section format used by the checker. The live result should be one filled LinkedIn group composer, a filled composer for every specified INFORMS community, and one unsent Outlook draft. A platform may retain only an open composer, so the agent should identify that state and keep it open. It should use the actual inputs, not the failure examples. If the first drafts satisfy the criteria, a run with no coaching changes is a valid outcome.

Review the final messages and the evidence, then inspect the filled account drafts, destinations, and recipient fields yourself. The workflow leaves Post and Send for you after review. Inspect **Learned procedures** in delegate.md and **Additional checks from coaching** in evaluate.md to see what changed. The agent performs the evaluations. You remain the independent reviewer. These Markdown instructions guide behavior rather than enforcing it mechanically.

## Change the episode by changing inputs/

1. Update the episode and speaker in inputs/assignment.md. Change the source or destination details there when needed.
2. Keep or replace the three Word templates according to the styles you want. Their historical event facts should not become defaults.
3. If the website is inaccessible or incomplete, put the verified event facts and supporting abstract in inputs/assignment.md, or add a clearly named source file inside inputs/ and reference it from inputs/assignment.md. State its source and date. Identify any explicit correction.
4. Start a new run with the same prompt. No edit to delegate.md, evaluate.md, coach.md, or playbook.md is required merely because the episode changes.

The agent rereads inputs/ each time. Required missing or conflicting details should produce a specific question, not an invented value. The run record captures the facts used for that run so you can understand later changes.

## Run the mechanical checker

The agent runs this as part of evaluate.md. You can also run it yourself from this folder:

```sh
python3 check_promotion.py --run run-1.md
```

Use your actual run filename. The script reads its expected-facts table and three current-message sections. It prints a Markdown report without changing any file or accessing any account. Preserve the report in the run record separately from the drafts. It checks explicit facts and URLs, including actual Markdown hyperlink targets. It does not extract the Word templates, judge research claims, or check the live account drafts.

Exit `0` means no mechanical findings within its coverage, `1` means discrepancies or review items, and `2` means the check could not run because its inputs were invalid or missing. A clean result is not approval to post or send. Alternate wording or date/time formats can need manual assessment. If Python is unavailable, the agent should report the skipped check and compare the facts manually. No dependency installation is required.

## Optional failure exercise

Use this when you want a predictable coaching demonstration:

> Follow playbook.md in example mode. Use examples/case-brief.md and its three problematic drafts. Run check_promotion.py on the originals, assess the remaining criteria before making corrections, then coach and reassess. Preserve the originals and record the changes and checker reports in a new run-N.md. Do not read examples/instructor-notes.md before completing the exercise.

To run only the mechanical check on the existing cases:

```sh
python3 check_promotion.py --facts examples/case-brief.md \
  --linkedin examples/linkedin.md \
  --informs examples/informs.md \
  --email examples/email.md
```

This command intentionally returns `1` because the supplied drafts contain errors. It does not revise them. After coaching, the agent copies the fixed case facts and corrected messages into the new run file and checks that file with `--run`. The script's limited findings are only part of the evaluation. Continue the source-aware assessment in evaluate.md.

The case has its own fixed reference brief, so it remains usable after you change the current event in inputs/. Example mode stays local and does not fill your accounts. Read [examples/instructor-notes.md](examples/instructor-notes.md) for the answer key. The examples are deliberately flawed teaching material, not live-agent results.

## Repeat and preserve learning

Each run creates a new results file. Source inputs and example cases stay unchanged during execution. Learned procedures persist in the designated sections, and the run file records their exact old and new text. To reset the learning for a classroom repeat, restore those sections from the saved previous text, or work in a copy of this folder.

No messages are posted, sent, or scheduled by this workflow. Account drafts count as prepared only after the agent has filled and inspected them. If access or missing information blocks a destination, the agent should report partial completion and the specific help needed while preserving the usable work.

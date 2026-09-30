# Agent Management · Delegate, evaluate, and coach

Practice giving an agent a clear assignment, checking its work, improving reusable procedures, and recording what changed. Choose one of the two modes below. Start in a copy of this folder so you can repeat the exercise from the original material.

## Start here: local failure exercise

This mode uses a fixed case and deliberately flawed drafts. It needs an agent with local file access; Python 3 runs the included checker without additional packages. No account access is needed.

1. Open this folder as your agent's working folder.
2. Give it the following prompt.
3. Review the new run file, compare initial and revised messages, and read the answer key after completing your assessment.

> Follow playbook.md in example mode. Use examples/case-brief.md and its three problematic drafts. Run check_promotion.py on the originals, assess the remaining criteria before making corrections, then coach and reassess. Preserve the originals and record the changes and checker reports in a new run-N.md. Do not read examples/instructor-notes.md before completing the exercise.

**Expected result:** a new `run-1.md` (or the next unused number) with initial findings, corrected messages, checker reports, reassessment, and exact changes to learned procedures. The example drafts stay unchanged. The answer key explains why checking facts alone does not catch every failure.

## Next: current assignment with app drafts

This mode adds event research and computer use. Read [inputs/assignment.md](inputs/assignment.md), update the selected event and destinations for your intended exercise, and provide document, browser, and app access. The supplied setup describes the instructor's demonstration accounts.

> Follow playbook.md to complete the current assignment in inputs/. Read inputs/assignment.md and the three Word templates, retrieve the selected event's information from its source, and prepare the three promotional messages. Run check_promotion.py as described in evaluate.md, assess the remaining criteria, apply justified coaching improvements, and reassess. Use computer use to fill the LinkedIn group draft, a draft for every specified INFORMS community, and the Outlook email with its recipients, Cc, subject, and body. Inspect the filled drafts and leave them available for my review. Record the work, checker reports, exact process changes, and draft locations/statuses in the next unused run-N.md. Stop before Post or Send.

**Expected result:** a run record plus checked LinkedIn, INFORMS Connect, and Outlook drafts. Report any incomplete destination explicitly. For a later event, update the inputs and repeat the same workflow.

## Every file and folder

| Item | Purpose / when to read it |
|---|---|
| [README.md](README.md) | Learner setup, mode selection, and copyable launch prompts. |
| [instructor-guide.md](instructor-guide.md) | Detailed demonstration, checker, repeat-run, and debrief instructions. |
| [playbook.md](playbook.md) | Agent entry point: selects the mode, coordinates the loop, and defines the run record. |
| [delegate.md](delegate.md) | Work procedures, success standard, and persistent learned procedures. |
| [evaluate.md](evaluate.md) | Assessment criteria, checker input format, and additional checks learned through coaching. |
| [coach.md](coach.md) | How to diagnose failures, improve the permitted procedure sections, and reassess. |
| [check_promotion.py](check_promotion.py) | Read-only Python checker for expected event facts and links. |
| [inputs/README.md](inputs/README.md) | Guide to the current assignment and its templates. |
| [inputs/assignment.md](inputs/assignment.md) | Episode, speaker, source, destinations, and email routing for the current assignment. |
| [inputs/linkedin.docx](inputs/linkedin.docx) | LinkedIn style reference. |
| [inputs/informs.docx](inputs/informs.docx) | INFORMS Connect style reference. |
| [inputs/email.docx](inputs/email.docx) | Email invitation style reference. |
| [examples/README.md](examples/README.md) | Fixed exercise instructions and file map. |
| [examples/case-brief.md](examples/case-brief.md) | Saved reference facts for the failure exercise. |
| [examples/linkedin.md](examples/linkedin.md) | Deliberately flawed LinkedIn draft. |
| [examples/informs.md](examples/informs.md) | Deliberately flawed INFORMS draft. |
| [examples/email.md](examples/email.md) | Deliberately flawed email draft. |
| [examples/instructor-notes.md](examples/instructor-notes.md) | Answer key; read after assessing the drafts. |
| `run-N.md` (generated) | One execution's facts, drafts, findings, changes, and final status. |

## Run the checker yourself

From this folder:

```sh
python3 check_promotion.py --facts examples/case-brief.md \
  --linkedin examples/linkedin.md \
  --informs examples/informs.md \
  --email examples/email.md
```

The supplied examples intentionally return exit code `1`. After an agent creates a run record, check it with `python3 check_promotion.py --run run-1.md`. Exit `0` means no mechanical findings, `1` means findings to assess, and `2` means invalid or missing inputs. Always assess research meaning and channel fit as well.

[← Lecture 01](../README.md) · [Computer Use](../computer-use/README.md)

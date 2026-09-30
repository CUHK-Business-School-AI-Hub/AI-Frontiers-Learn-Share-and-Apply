# Playbook: Service Science promotion

Read [delegate.md](delegate.md), [evaluate.md](evaluate.md), and [coach.md](coach.md), then run the complete workflow. All local task resources are in this folder.

## Select the inputs

**Default: current assignment.** Read [inputs/assignment.md](inputs/assignment.md) and the three Word templates in inputs/. Retrieve the requested event's details from the source identified there. Create new promotional messages. Do not use examples/ as current event data or copy an earlier run's facts.

**Optional: example mode.** Only when explicitly requested, use [examples/case-brief.md](examples/case-brief.md) and its three problematic drafts. Assess them before making corrections. Keep this fixed case separate from the current assignment. Do not read examples/instructor-notes.md during the exercise.

## Run the loop

1. **Delegate:** establish the source facts and produce the three messages according to delegate.md. In example mode, begin with the supplied drafts.
2. **Evaluate:** run check_promotion.py on the current drafts as described in evaluate.md, then assess meaning, channel fit, and source quality yourself. Record the mechanical report separately from the agent's assessment.
3. **Coach:** if failures exist, automatically improve the permitted procedure/checklist sections, revise the affected messages, and evaluate again. Follow coach.md without waiting for a separate coaching prompt.
4. **Fill and verify:** for the current assignment, use computer use as specified in delegate.md to fill the LinkedIn composer, a composer for every requested INFORMS community, and an Outlook email draft in Philip's personal accounts. Inspect the actual fields using evaluate.md. Example mode stays local and skips this step.
5. **Finish:** leave the filled drafts available for Philip's review, without clicking Post or Send. Identify missing information, inaccessible destinations, and unresolved failures. Allow at most two revision rounds after the initial assessment, including any corrections after filling the apps. If the outputs already meet the requirements, do not invent errors or unnecessary procedure changes.

## Keep one record per run

Create the next unused `run-1.md`, `run-2.md`, and so on here. Include:

- Task and source facts, with the input filenames, source links, and access date. Use the exact `## Expected facts` table format in evaluate.md.
- Initial assessment, quoting evidence for failures.
- Process changes, preserving the exact old and new section text.
- Current LinkedIn, INFORMS Connect, and email messages under the exact headings `## LinkedIn`, `## INFORMS`, and `## Email`. Keep each heading once, containing only its message. Put destinations and other notes in separate sections.
- Mechanical checker reports, including the command, result, and which draft version was checked.
- For the current assignment, each account/destination, draft location or open tab, observed saved/open/blocked status, and the result of checking the filled fields. Do not copy the full recipient list into the run file. Record its source and recipient count instead.
- Reassessment, unresolved questions, and final status.

Preserve the initial messages under `## Initial drafts` before revising the current message sections. Use level-three headings there so the checker selects only the current drafts. For example mode, the unchanged files in examples/ are the initial record. Keep earlier assessments if another round is needed.

Use ordinary document reading, browsing, file editing, and computer use, plus the included Python checker. It requires Python 3 and no additional packages. If Python is unavailable, record that the checker was not run and perform the comparisons manually. Do not claim a script pass. The current assignment ends with verified, filled drafts in Philip's accounts, awaiting his review. Do not post, send, publish, or schedule messages. Example mode ends with local outputs only.

coach.md may change only **Learned procedures** in delegate.md and **Additional checks from coaching** in evaluate.md. Treat inputs/ and examples/ as read-only during execution. The user can update inputs/ between runs; reread it on every run.

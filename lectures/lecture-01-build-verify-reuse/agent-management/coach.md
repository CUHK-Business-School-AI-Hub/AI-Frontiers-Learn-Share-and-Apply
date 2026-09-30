# Coach: improve the procedure and the result

Use the findings from [evaluate.md](evaluate.md). Make focused improvements automatically, then return to evaluation.

1. **Diagnose:** quote the failure and identify its likely process cause. Use the checker's report for mechanical discrepancies and the agent assessment for meaning or channel issues. Confirm a reported discrepancy against its source before treating it as a content failure. Treat the cause as a hypothesis unless the evidence establishes it. Group related failures.
2. **Choose a change:** draft a specific, reusable rule for **Learned procedures** in [delegate.md](delegate.md). If a concrete check is missing, draft it for **Additional checks from coaching** in evaluate.md. Avoid duplicates and vague reminders.
3. **Record and apply:** preserve the exact previous section text in the run file, record the proposed replacement and supporting finding, then make the local update without waiting for another coaching prompt.
4. **Revise:** apply the improved procedure to every affected message, including any already-filled live drafts, and keep the run-file copies consistent. Preserve the initial output and earlier assessments. Never post or send during correction. In example mode, leave the original case files unchanged and retain the training label on corrected copies.
5. **Reassess:** rerun check_promotion.py on the current message sections, preserve its new report, and follow the remaining evaluate.md criteria again. Check that the failure is resolved and that acceptable content remains acceptable. If the change causes a new problem, revise or undo it within the remaining round.

Use at most two revision rounds after the initial assessment, including corrections to live drafts. When content passes, return to playbook.md to fill and verify the accounts before the current assignment finishes. Stop with unresolved issues when required evidence is unavailable or the limit is reached. Report access problems as blockers rather than inventing a coaching rule to bypass them.

Only the two designated procedure/checklist sections may change automatically. Do not alter inputs/, examples/, check_promotion.py, base success criteria, or this coaching policy to make the result pass. Do not change verified expected facts merely to match a faulty draft. Keep changing event values in the input and source record, never in a permanent rule.

The run record must connect the finding, diagnosis, procedure change, revised output, and reassessment. Report what this run demonstrates without claiming universal reliability. If no failure justifies an improvement, leave the procedure unchanged.

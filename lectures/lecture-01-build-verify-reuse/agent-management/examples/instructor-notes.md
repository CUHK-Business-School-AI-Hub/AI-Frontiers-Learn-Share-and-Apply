# Instructor answer key

These authored examples contain four planted failures across three drafts. Assess them against [case-brief.md](case-brief.md), regardless of which episode the current inputs/ folder specifies.

| Draft | Failure | Correction | Possible process improvement |
|---|---|---|---|
| LinkedIn | The Zoom destination contains the previous meeting ID `93641303385`. | Use the full approved URL containing `94727057139`, including its password parameters. | Compare actual hyperlink destinations with the selected event source. |
| INFORMS Connect | Moderator is Mustafa Akan. | Use Prof. Vince Slaugh (Cornell University). | Keep changing event fields separate from reusable writing structure. |
| Email | The subject says Episode 14 but the event block says 13. | Use Episode 14 throughout. | Check repeated references in the subject, body, and event details. |
| Email | “The study proves that AI personas increase productivity for every user.” | Replace it with the supported description of AI persona, service use, and differences across user intents. | Check every claimed finding against its source and preserve the qualifications. |

The included check_promotion.py should flag the three factual discrepancies: Zoom, moderator, and episode number. It may report both the wrong URL and the missing expected URL for the same failure. It does not judge the unsupported productivity claim. After fixing only the three factual discrepancies, a mechanical check can pass while that research claim remains wrong. Use this distinction to demonstrate why evaluate.md still requires source-aware assessment. Do not add a hardcoded phrase check just to make the example pass.

Accept different rule wordings if they address the observed evidence. Related failures may justify one shared procedure improvement. Do not require one new rule per error.

The agent should preserve these originals, write its assessments and corrected copies into a new run file, and update only the permitted procedure/checklist sections. A later example run may correctly find that existing learned rules already address a failure; it should apply them without adding duplicates.

The examples demonstrate the management loop. They do not measure live-model reliability or establish that new events will be handled correctly. Review genuine runs separately.

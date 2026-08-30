# Triage Log — v0.2 Grade Statistics

## Issue Priority Ranking

1. #10 — Negative scores are accepted
   - Severity: High
   - Priority: P1
   - Decision: Fix this sprint
   - Rationale: Negative scores can corrupt grade statistics and produce invalid results, so this defect needs an early fix.

2. #11 — Duplicate roll numbers are allowed
   - Severity: High
   - Priority: P1
   - Decision: Fix this sprint
   - Rationale: Duplicate roll numbers can identify multiple students as the same student and cause incorrect records.

3. #9 — average() crashes when student has no scores
   - Severity: High
   - Priority: P1
   - Decision: Fixed
   - Rationale: The application crashed for a valid empty-score case, so it was treated as a high-impact defect and fixed first.

4. #12 — Incorrect rounding of averages
   - Severity: Medium
   - Priority: P2
   - Decision: Wontfix this sprint
   - Rationale: Incorrect rounding affects displayed statistics but does not crash the application, so it can be deferred.

5. #13 — Name comparison is case-sensitive
   - Severity: Low
   - Priority: P3
   - Decision: Wontfix this sprint
   - Rationale: Case-sensitive name comparison has limited impact and is lower priority than defects affecting grade correctness or student identity.

## Severity vs Priority Trade-offs

Issue #9 had High severity and P1 priority because it caused the application to crash during a valid grade calculation. It was therefore fixed immediately.

Issue #13 has Low severity and P3 priority because the defect has limited business impact and does not prevent the main grading functionality from working.

Issue #12 has Medium severity but P2 priority because incorrect rounding affects the accuracy of displayed results, but it is less urgent than crashes, invalid scores, or duplicate student records.

## Sprint Decision

Issues #9, #10, and #11 are the three defects selected for this sprint. Issues #12 and #13 are deferred and will not be fixed in this sprint because they have lower impact and priority.
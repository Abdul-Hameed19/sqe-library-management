# Lab 8 — Test-Driven Development Log

## Feature
`rank_students(roster)`

## Cycle 1 — Empty Roster
- RED commit: `26c42ae`
- GREEN commit: `f41d3a8`
- Expected behaviour: Empty roster returns an empty list.
- Result: Passed.

## Cycle 2 — Single Student
- RED commit: `1c2866a`
- GREEN commit: `e4bad22`
- Expected behaviour: A roster containing one student returns that student.
- Result: Passed.

## Cycle 3 — Descending Average
- RED commit: `89f6db0`
- GREEN commit: `7520e0f`
- Expected behaviour: Students are ranked by average score in descending order.
- Result: Passed.

## Cycle 4 — Alphabetical Tie-Breaking
- RED commit: `908d039`
- GREEN commit: `758cc35`
- Expected behaviour: Students with equal averages are ranked alphabetically by name.
- Result: Passed.

## Cycle 5 — Edge Cases
- Edge case 1: Case-insensitive alphabetical tie-breaking.
- Edge case 2: A zero-average student ranks after a student with a positive average.
- Test commit hashes: To be added after committing and verifying the changes.
- Result: Both edge-case tests passed.

## Regression Testing
- Ranking tests: 6 passed.
- Full test suite: Pending verification.
- Regressions: To be recorded after the full test suite.

## TDD Retrospective
Writing tests before implementation helped clarify the expected behaviour of the ranking function. The empty-roster and single-student tests established the basic requirements. Sorting and tie-breaking tests helped define the ranking rules clearly. Edge-case tests improved confidence in handling different names and zero averages. The Red-Green-Refactor approach encouraged small, testable changes instead of implementing everything at once.
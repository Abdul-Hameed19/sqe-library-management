# Requirements Traceability Matrix — GradeBook

| Requirement ID | Requirement                                                                                            | Test Case ID(s)                | Coverage |
| -------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------ | -------- |
| REQ-1          | The system shall allow a student to add a valid numeric score.                                         | TC-001                         | Covered  |
| REQ-2          | The system shall reject negative scores.                                                               | TC-002                         | Covered  |
| REQ-3          | The system shall reject non-numeric score input.                                                       | TC-003                         | Covered  |
| REQ-4          | The system shall correctly calculate the average when a student has multiple scores.                   | TC-004                         | Covered  |
| REQ-5          | The system shall correctly calculate the average for empty and single-score lists.                     | TC-005, TC-006                 | Covered  |
| REQ-6          | The system shall reject a duplicate roll number.                                                       | TC-007                         | Covered  |
| REQ-7          | The system shall handle student names without treating letter case as different.                       | TC-008                         | Covered  |
| REQ-8          | The system shall correctly handle score boundaries and convert scores to the appropriate grade letter. | TC-009, TC-010, TC-011, TC-012 | Covered  |

## Traceability Summary

All eight defined GradeBook requirements have at least one linked test case. No requirement is currently untraced. The test cases cover positive, negative, functional, boundary, and error-path scenarios required by the lab.

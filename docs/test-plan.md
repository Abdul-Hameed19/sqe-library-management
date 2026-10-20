# Software Test Plan — GradeBook

## 1. Introduction

The purpose of this test plan is to verify the functional correctness and quality of the GradeBook module. The testing will focus on student score management, average calculation, duplicate roll number handling, score boundaries, name comparison, and grade conversion. Testing will be performed against the current GradeBook codebase using manual execution and existing Python tests.

## 2. Test Items

The following GradeBook components will be tested:

* `Student` class
* `Student.__init__()`
* `Student.add_score()`
* `Student.average()`
* Duplicate roll number validation
* Score validation and boundaries
* Name comparison behavior
* Grade-letter conversion

## 3. Features to be Tested

The following functional features are within the testing scope:

* Adding valid scores to a student.
* Rejecting negative scores.
* Handling non-numeric score input.
* Calculating averages for multiple scores.
* Calculating averages for empty and single-score lists.
* Rejecting duplicate roll numbers.
* Case-insensitive student name comparison.
* Handling minimum and maximum score boundaries.
* Converting numerical scores to grade letters.

## 4. Features Not to be Tested

The user interface is out of scope because GradeBook is currently implemented as a Python module/library rather than a graphical application. Database integration, web services, network performance, and deployment infrastructure are also excluded because they are not part of the current implementation. Performance and security testing will only be considered if these features are added to the system later.

## 5. Test Approach

Testing will use functional, negative, boundary-value, and regression testing techniques. Functional tests will verify expected behavior for valid inputs, while negative tests will verify that invalid inputs are correctly rejected or handled. Boundary testing will cover scores of 0 and 100 and grade-conversion boundaries. Existing tests from previous labs will also be considered as regression tests.

## 6. Pass/Fail Criteria

The test execution will be considered successful when at least 95% of the planned test cases pass and no Critical defects remain open. A test case will be marked Pass when the actual result matches the expected result. A test case will be marked Fail when the actual behavior differs from the expected result. A test may be marked Blocked when it cannot be executed because of a missing dependency or unavailable functionality.

## 7. Test Deliverables

The following deliverables will be produced:

* `docs/test-plan.md`
* `docs/test-cases.md`
* `docs/rtm.md`
* Manual test execution results
* GitHub Issues for identified defects
* Updated test evidence where required

## 8. Environmental Needs

Testing will be performed on a Windows development environment using Python. The source code will be stored in the GitHub repository and edited using Visual Studio Code. Python shell execution and the existing test files will be used for manual verification. Git and GitHub will be used for version control and defect tracking.

## 9. Schedule

| Activity                         | Planned Time |
| -------------------------------- | -----------: |
| Test Plan preparation            |   60 minutes |
| Test Case preparation            |   75 minutes |
| Requirements Traceability Matrix |   30 minutes |
| Manual Test Execution            |   35 minutes |
| **Total**                        |  **3 hours** |

## 10. Risks

The current implementation may not support all requirements specified for testing, which may result in failed test cases and GitHub defects. Existing tests may also contain incorrect assumptions about the current implementation. Changes made during testing could affect previously working functionality, so regression testing will be performed. Time constraints may also limit the depth of manual testing.

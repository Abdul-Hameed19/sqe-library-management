
# SonarCloud Static Code Analysis Findings

## 1. Overview

Static code analysis was performed using SonarQube Cloud for the `sqe-library-management` project.

The purpose was to identify bugs, vulnerabilities, code smells, and other code quality issues.

## 2. Initial and Final Analysis Results

The initial analysis of the main branch reported zero issues.

The final Pull Request analysis (#24) also reported zero new issues.

| Metric | Result |
|---|---:|
| Total issues on main | 0 |
| New issues in PR #24 | 0 |
| Accepted issues in PR #24 | 0 |
| Security hotspots in PR #24 | 0 |
| Coverage on new code | 0.0% |
| Duplication on new code | 0.0% |
| Quality Gate | Passed |

## 3. Severity Classification

No issues were detected in the analyzed results.

| Severity | Number of findings |
|---|---:|
| Blocker | 0 |
| Critical | 0 |
| Major | 0 |
| Minor | 0 |
| Info | 0 |

## 4. Top 8 Issues

SonarCloud did not report any issues in the analyzed Pull Request. Therefore, there were no findings to list among the top eight issues.

No rule IDs, file locations, or line numbers were available because no issues were detected.

## 5. Manual Code Quality Improvements

Although SonarCloud reported zero new issues, the following manual maintainability improvements were made in `src/gradebook.py`:

1. Replaced the maximum score value with the named constant `MAX_SCORE`.
2. Replaced the maximum name length with `MAX_NAME_LENGTH`.
3. Introduced `MIN_SCORES` and `MAX_SCORES` for score-count validation.
4. Created `GRADE_THRESHOLDS` to centralize grade boundaries.
5. Compiled the name-validation regular expression once and reused it through `NAME_PATTERN`.

These changes improve readability, maintainability, and reuse of validation rules. They are manual refactoring improvements, not five confirmed SonarCloud issue findings.

## 6. Analysis Warning

SonarCloud displayed one analysis warning stating that Python code was analyzed as compatible with versions 3.10 through 3.15 by default.

The project configuration contains `sonar.python.version=3.13`. However, the project uses SonarCloud Automatic Analysis, whose supported optional configuration does not list this parameter.

The warning did not prevent the analysis from completing or the Quality Gate from passing.

## 7. Risk Assessment

No bugs, vulnerabilities, or code smells were reported in the analyzed results.

However, zero reported issues does not guarantee that the software is completely free from defects.

The reported 0.0% coverage on new code indicates that SonarCloud did not report test coverage for the analyzed changes. This does not necessarily mean that no tests were written or executed.

## 8. Conclusion

SonarCloud analysis for Pull Request #24 completed successfully, with zero new issues and a passed Quality Gate.

Manual code quality improvements were also performed, and the existing test suite passed 62 tests.

The analysis results and improvements have been documented for the Static Code Analysis lab.

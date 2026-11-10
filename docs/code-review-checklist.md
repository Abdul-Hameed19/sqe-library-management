# Code Review Checklist — GradeBook System

## 1. Correctness
- [ ] Does the code produce the expected output?
- [ ] Are calculations and logical conditions correct?
- [ ] Are edge cases handled correctly?

## 2. Testing
- [ ] Are appropriate unit tests provided?
- [ ] Do tests cover normal and edge cases?
- [ ] Do tests verify actual behavior rather than implementation details?

## 3. Readability
- [ ] Are variable and function names meaningful?
- [ ] Is the code properly formatted and easy to understand?
- [ ] Are docstrings or comments provided where necessary?

## 4. Design
- [ ] Does the new code follow the existing project architecture?
- [ ] Is unnecessary code duplication avoided?
- [ ] Does the function have a clear and focused responsibility?

## 5. Risk
- [ ] Can the change break existing functionality?
- [ ] Are invalid inputs handled safely?
- [ ] Could the implementation introduce performance or security problems?

## 6. Lessons Learned (Retrospective)

### Most Valuable Checklist Item
- Checking whether edge cases are handled correctly was the most valuable item because it helped identify division by zero and single-student issues in the percentile function.

### New Checklist Item to Add
- [ ] Are boundary conditions and special cases tested, including empty collections, single items, and duplicate values?
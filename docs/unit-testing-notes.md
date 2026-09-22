# Unit Testing Notes

## Task 5 — Pytest Output

### 1. Verbose Test Run

Command:

```bash
python -m pytest -v tests/
```

Result:

```text
54 passed
```

The `-v` option means **verbose**. It displays detailed information about each individual test, including the test file, test name, and whether the test passed or failed.

**When to use:** Use `-v` when you want to clearly see which tests are being executed and their individual results.

---

### 2. Short Traceback Test Run

Command:

```bash
python -m pytest --tb=short
```

Result:

```text
54 passed
```

The `--tb=short` option displays a shorter traceback when a test fails. It provides useful error information without showing the full lengthy traceback.

**When to use:** Use `--tb=short` when debugging test failures and you want concise error information.

---

## Fixture Scope

The test suite uses different pytest fixture scopes.

### Function Scope

The `make_student` fixture uses the default **function scope**.

It runs separately for every test that uses it, providing fresh and independent test data.

This helps prevent one test from affecting another test.

### Module Scope

The `sample_scores` fixture uses **module scope**.

It is created once for the test module and can be shared by all tests in that module.

Module scope is useful when setup is expensive and the data can safely be shared.

---

## Final Test Result

The complete test suite passed successfully:

**54 tests passed.**

The test suite includes fixtures, class-average testing, mocked file I/O, parametrized edge-case testing, and existing unit and boundary-value tests.

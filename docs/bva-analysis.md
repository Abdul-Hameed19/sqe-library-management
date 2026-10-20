# Boundary Value Analysis — Lab 6

## Task 1 — Boundary Analysis for letter_grade()

The valid score range is 0–100.

The grade cut-offs are:

* 60 → D
* 70 → C
* 80 → B
* 90 → A

| Boundary      | Value - 1 | Expected   | Boundary Value | Expected | Value + 1 | Expected   |
| ------------- | --------: | ---------- | -------------: | -------- | --------: | ---------- |
| Minimum score |        -1 | ValueError |              0 | F        |         1 | F          |
| D/F cut-off   |        59 | F          |             60 | D        |        61 | D          |
| C/D cut-off   |        69 | D          |             70 | C        |        71 | C          |
| B/C cut-off   |        79 | C          |             80 | B        |        81 | B          |
| A/B cut-off   |        89 | B          |             90 | A        |        91 | A          |
| Maximum score |        99 | A          |            100 | A        |       101 | ValueError |

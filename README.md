# CCR Insight Reporter

## Project Status
🚧 **This script is still in progress and not yet functional.**

## Purpose
Calculates College & Career Readiness (CCR) data according to Missouri's MSIP 6 guidelines from various separate reports. The general report framework has been internally named **"Starship"**.

## Background
The original data process was conducted using a manually maintained Excel spreadsheet that consolidated student performance metrics across multiple assessments. This script is being developed to replace and improve that system.

---

## Overview of Starship

The spreadsheet represents a comprehensive analysis of student performance across multiple assessments. Each student has a unique identifier (Student ID) used to pull data from several sources, including:

- ACT
- ASVAB
- WorkKeys
- AP
- Dual Credit (DC)
- IRC
- PLTW Exam

The final output sheet, **"MSIP 5"**, combines scores and grades from these sources.

### Key Calculated Columns

- **CCR 1–3 Total**: Maximum weighted value from ACT, ASVAB, and WorkKeys.
- **CCR 4 Total**: Maximum weighted value from Semester 1 & 2 AP/DC Grades, AP Exam, IRC, and PLTW Exam.

---

## Weighting and Logic

### CCR 1–3 Weighting

- **ACT**:
  - <18 → 0.25
  - 18–21 → 0.75
  - 22–25 → 1.0
  - ≥26 → 1.25

- **ASVAB**:
  - <30 → 0.25
  - 30–62 → 0.75
  - 63–87 → 1.0
  - ≥88 → 1.25

- **WorkKeys**:
  - <4 → 0.25
  - 4 → 0.75
  - 5 → 1.0
  - ≥6 → 1.25

### CCR 4 Weighting

- **AP/DC Grades**:
  - Grades A+ to B- → 1.0
  - All others → 0

- **AP Exam**:
  - Score ≥ 3 → 1.25
  - <3 → 0

- **IRC Exam**:
  - "P" → 1.0
  - Else → 0

- **PLTW Exam**:
  - Score ≥ 6 → 1.0
  - Else → 0

---

## Logic Rules

- **CCR 1–3 Total**: max(ACT weight, ASVAB weight, WorkKeys weight)
- **CCR 4 Total**: max of all CCR 4 contributors (AP/DC/IRC/PLTW)

---

## Limitations of Excel

- Only pulls the **first** matching record per student; doesn't return highest score
- Often restricted to a single year of data
- Difficult to track held-back students or long-term performance
- Not scalable for multi-year aggregation

---

## Planned Script Setup

### File Organization

Files saved in `/dataSources/` (same directory as script):

- **ACT**: ACT_CY.csv, ACT_PY1.csv through ACT_PY4.csv
- **ASVAB**: ASVAB_PY1.csv through ASVAB_PY4.csv
- **WorkKeys**: workkeys_PY1.csv through workkeys_PY4.csv
- **IRC**: IRC.csv
- **AP**: Various files per school and year (e.g., AP_School1_PY1.csv)

### Output

- `Starship_<date>.xlsx` containing:
  - CCR 1–3 Total
  - CCR 4 Total
  - Raw scores and weighted components
  - Student, school, and grade info

### Final Pivot Table (Goals)

- Count of students
- Sum of CCR 1–3 and CCR 4 totals
- Grouped by:
  - Reporting school
  - Attending school
  - Grade level (with dropdown/filtering)

---

## Full AP Report Columns

*(Included for future mapping logic)*

```
[Full AP column header dump goes here — omitted for brevity, but will be retained in original file.]
```

---

## Notes

- The highest semester average across multiple years will be used for S1/S2 AP and DC grade logic.
- Future adjustments may be needed as actual report formats evolve.

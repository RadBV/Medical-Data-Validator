# 🏥 Medical Data Validator

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-2ea44f?style=flat)
![Type](https://img.shields.io/badge/Type-Data%20Validation-orange?style=flat)

A Python program that validates medical data to ensure it complies with a set of rules

---

## Overview

This data validator ensures that all medical records contain valid formatting, data types and all its required fields. Built to practice concepts like error handling, regular expressions, and working with dictionaries and lists in Python.

## 💡 What I Learned

- **Regular expressions** — My first hands-on use of Python's `re` module. Used `re.fullmatch()` with the `re.IGNORECASE` flag to validate ID formats like `P1001` and `V2301` against regex expressions (`'p\d+` and `v\d+` respectively).
- **`isinstance()`** — Used for checking data types across all fields and their values, validating whether they were ints, strings, lists, etc.
- **Dictionary unpacking (`**`)** — Passed a dictionary's values as arguments to a function using the double asterisk operator (`findInvalidRecords(**dictionary)`) keeping the code clean and readable.
- **List comprehension** — Used to filter invalid fields (checking if any value of the items in `constraints` is `False`) and to build the final invalid fields list all in one line.
- **Single-responsibility functions** — Split validation into two focused functions (`validate` and `findInvalidRecords`) so each does one job and delegates the rest.

## Features

- Validates the structure of an entire dataset (must be a `list` or `tuple`)
- Confirms each record within the dataset is a `dict` with exactly the required keys
- Enforces strict field rules for all six patient attributes
- Reports *every* violation across *every* record, not just the first one found
- Uses regex to validate ID formats (`P####` / `V####`), case-insensitive


## 📋 Validation Rules

| Field | Rule |
|---|---|
| `patientID` | String matching pattern `P` + digits (e.g. `P1001`) |
| `age` | Integer, must be 18 or older |
| `gender` | String, `"male"` or `"female"` (case-insensitive) |
| `diagnosis` | String or `None` |
| `medications` | List of strings |
| `lastVisitID` | String matching pattern `V` + digits (e.g. `V2301`) |

## ⚙️ How it Works

Validation has two layers:

**1. The dataset structure is checked:** `validate(data)` confirms that the entire dataset is a sequence (either `list` or `tuple`), and that each element is a dictionary (patient record) containing all six required keys.

**2. All fields are checked:** For each patient record that passes the structure check, `findInvalidRecords(...)` is called to test all six fields against the field rules above.

If any validation fails, an error message for that failure will print. If all checks pass, a confirmation for valid format will print.

```python
# Example: a record with an invalid age and a non-string medication
record = {
    'patientID': 'P1002',
    'age': -2,                          # ❌ below minimum age of 18
    'gender': 'male',
    'diagnosis': 'Type 2 Diabetes',
    'medications': ['Metformin', 45],   # ❌ 45 is not a string
    'lastVisitID': 'V2302',
}

# Output:
# Unexpected format 'age: -2' at position 0.
# Unexpected format 'medications: ['Metformin', 45]' at position 0.
```

# Tech Used

- **Python 3** — core language
- **`re` (regex)** — Validating format for IDs


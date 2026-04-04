# 🏥 Medical Data Validator

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-2ea44f?style=flat)
![Type](https://img.shields.io/badge/Type-Data%20Validation-orange?style=flat)

A Python program that validates medical data to ensure it complies with a set of rules

---

## Overview

This data validator ensures that all medical records contain valid formatting, data types and all its required fields. Built to practice concepts like error handling, regular expressions, and working with dictionaries and lists in Python.

---

## What I Learned

- **Regular expressions** — My first hands-on use of Python's `re` module. Used `re.fullmatch()` with the `re.IGNORECASE` flag to validate ID formats like `P1001` and `V2301` against regex expressions (`'p\d+` and `v\d+` respectively).
- **`isinstance()`** — Used for checking data types across all fields and their values, validating whether they were ints, strings, lists, etc.
- **Dictionary unpacking (`**`)** — Passed a dictionary's values as arguments to a function using the double asterisk operator (`findInvalidRecords(**dictionary)`) keeping the code clean and readable.
- **List comprehension** — Used to filter invalid fields (e.g. checking that every item in `medications` is a string) and to build the final invalid fields list all in one line.
- **Single-responsibility functions** — Split validation into two focused functions (`validate` and `findInvalidRecords`) so each does one job and delegates the rest.

---

## Features

Wip

---

## Validation Rules

Wip

---

## How it Works

Wip

---

## Usage

Wip

---

# Tech Used

- **Python 3** — core language
- **`re` (regex)** — Validating format for IDs


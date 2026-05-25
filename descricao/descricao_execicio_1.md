# Final Project — Sprint 1

## Python Fundamentals — Mandatory Text Processing Script

---

## 1. Project Overview

Using only the Python fundamentals learned in Sprint 1, you will build a single, self-contained text-processing tool capable of:

- Extracting patterns using regex
- Validating input formats
- Cleaning text
- Organizing code into functions and classes
- Handling errors
- Working with files

---

## 2. Mandatory Functional Requirements

### (1) Email Extraction Function

Create a function that:

- Receives a text string
- Finds all valid email addresses

An email is considered valid only if it contains:

- An `@` symbol
- A domain ending in:
  - `.com`
  - `.org`
  - `.net`
  - `.br`

The function must return:

- A list of email strings

---

### (2) ID Validation Function

Create a function that:

- Receives a list of employee IDs
- Validates IDs matching the exact pattern:

```text
AAA-1234
```

Where:

- `AAA` = exactly 3 uppercase letters
- `1234` = exactly 4 digits

The function must return:

- A list of valid IDs
- A list of invalid IDs

---

### (3) TextCleaner Class

Create a class named `TextCleaner` with:

#### Attributes

- `original_text`

#### Methods

- `remove_extra_spaces()`
- `remove_special_characters()`
  - Keep only:
    - letters
    - numbers
    - spaces
    - dots (`.`)
    - commas (`,`)

- `to_lowercase()`

The class must return the cleaned text.

---

### (4) File Reader With Error Handling

Create a function that:

- Attempts to read a `.txt` file from disk
- Uses `try/except` to handle errors such as:
  - File not found
  - Invalid encoding

The function must:

- Return the file content as a string
- Return an error message instead of crashing

---

### (5) Word Frequency Counter

Create a function that:

- Receives a text string
- Counts how many times each word appears
- Returns a dictionary:

```python
{word: count}
```

Requirements:

- Ignore case (case-insensitive)
- Ignore punctuation

---

## 3. How Everything Connects

You must provide a short script/notebook that:

1. Reads a sample file using the File Reader
2. Cleans the text using `TextCleaner`
3. Extracts emails from the cleaned text
4. Validates employee IDs from the cleaned text
5. Computes word frequency
6. Prints outputs in a clear, readable format

---

## 4. Deliverables

A Python script or Jupyter notebook implementing all mandatory components.

The code must be:

- Clean and modular
- Commented
- Using only Python fundamentals from Sprint 1

---

## 5. Example Input

Sample text (they can copy/paste or load from file):

```text
Hello team,

Please contact maria.silva@example.com or HR at hr@company.com.br.

Employee IDs pending validation:
ABC-1234, AB1-2345, XYZ-9999.

Thank you!
```

---

## 6. Expected Output (High-Level)

The program should display:

- Extracted emails
- Valid vs invalid IDs
- Cleaned text version
- Word frequency summary
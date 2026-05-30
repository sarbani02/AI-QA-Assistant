# AI Prompt Engineering Documentation

This document explains how prompts were crafted for Groq LLaMA to generate professional QA artifacts.

## Why Prompt Engineering Matters
A bad prompt gives generic output.
A good prompt gives professional, industry-ready output.

---

## 1. Test Case Generation Prompt

### Basic prompt (bad):
Generate test cases for login page

### Engineered prompt (used in this project):
Act as a senior QA analyst with 10 years experience.
Generate 10 professional test cases for {module} page 
with these fields: {fields}

Format each test case as:
TC ID | Title | Steps | Expected Result | Priority | Severity

Include positive, negative and boundary test cases.
Make it professional and ready for corporate use.

### Why this works:
- "Act as senior QA analyst" — gives AI a role, improves quality
- "10 years experience" — sets expertise level
- Specific format requested — ensures consistent structured output
- "positive, negative and boundary" — ensures complete test coverage
- "corporate use" — sets professional quality standard

---

## 2. Bug Report Generation Prompt

### Engineered prompt:
Act as a senior QA analyst.
Write a professional bug report for this issue in {module} module:
{description}

Include: Bug ID, Title, Module, Severity, Priority,
Steps to Reproduce, Expected Result, Actual Result,
Environment details.
Make it ready to log in Jira.

### Why this works:
- Specifies exact fields required in corporate bug reports
- "Ready to log in Jira" — sets industry standard output
- Module context improves accuracy of the report

---

## 3. Test Data Generation Prompt

### Engineered prompt:
Act as a senior QA analyst.
Generate 10 sets of test data for {field_type} field.
Include 5 valid and 5 invalid data sets.
Include boundary values and special characters.
Format as a clear table.

### Why this works:
- Specifies exact ratio of valid vs invalid data
- Requests boundary values — shows QA knowledge
- Table format makes output immediately usable

---

## Key Prompt Engineering Techniques Used

| Technique | Example | Result |
|-----------|---------|--------|
| Role assignment | "Act as senior QA analyst" | Higher quality output |
| Experience level | "10 years experience" | Professional tone |
| Output format | "TC ID, Title, Steps..." | Consistent structure |
| Industry context | "Ready for Jira" | Corporate standard |
| Coverage requirement | "positive, negative, boundary" | Complete test coverage |

---

## Performance Results
- Test cases generated in ~2 seconds
- 90%+ relevance to input module
- Output directly usable without editing
- Consistent format across all generations
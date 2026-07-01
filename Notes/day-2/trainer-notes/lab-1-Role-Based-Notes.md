# Lab 1 — Trainer Guide
## Role-Based Prompting + Summarizing Bug Reports and Requirement Documents

## 🎯 Lab Objectives

By the end of this lab, students will be able to:
1. Understand what Role-Based Prompting is and why it matters
2. Write effective role-based prompts for testing scenarios
3. Use AI to summarize bug reports clearly and accurately
4. Use AI to extract key information from requirement documents

---

## 🧠 Section 1 — What is Role-Based Prompting?

When you talk to an AI, it does not automatically know **who you are** or **what context you are in**.

By default, the AI tries to be a general assistant. But when you give it a **role**, it adjusts its tone, depth, and focus to match that role.

Think of it like this:

> If you ask a doctor "what should I eat?", you get a health-focused answer.  
> If you ask a chef the same question, you get a recipe-focused answer.  
> Same question — very different answers — because of the **role**.

This is exactly what Role-Based Prompting does. You tell the AI **who to be** before asking your question.

---

### The Basic Structure of a Role-Based Prompt

```
You are a [ROLE].
Your job is to [TASK].
Here is the input: [INPUT]
Give me [EXPECTED OUTPUT FORMAT].
```

---

### Why Does This Matter in Testing?

As a tester or QA engineer, you deal with:
- Bug reports that are messy or incomplete
- Requirement documents that are long and hard to read
- Test cases that need to be written quickly

Role-based prompting helps the AI **think like a QA engineer** — not like a generic assistant.

---

## 🛠️ Section 2 — Demo: Role-Based Prompting

### Demo 1A — Without a Role (Show the Difference First)

**Prompt to run (no role):**
```
Summarize this bug report:

Title: Login button not working on mobile
Description: When I tap the login button on my iPhone, nothing happens. 
I tried multiple times. The page does not load. 
Sometimes I see a spinner for 2 seconds and then it disappears.
Environment: iOS 16, Safari browser, App version 3.2.1
Reported by: QA Team
```

> **What to point out:** The AI gives a general summary. It may not highlight severity, steps to reproduce, or what a tester needs to act on.

---

### Demo 1B — With a Role (Show the Improvement)

**Prompt to run (with role):**
```
You are a senior QA engineer reviewing bug reports for a mobile application.
Your job is to summarize the bug report below in a structured format that 
helps the development team understand and fix the issue quickly.

Include the following in your summary:
- Bug Title
- Severity (Critical / High / Medium / Low)
- Affected Environment
- Steps to Reproduce (infer if not clearly stated)
- Expected Behavior
- Actual Behavior
- Suggested Priority

Bug Report:
Title: Login button not working on mobile
Description: When I tap the login button on my iPhone, nothing happens. 
I tried multiple times. The page does not load. 
Sometimes I see a spinner for 2 seconds and then it disappears.
Environment: iOS 16, Safari browser, App version 3.2.1
Reported by: QA Team
```

> **What to point out:** The AI now structures the output like a real QA document. It infers missing details. It is immediately useful.

---

### Demo 2 — Summarizing a Requirement Document

**Prompt to run:**
```
You are a QA analyst working on a software testing project.
Your job is to read the following requirement document and extract:
1. A short summary of what the feature does (2-3 sentences)
2. A list of all testable conditions (what can pass or fail)
3. Any ambiguous or unclear requirements that need clarification

Requirement Document:
Feature: User Registration

Users should be able to register on the platform using their email address 
and a password. The password must be at least 8 characters long. 
After registration, users should receive a confirmation email. 
The system should not allow duplicate email addresses. 
Users under 18 years of age should not be allowed to register.
```

> **What to point out:**
> - The AI extracts testable conditions automatically
> - It flags ambiguous requirements (e.g., "how is age verified?")
> - This saves hours of manual reading and analysis

---
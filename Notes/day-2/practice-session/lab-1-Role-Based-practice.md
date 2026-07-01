# Lab 1 — Student Practice Sheet
## Role-Based Prompting + Summarizing Bug Reports and Requirement Documents

## 📌 What You Will Practice

In this session, you will write role-based prompts to:
1. Summarize a bug report in a structured format
2. Analyze a requirement document and extract testable conditions

These are **different examples** from what your trainer demonstrated — so you get fresh practice!

---

## ✅ Before You Start

- Open **claude.ai** or **chatgpt.com** in your browser
- Log in to your account
- Start a **new conversation** for each exercise
- Read the full exercise before writing your prompt

---

## 🧪 Exercise 1 — Summarize a Bug Report

### Your Task

Below is a messy bug report submitted by a developer. Your job is to write a **role-based prompt** that instructs the AI to summarize it in a clean, structured format useful for the QA team.

### The Bug Report (paste this into your prompt)

```
hey team, so i was testing the checkout page and when i added 3 items to cart 
and tried to apply a discount code "SAVE20" it just showed an error that said 
"something went wrong". i tried again and same thing. but when i only had 1 item 
in the cart the code worked fine. this is on chrome, windows 11, version 4.5.0 
of the app. pretty sure its a backend issue. happened around 2pm today.
```

### Instructions

1. Write a role-based prompt that tells the AI who it is and what to do
2. Ask the AI to produce a structured summary with these sections:
   - Bug Title
   - Severity
   - Environment
   - Steps to Reproduce
   - Expected vs Actual Behavior
   - Suggested Priority
3. Paste your prompt + the bug report into Claude or ChatGPT
4. Review the output — does it look like something a QA team can act on?

### 💡 Hint — Starter Structure

```
You are a __________.
Your job is to __________.
Summarize the bug report below using this format:
- Bug Title:
- Severity:
- Environment:
- Steps to Reproduce:
- Expected Behavior:
- Actual Behavior:
- Suggested Priority:

Bug Report:
[paste the bug report here]
```

---

## 🧪 Exercise 2 — Analyze a Requirement Document

### Your Task

Below is a requirement document for a new feature. Write a **role-based prompt** that instructs the AI to extract testable conditions and flag any unclear requirements.

### The Requirement Document (paste this into your prompt)

```
Feature: Password Reset Flow

Registered users should be able to reset their password from the login page 
by clicking "Forgot Password". They will enter their registered email address 
and receive a reset link. The link should expire after some time. 
Users should not be able to reuse their old password. 
The new password must meet the platform's security standards. 
If the email is not registered, the system should handle it appropriately.
```

### Instructions

1. Write a role-based prompt that tells the AI it is a QA analyst
2. Ask the AI to extract:
   - A short feature summary (2–3 sentences)
   - All testable conditions (what can pass or fail)
   - A list of unclear or ambiguous requirements that need clarification
3. Paste your prompt + the requirement into Claude or ChatGPT
4. Look at the ambiguous items the AI flags — do you agree with them?

### 💡 Hint — Starter Structure

```
You are a __________.
Your job is to read the requirement document below and provide:
1. A short summary of the feature
2. A list of all testable conditions
3. A list of unclear or ambiguous requirements that need clarification

Requirement Document:
[paste the requirement here]
```

---

## 🧪 Exercise 3 (Bonus — If Time Permits) — Chain Your Prompts

### Your Task

After completing Exercise 2, **continue in the same chat window** and send this follow-up message:

```
Based on the testable conditions you identified, write 3 test cases in this format:

Test Case ID | Test Case Title | Steps | Expected Result | Pass/Fail
```

### What to Observe

- Did the AI remember the context from your previous message?
- Did it use the testable conditions it already found?
- How much time did this save compared to writing test cases manually?

---

## 📝 Reflection Questions

After completing the exercises, think about these:

1. What difference did adding a **role** make to the AI's output?
2. Which part of the output was most useful to you as a tester?
3. What would you change in your prompt to get an even better result?
4. Can you think of a real task in your current project where this would save you time?

---

## 🔑 Key Takeaways

- A **role** tells the AI who to be — this shapes the entire response
- A **structured output format** in your prompt = structured output from the AI
- You can **chain prompts** in the same conversation — the AI remembers context
- The better your prompt, the less editing you need to do on the output

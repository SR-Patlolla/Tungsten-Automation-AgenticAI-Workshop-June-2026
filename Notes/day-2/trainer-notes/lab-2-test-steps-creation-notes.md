# Lab 2 — Trainer Guide
## Automating the Creation of Manual Test Steps from Requirement PDFs

---

## 🎯 Lab Objectives

By the end of this lab, students will be able to:
1. Upload a requirement PDF to an AI tool and extract meaningful content from it
2. Write role-based prompts that generate structured manual test steps from requirements
3. Identify positive, negative, and edge case test scenarios from a requirement document

---

## 🧠 Section 1 — Concept: Why Automate Test Step Creation?

Writing manual test steps from a requirement document is one of the most time-consuming tasks for a QA engineer. A tester has to:
- Read and understand the full requirement
- Identify what needs to be tested
- Write each step clearly so anyone can follow it
- Cover positive flows, negative flows, and edge cases

This process can take hours — especially for large documents.

With AI, you can feed the requirement document directly and get a structured set of test steps in minutes. The AI reads the document, understands the acceptance criteria, and generates test steps — all you need is the right prompt.

---

## 🛠️ Section 2 — Demo: Generating Test Steps from a Requirement PDF

### The PDF Used for This Demo
**File:** `Web_E-commerce_User_Registration_Feature_Story.pdf`  
**Feature:** User Registration for an E-commerce Platform  
**Story ID:** ECOM-101

---

### Step 1 — Upload the PDF to the AI Tool

#### On Claude (claude.ai):
- Open a new conversation
- Click the **paperclip / attachment icon** at the bottom of the chat
- Upload the file: `Web_E-commerce_User_Registration_Feature_Story.pdf`
- Wait for Claude to confirm it has read the file

#### On ChatGPT:
- Open a new chat
- Click the **attachment icon** (paperclip)
- Upload the same PDF
- ChatGPT will process and confirm the file

> **Point to highlight:** The AI reads the entire PDF — you do not need to copy-paste any content. This is the power of document-aware prompting.

---

### Step 2 — Run the First Prompt: Understand the Feature

Before jumping to test steps, show students how to first ask the AI to summarize what it understood. This is a good habit — it confirms the AI read the document correctly.

**Prompt:**
```
You are a senior QA engineer.
I have uploaded a JIRA feature story document.
Read the document carefully and give me:
1. A short summary of the feature (3-4 sentences)
2. A list of all acceptance criteria in simple language
3. Any edge cases or special conditions mentioned in the document
```

> **What to point out:** The AI will accurately pull out the acceptance criteria and edge cases from the PDF. Ask students — "Did you have to read the full document yourself? No. The AI did it for you."

---

### Step 3 — Run the Second Prompt: Generate Manual Test Steps

**Prompt:**
```
You are a senior QA engineer creating a manual test plan.
Based on the uploaded requirement document, identify all scenarios that need 
to be tested and generate manual test steps for the User Registration feature.

Make sure to cover positive flows, negative flows, and edge cases based on 
what the document states.

For each test scenario, provide:
- Test Case ID (e.g., TC-001)
- Test Case Title
- Pre-conditions
- Test Steps (numbered)
- Expected Result
- Test Type (Positive / Negative / Edge Case)
```

> **What to point out:**
> - You did not tell the AI which scenarios to test — it figured them out by reading the document
> - It pulls the exact rules from the acceptance criteria (e.g., password must be 8 characters, email format validation, duplicate username handling)
> - This is the real power — the AI thinks like a QA engineer, not just a text formatter
> - Ask students: *"How long would it take you to read this document and come up with all these scenarios manually?"*

---

### Step 4 — Follow-Up Prompt: Export-Ready Format

Show students how to ask for the output in a table format — useful for pasting into Excel or a test management tool.

**Prompt:**
```
Now present the same test cases in a table format with these columns:
Test Case ID | Test Case Title | Pre-conditions | Steps | Expected Result | Test Type
```

> **What to point out:** The same content, now formatted as a table — ready to be copied into Jira, TestRail, or Excel. No reformatting needed.
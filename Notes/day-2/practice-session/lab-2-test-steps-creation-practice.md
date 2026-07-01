# Lab 2 — Student Practice Sheet
## Automating the Creation of Manual Test Steps from Requirement PDFs

---

## 📌 What You Will Practice

In this session, you will:
1. Upload a requirement PDF to an AI tool
2. Write prompts to extract and understand the feature requirements
3. Generate structured manual test steps covering positive, negative, and edge case scenarios

---

## ✅ Before You Start

- Open **claude.ai** or **chatgpt.com** and log in
- You will be given the file: **`Mobile_App_Push_Notification_Feature_Story_News_App.pdf`**
- Start a **new conversation**
- Upload the PDF using the attachment / paperclip icon before writing any prompt

---

## 🧪 Exercise 1 — Understand the Feature First

### Your Task

Before generating test steps, ask the AI to read and summarize the document. This confirms the AI understood the requirement correctly.

Write a role-based prompt that asks the AI to:
1. Give a short summary of the feature (3–4 sentences)
2. List all acceptance criteria in simple language
3. Identify any edge cases or special conditions mentioned

### 💡 Hint — Starter Structure

```
You are a __________.
I have uploaded a JIRA feature story document.
Read the document and give me:
1. ...
2. ...
3. ...
```

### ✅ Check Before Moving On

Read the AI's output and ask yourself:
- Did it correctly identify the feature?
- Did it list the acceptance criteria accurately?
- Did it catch the edge cases (e.g., conflicting DND periods, no topics selected)?

If something is missing or wrong, refine your prompt and try again.

---

## 🧪 Exercise 2 — Generate Manual Test Steps

### Your Task

Write a prompt that instructs the AI to **read the uploaded requirement document**, identify all scenarios that need to be tested, and generate manual test steps for the Push Notification feature.

Do **not** list the scenarios yourself — let the AI figure them out from the document.

Ask the AI to cover positive flows, negative flows, and edge cases on its own.

For each test case, ask the AI to provide:
- Test Case ID
- Test Case Title
- Pre-conditions
- Test Steps (numbered)
- Expected Result
- Test Type (Positive / Negative / Edge Case)


### ✅ What to Check in the Output

- Did the AI identify scenarios you would have thought of yourself?
- Did it catch the edge cases from the document (e.g., conflicting DND periods, notification retry on failure)?
- Did it miss anything important? If yes — that is a great discussion point!

---

## 🧪 Exercise 3 — Format as a Table

### Your Task

In the **same conversation**, send a follow-up prompt asking the AI to present the same test cases in a table format with these columns:

```
Test Case ID | Test Case Title | Pre-conditions | Steps | Expected Result | Test Type
```

### What to Observe

- Did the AI remember the test cases from the previous message?
- Is the table format clean and ready to copy into a spreadsheet or test management tool?

---

## 🧪 Exercise 4 — Bonus: Add a New Scenario

Still in the same conversation, ask the AI to add one more test case:

```
Add a test case for when the app receives a push notification while it is 
already open and in focus by the user.
```

### What to Observe

- Did the AI add it correctly based on the requirement document?
- Did it assign the right Test Case ID continuing from the previous list?

---

## 📝 Reflection Questions

1. How much time did it take to generate all test cases compared to writing them manually?
2. Did the AI miss any important scenario? What would you add?
3. How did the **summary step** (Exercise 1) help before jumping to test generation?
4. Would you trust this output directly, or would you review it first? Why?

---

## 🔑 Key Takeaways

- Always **verify AI understanding first** before asking it to generate test cases
- A well-structured prompt with clear output format = test cases ready to use
- **Follow-up prompts** in the same conversation let you refine and extend the output without starting over
- AI generates the first draft — **you are the expert** who reviews and improves it

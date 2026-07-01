# Lab 4 — Trainer Guide
## Custom GPTs & Claude Projects — Personalizing Agents to Follow Tungsten's Internal Standards

---

## 🎯 Lab Objectives

By the end of this lab, students will be able to:
1. Understand what Custom GPTs and Claude Projects are and why they are useful
2. Create 3 focused Custom GPTs in ChatGPT — one for each QA task
3. Create 3 equivalent Claude Projects as an alternative
4. Use each personalized agent to perform its specific task without writing any prompt from scratch

---

## 🧠 Section 1 — Concept: Why Custom GPTs and Claude Projects?

In Labs 1, 2, and 3, students wrote role-based prompts every single time they started a new task. Every new conversation meant starting from scratch — re-explaining the role, the format, the rules.

That is fine for learning. But in real work, it is inefficient.

**Custom GPTs and Claude Projects solve this problem.**

They let you write your instructions once — who the AI is, how it should behave, what format it should follow — and save it permanently. Every time you open that GPT or Project, the AI already knows all of this. You just give it the task.

Think of it like this:

> In Labs 1–3, every time you started a conversation, you were onboarding a new employee from scratch.  
> A Custom GPT or Claude Project is like a trained employee who already knows your standards, your format, and your expectations — every single time.

---

### Why 3 Separate GPTs — Not One?

You might think: *"Why not put everything into one GPT?"*

Here is why separate GPTs are better:

- Each GPT has **one focused job** — the instructions are shorter, cleaner, and more precise
- Less chance of the AI getting confused between tasks
- In a real team, different people use different tools at different times — a focused GPT fits naturally into that workflow
- Easier to maintain — if the bug report format changes, you update only that one GPT

---

## 🛠️ Section 2 — Demo Part A: Creating 3 Custom GPTs in ChatGPT

### How to Open the GPT Builder (Do This Once)

- Go to **chatgpt.com** and log in (requires ChatGPT Plus subscription)
- Click on your profile icon → **My GPTs**
- Click **Create a GPT**
- Use the **Configure** tab — it gives you full control
- Repeat this process for each of the 3 GPTs below

---

### GPT 1 — Bug Report Summarizer

**Name:**
```
Tungsten Bug Report Summarizer
```

**Description:**
```
Summarizes messy or incomplete bug reports into a clean, structured format 
ready for the development team to act on.
```

**Instructions:**
```
You are a senior QA engineer working for Tungsten Automation.

Your only job is to summarize bug reports.

When a user gives you a bug report — in any format, however messy or incomplete — 
summarize it using this exact structure:

- Bug Title
- Severity (Critical / High / Medium / Low)
- Affected Environment
- Steps to Reproduce (infer from the description if not explicitly stated)
- Expected Behavior
- Actual Behavior
- Suggested Priority

Always respond in this structured format. Do not add extra commentary.
If critical information is missing and cannot be inferred, flag it clearly 
at the bottom under "Missing Information".
```

**Test Prompt to Run Live:**
```
hey team, checkout button does nothing when i tap it on my phone. 
tried 3 times. android 13, chrome, app version 2.3.0. 
happens only when cart has more than 2 items.
```

> **What to point out:** No role. No format instruction. Just the raw bug report — and the GPT produces a clean, structured summary instantly.

---

### GPT 2 — Test Case Generator

**Name:**
```
Tungsten Test Case Generator
```

**Description:**
```
Reads requirement documents and automatically generates structured manual 
test cases covering positive, negative, and edge case scenarios.
```

**Instructions:**
```
You are a senior QA engineer working for Tungsten Automation.

Your only job is to generate manual test cases from requirement documents.

When a user uploads a requirement document or pastes requirement text:
- Read it carefully
- Identify all testable scenarios on your own — do not ask the user to list them
- Generate manual test cases covering positive flows, negative flows, and edge cases

For each test case provide:
- Test Case ID (e.g., TC-001)
- Test Case Title
- Pre-conditions
- Test Steps (numbered)
- Expected Result
- Test Type (Positive / Negative / Edge Case)

Base every test case strictly on what the document states.
Do not invent scenarios that are not supported by the requirement.
```

**Knowledge Files to Upload:**
- `Web_E-commerce_User_Registration_Feature_Story.pdf`
- `Mobile_App_Push_Notification_Feature_Story_News_App.pdf`
- `Api_Weather_Forecast_API_Feature_Story_Travel_App.pdf`

> **What to point out:** With the PDFs uploaded to the Knowledge section, students do not need to upload anything. They can simply say the feature name and the GPT already has the document.

**Test Prompt to Run Live:**
```
Generate test cases for the User Registration feature.
```

> **What to point out:** No document upload. No instructions. The GPT reads from its knowledge, identifies all scenarios, and generates structured test cases — exactly as practiced in Lab 2.

---

### GPT 3 — Prompt Optimizer

**Name:**
```
Tungsten Prompt Optimizer
```

**Description:**
```
Reviews weak or vague prompts, identifies what is missing, and rewrites them 
into precise, high-quality prompts for better AI output.
```

**Instructions:**
```
You are a prompt engineering expert working for Tungsten Automation.

Your only job is to improve prompts.

When a user gives you a prompt to improve:
1. Critique it — identify what is missing, vague, or unclear
2. Rewrite it into a stronger, more precise version
3. Briefly explain what you changed and why

Do not generate the actual output of the improved prompt unless the user 
explicitly asks you to. Your job is to improve the prompt, not execute it.

If the user asks you to run the improved prompt after reviewing it, do so.
```

**Test Prompt to Run Live:**
```
Improve this prompt: "Test the search feature"
```

> **What to point out:** The GPT critiques, rewrites, and explains — exactly as practiced in Lab 3. No setup needed from the student each time.

---

## 🛠️ Section 3 — Demo Part B: Creating 3 Claude Projects

### How to Open Claude Projects (Do This Once)

- Go to **claude.ai** and log in (requires Claude Pro subscription)
- On the left sidebar, click **Projects**
- Click **Create Project**
- Repeat for each of the 3 projects below

> **What to point out:** Claude Projects are simpler to set up than Custom GPTs — no builder UI, just a name and an instructions field. The concept and the instructions are identical.

---

### Project 1 — Bug Report Summarizer

**Name:** `Tungsten Bug Report Summarizer`

**Project Instructions:** Paste the exact same instructions from GPT 1 above.

---

### Project 2 — Test Case Generator

**Name:** `Tungsten Test Case Generator`

**Project Instructions:** Paste the exact same instructions from GPT 2 above.

**Upload Files:**
- Click **Add content** → **Upload files**
- Upload the same 3 PDFs

---

### Project 3 — Prompt Optimizer

**Name:** `Tungsten Prompt Optimizer`

**Project Instructions:** Paste the exact same instructions from GPT 3 above.

---

### Test All 3 Claude Projects

Run the same 3 test prompts used in the Custom GPT demo — one in each project.

> **What to point out:**
> - The output is comparable to the Custom GPTs
> - The instructions are identical — the tool is just the container
> - Claude Projects are slightly faster to set up — no multi-step builder
> - Both achieve the same goal — students use whichever subscription they have

---
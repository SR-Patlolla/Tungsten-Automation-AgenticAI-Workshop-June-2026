# Lab 4 — Student Practice Sheet
## Custom GPTs & Claude Projects — Personalizing Agents to Follow Tungsten's Internal Standards

---

## 📌 What You Will Practice

In this session, you will build 3 focused AI agents — one for each task you practiced in Labs 1, 2, and 3. Each agent will have its own instructions so you never have to write a prompt from scratch again.

---

## ✅ Before You Start

- Decide which tool you are using: **claude.ai** (Claude Pro) or **chatgpt.com** (ChatGPT Plus)
- Have the 3 requirement PDFs from Lab 2 ready to upload
- Follow the section that matches your tool

---

## 🧪 Exercise 1 — Build Your Bug Report Summarizer

### Your Task

Create a GPT or Claude Project that acts as a bug report summarizer.

**Name it:** `Tungsten Bug Report Summarizer`

Write the instructions yourself — do not copy from the trainer's demo. Based on what you practiced in Lab 1, think about:
- What role should the AI play?
- What input will it receive?
- What structured format should it always output?
- What should it do when information is missing?

### Test It

Once built, paste this bug report into your agent — with no extra instructions:

```
search bar on the homepage is broken. typed "shoes" and got no results. 
but when i searched "shoe" it worked. tried on firefox and safari both same issue. 
iphone 14, ios 17, app version 5.1.2. happened today morning.
```

### ✅ What to Check

- Did the agent produce a structured summary without you asking for a format?
- Did it infer the missing details (e.g., steps to reproduce)?
- Did it flag anything that was genuinely missing?

---

## 🧪 Exercise 2 — Build Your Test Case Generator

### Your Task

Create a GPT or Claude Project that reads requirement documents and generates test cases automatically.

**Name it:** `Tungsten Test Case Generator`

Write the instructions yourself. Think about:
- What role should the AI play?
- What should it do when given a requirement document?
- Should it ask the user for scenarios or figure them out itself?
- What format should each test case follow?

**Upload these files to the Knowledge / Files section:**
- `5a. Web_E-commerce_User_Registration_Feature_Story.pdf`
- `5b. Mobile_App_Push_Notification_Feature_Story_News_App.pdf`
- `5c. Api_Weather_Forecast_API_Feature_Story_Travel_App.pdf`

### Test It

Once built, send this message — nothing else:

```
Generate test cases for the Weather Forecast API feature.
```

### ✅ What to Check

- Did the agent find the right document from its knowledge without you uploading anything?
- Did it identify scenarios on its own without you listing them?
- Did it cover positive, negative, and edge cases?

---

## 🧪 Exercise 3 — Build Your Prompt Optimizer

### Your Task

Create a GPT or Claude Project that critiques and rewrites weak prompts.

**Name it:** `Tungsten Prompt Optimizer`

Write the instructions yourself. Think about:
- What role should the AI play?
- What should it do when given a weak prompt?
- Should it generate the final output immediately or wait for confirmation?
- What should its response always include?

### Test It

Once built, send this message — nothing else:

```
Improve this prompt: "Check if the API is working"
```

### ✅ What to Check

- Did the agent critique the prompt clearly?
- Did it rewrite it into a stronger version?
- Did it hold back from running the improved prompt until you asked?

---

## 🧪 Exercise 4 — Use All 3 Agents Together (Bonus)

### Your Task

Open all 3 agents you just built. Use them in sequence to simulate a real QA workflow:

**Step 1 — Use the Bug Report Summarizer:**
```
App crashes when uploading a profile picture larger than 5MB. 
Tested on android 12, app v3.0.1. happens every time.
```

**Step 2 — Use the Test Case Generator:**
```
Generate test cases for the Push Notification feature.
```

**Step 3 — Use the Prompt Optimizer:**
```
Improve this prompt: "Write a test plan for the mobile app"
```

### What to Observe

- Each agent stayed in its lane — it did only its specific job
- You gave minimal input each time — no role, no format, no instructions
- Three specialized agents, three different tasks, consistent output every time

---

## 📝 Reflection Questions

1. How different was the experience of using your agent compared to writing a fresh prompt every time?
2. Did your agent's instructions need any adjustment after you tested it? What did you change?
3. If you were setting this up for your entire QA team, what additional instructions would you add?
4. Can you think of a 4th agent that would be useful in your day-to-day testing work?

---

## 🔑 Key Takeaways

- A Custom GPT or Claude Project is a **reusable, specialized agent** — write the instructions once, use it forever
- Each agent should have **one focused job** — this makes it more reliable and easier to maintain
- The **instructions are the product** — the tool (ChatGPT or Claude) is just the container
- You have now built 3 specialized agents — in the upcoming modules, you will learn how agents like these can work together automatically as a team

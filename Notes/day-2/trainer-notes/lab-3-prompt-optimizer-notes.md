# Lab 3 — Trainer Guide
## Prompt Optimizer — Training the AI to Refine Its Own Prompts for More Accuracy

---

## 🎯 Lab Objectives

By the end of this lab, students will be able to:
1. Understand why prompt quality directly affects AI output quality
2. Recognize the difference between a weak prompt and a strong prompt
3. Use the AI itself to critique and rewrite a weak prompt
4. Apply the refined prompt and compare the output difference

---

## 🧠 Section 1 — Concept: What is a Prompt Optimizer?

Most people write a prompt, get a mediocre output, and assume the AI is not good enough. The real problem is almost always the prompt — not the AI.

A **Prompt Optimizer** is a technique where you ask the AI to:
1. Look at your weak prompt
2. Tell you what is wrong with it
3. Rewrite it into a better version
4. Then use that better version to generate the actual output

Think of it like this:

> You hand a junior tester a vague instruction: *"Test the login page."*  
> They don't know what to test, what format to use, or what counts as pass or fail.  
> But if you ask a senior tester to review that instruction and rewrite it — you get something precise and actionable.  
> That is exactly what we are doing here — the AI plays both roles.

This is powerful because:
- You do not need to be an expert prompt engineer to get expert-level output
- The AI knows what information it needs — you just have to ask it to tell you
- It creates a feedback loop that continuously improves your results

---

## 🛠️ Section 2 — Demo: AI Refining Its Own Prompt

### The Scenario

You are a QA engineer who needs to generate test cases for a login feature. You write a quick, vague prompt — the kind most beginners write. Then you ask the AI to fix it.

---

### Step 1 — Start With a Weak Prompt

Run this prompt first and show the output to students:

**Weak Prompt:**
```
Write test cases for a login page.
```

> **What to point out:** The output will be generic. It may cover basic happy path and a couple of negative cases — but it will not know:
> - What technology or platform this is for
> - What the acceptance criteria are
> - What format the test cases should be in
> - Whether to cover security, performance, or just functional scenarios
>
> The AI guessed everything. That is the problem.

---

### Step 2 — Ask the AI to Critique the Prompt

In the **same conversation**, send this:

**Optimizer Prompt:**
```
The prompt I just gave you was: "Write test cases for a login page."

As a prompt engineering expert, critique this prompt and tell me:
1. What is missing or unclear in this prompt?
2. What additional context would help you generate better and more accurate test cases?
3. Rewrite this prompt into an improved version that would give a much better output.

Do not generate the test cases yet — just give me the improved prompt.
```

> **What to point out:**
> - The AI will identify exactly what was missing — role, context, format, scope, platform, acceptance criteria
> - It will rewrite the prompt with all those elements included
> - This teaches students to think about **what the AI needs to know** before writing any prompt
> - Ask students: *"Did the AI identify gaps you would not have thought of yourself?"*

---

### Step 3 — Run the Improved Prompt

Take the rewritten prompt the AI produced and run it in a **new conversation**. Show the output side by side with the first one.

> **What to point out:**
> - The output is now structured, specific, and directly usable
> - It covers the right scenarios based on the context provided
> - The only thing that changed was the prompt — the AI model is exactly the same
> - This is the single most important lesson: **better prompt = better output, every time**

---

### Step 4 — Push It Further: Ask the AI to Optimize Again

Show students that this process can be repeated. After getting the improved output, send:

**Second Optimization Prompt:**
```
Review the prompt you just rewrote. Is there anything else that could make it 
even more precise or produce a more complete set of test cases?
If yes, give me a version 2 of the improved prompt.
```

> **What to point out:** The AI will often find one or two more things to improve — such as asking for boundary value analysis, specifying the number of test cases, or adding a requirement to flag ambiguous acceptance criteria. This shows that prompt optimization is an **iterative process**, not a one-time fix.
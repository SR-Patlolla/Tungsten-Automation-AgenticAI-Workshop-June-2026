# Lab 3 — Student Practice Sheet
## Prompt Optimizer — Training the AI to Refine Its Own Prompts for More Accuracy

---

## 📌 What You Will Practice

In this session, you will:
1. Write a weak prompt for a real QA task
2. Ask the AI to critique your prompt and rewrite it
3. Run the improved prompt and compare the difference
4. Push the AI to optimize the prompt a second time

---

## ✅ Before You Start

- Open **claude.ai** or **chatgpt.com** and log in
- Start a **new conversation**
- No file upload needed for this lab

---

## 🧪 Exercise 1 — Write a Weak Prompt and Run It

### Your Task

You are a QA engineer who needs to generate test cases for a **user profile update feature** in a mobile app.

Write the simplest, most basic prompt you can think of — the kind you would write if you were in a hurry. Run it and save the output.

**Example of a weak prompt (do not copy this — write your own version):**
```
Write test cases for a profile update feature.
```

### What to Note

- How many test cases did the AI generate?
- Did it cover negative and edge cases?
- Did it ask you for any missing information, or did it just guess?
- Is the output format something you could directly use in a test management tool?

---

## 🧪 Exercise 2 — Ask the AI to Critique and Rewrite Your Prompt (15 mins)

### Your Task

In the **same conversation**, send the following optimizer prompt. Replace `[your original prompt]` with the exact prompt you wrote in Exercise 1.

```
The prompt I just gave you was: "[your original prompt]"

As a prompt engineering expert, critique this prompt and tell me:
1. What is missing or unclear in this prompt?
2. What additional context would help you generate better and more accurate test cases?
3. Rewrite this prompt into an improved version that would give a much better output.

Do not generate the test cases yet — just give me the improved prompt.
```

### What to Note

- What gaps did the AI identify in your original prompt?
- Did it catch things you did not think about?
- Read the rewritten prompt carefully — does it look like something you could have written yourself?

---

## 🧪 Exercise 3 — Run the Improved Prompt

### Your Task

Open a **new conversation** and paste the improved prompt the AI gave you in Exercise 2. Run it and compare the output with what you got in Exercise 1.

### What to Compare

| | Weak Prompt Output | Improved Prompt Output |
|---|---|---|
| Number of test cases | | |
| Negative / edge cases covered | | |
| Output format | | |
| Usability (ready to use?) | | |

Fill in this table mentally or on paper — you will discuss it with the class.

---

## 🧪 Exercise 4 — Optimize Again

### Your Task

Go back to the conversation from Exercise 2 and send this follow-up:

```
Review the improved prompt you just wrote. Is there anything else that could 
make it even more precise or produce a more complete set of test cases?
If yes, give me a version 2 of the improved prompt.
```

### What to Observe

- Did the AI find more room for improvement?
- What did it add in version 2 that was not in version 1?
- At what point does the prompt feel complete enough to use?

---

## 📝 Reflection Questions

1. What was the biggest gap the AI identified in your original prompt?
2. How different was the output quality between the weak and improved prompt?
3. Would you use this optimizer technique in your daily work? For what kind of tasks?
4. Is there a limit to how many times you should optimize a prompt?

---

## 🔑 Key Takeaways

- A weak prompt gives generic output — not because the AI is limited, but because it had to guess
- The AI knows what information it needs — you just have to ask it to tell you
- Prompt optimization is an **iterative process** — each round makes the output more precise
- You do not need to be a prompt engineering expert — you just need to know how to ask the AI to fix your prompt

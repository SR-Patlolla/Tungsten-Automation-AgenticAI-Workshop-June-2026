# Core Prompt Techniques

---

# From Prompt Types to Prompt Techniques

| | Prompt Types | Core Prompt Techniques |
|---|---|---|
| **What it answers** | *How do I ask this?* | *How do I make the AI think, reason, and act correctly?* |
| **Scope** | One single prompt | Entire workflows, agent systems |
| **Who uses it** | Anyone using AI casually | AI engineers, agent builders, professionals |
| **Analogy** | Grammar of a sentence | Strategy of a book |
| **Output control** | Format, tone, structure | Reasoning quality, multi-step accuracy, behaviour |


**What We Covered already**
- Prompt *types* — the structure and purpose of how you ask
- Instructional, Contextual, Formatting, Open-Ended, Specific Example, Clarification, Comparative

**What We Cover Now:**
- Prompt *techniques* — industry-standard methods used by AI professionals, researchers, and engineers worldwide
- These techniques power everything from simple AI assistants to complex Agentic AI systems

> "Understanding these techniques will make you a more effective and confident AI practitioner — and prepare you for building Agentic AI systems."

---

# Zero-Shot Prompting

**What It Is:**
- Asking the AI to perform a task with **no examples or demonstrations**
- The AI relies entirely on its pre-trained knowledge to respond
- The most common form of prompting — most people use it without knowing it has a name

**Why It Works:**
- Modern AI models are trained on massive amounts of text data
- They already understand a wide range of tasks, concepts, and formats — without needing examples

**Example:**
> `Explain what regression testing is in simple terms.`

**Expected Output:** A clear, beginner-friendly explanation of regression testing — what it is, why it is done, and when it is used. No examples were needed to guide the AI.

**When to Use vs. When to Move On:**

| Situation | What to Do |
|---|---|
| Task is clear and straightforward | ✅ Zero-Shot is enough |
| Output is too generic or inaccurate | ➡️ Move to One-Shot or Few-Shot |
| Task involves complex multi-step reasoning | ➡️ Move to Chain-of-Thought |

> "Zero-shot is your starting point. If the output isn't good enough, that's your signal to move to a more guided technique."

---

# One-Shot Prompting

**What It Is:**
- Providing the AI with **exactly one example** before asking it to perform the same task on new input
- The single example acts as a template — showing the AI the format, tone, and structure you expect

**Why It Works:**
- One example is often enough to shift the AI from a generic response to one that matches your specific style or format
- Particularly useful when you have a consistent output pattern you want the AI to follow

**Example:**

```
I will give you a bug description and you will convert it into a structured bug report.

Example:
Bug Description: The search bar doesn't return results when special characters are entered.
 
Bug Report:
- Title: Search bar fails to return results for special character inputs
- Steps to Reproduce: 1. Navigate to the search bar. 2. Enter a special character such as "@" or "#". 3. Press Enter.
- Expected Result: Relevant search results are displayed.
- Actual Result: No results are returned and no error message is shown.
- Severity: Medium

Now convert this:
Bug Description: The checkout button becomes unresponsive after applying a discount code on the payment page.
```
**Expected Output:** A structured bug report following the exact same format — Title, Steps to Reproduce, Expected Result, Actual Result, and Severity — applied to the checkout button issue.

"One-shot prompting is powerful for standardising outputs. Show the AI one example of your team's format — it will follow it consistently."

---

# Few-Shot Prompting

**What It Is:**
- Providing the AI with **multiple examples** — typically 2 to 5 — before asking it to perform the task
- Each example reinforces the pattern, format, and style you expect
- Gives the AI a stronger signal to produce consistent and accurate outputs

**Why It Works:**
- Multiple examples reduce ambiguity — the AI identifies the pattern across all examples and applies it reliably to new inputs
- The more consistent your examples, the more consistent the output

**Example:**

```
Classify the following test cases as Functional, Performance, or Security.

Example 1: Verify that the login page accepts valid credentials and redirects to the dashboard. → **Functional**
Example 2: Verify that the application handles 10,000 simultaneous users with response time under 3 seconds. → **Performance**
Example 3: Verify that the API endpoint rejects requests without a valid authentication token. → **Security**

Now classify:
Verify that the password reset email is sent within 30 seconds of the request.
```
**Expected Output:** Performance — the AI follows the pattern from three examples and correctly identifies the timing-based test as performance-related.

**When to Use:**

| Use Few-Shot When... | Reason |
|---|---|
| Output must follow a strict format | Multiple examples reinforce the exact pattern |
| Zero-shot or one-shot gives inconsistent results | More examples reduce ambiguity |
| Classifying, categorising, or labelling data | Examples teach the AI your classification logic |

> "In Agentic AI, few-shot prompting is used to teach agents how to format outputs, make decisions, and follow workflows — all through examples rather than code."

---

# Chain-of-Thought (CoT) Prompting

**What It Is:**
- Instructing the AI to **think through a problem step by step** before arriving at a final answer
- Instead of jumping to a conclusion, the AI reasons out loud — breaking the problem into logical steps and working through each one sequentially

**Why It Works:**
- AI models perform significantly better on complex, multi-step problems when asked to reason through the steps first
- The reasoning process helps the AI catch errors and arrive at more accurate conclusions

## 🔑 Primary Trigger Phrases (Most Reliable)

| Trigger Phrase | What It Forces the AI to Do |
|---|---|
| `Think step by step.` | Breaks the problem into sequential reasoning steps |
| `Walk me through your reasoning.` | Makes the AI narrate its thought process out loud |
| `Explain your thought process before giving the final answer.` | Separates reasoning from conclusion |
| `Let's think through this carefully.` | Slows the AI down and encourages structured thinking |
| `Reason through this before answering.` | Prioritises logic over a quick response |

## 🔴 What Does NOT Trigger CoT

| Prompt Style | Why CoT is NOT Triggered |
|---|---|
| `Explain what regression testing is.` | Direct ask — AI jumps to answer without reasoning |
| `What is the capital of France?` | Factual lookup — no reasoning chain needed |
| `Summarise this paragraph.` | Instructional — output focused, not reasoning focused |
| `List 5 benefits of automation.` | List generation — no step-by-step logic required |

## ✅ Quick Formula to Trigger CoT

```
[Your Question] + [CoT Trigger Phrase]
```

**Side-by-Side Example:**

| Version | Prompt | Output Quality |
|---|---|---|
| ❌ Without CoT | `An automated test is passing locally but failing in the CI/CD pipeline. What is the cause?` | Generic list of possible causes — no structured reasoning |
| ✅ With CoT | `An automated test is passing locally but failing in the CI/CD pipeline. Think step by step through the possible causes, eliminate unlikely ones, and identify the most probable root cause with a recommended fix.` | Structured reasoning through environment differences, timing, dependencies — leading to a specific root cause and fix |

> "Chain-of-Thought is one of the most powerful techniques in Agentic AI. When an agent needs to plan, debug, or decide — CoT is what enables it to reason rather than just react."

## 📌 Rule of Thumb

> If the task involves **reasoning, diagnosis, planning, or multi-step logic** —
> always append a CoT trigger phrase.
> Without it, the AI will give you an answer. With it, the AI will give you *the right* answer.

---

# Role / Persona Prompting

**What It Is:**
- Assigning a specific **identity, expertise, or persona** to the AI before asking it to respond
- By telling the AI who it is, you shape the tone, depth, language, and perspective of its entire response

**Why It Works:**
- AI models are trained on content written by people with vastly different expertise levels and roles
- Assigning a role activates the knowledge, vocabulary, and communication style associated with that role

**Side-by-Side Example:**

| Version | Prompt |
|---|---|
| ❌ Without Role | `Review this test plan and identify any gaps. [paste test plan]` |
| ✅ With Role | `You are a senior QA architect with 15 years of experience in enterprise software testing. Your expertise includes test strategy, risk-based testing, and automation frameworks. Review the following test plan and identify gaps in coverage, unaddressed risks, and improvements to the overall testing strategy. [paste test plan]` |

**What Changes in the Output:**
- Without role: General review with surface-level observations
- With role: Expert-level review identifying specific coverage gaps, risk areas, and strategic recommendations — written in the authoritative tone of a senior QA professional

**When to Use:**

| Use Case | Role Prompt Example |
|---|---|
| Expert domain review | "You are a senior security engineer..." |
| Audience-appropriate communication | "You are a technical writer explaining to non-technical users..." |
| Building AI agents | "You are QA-Assist, a specialised QA support agent..." |

> "Every AI agent has a role prompt behind the scenes. It is what makes a support bot sound different from a coding assistant — even if they use the exact same underlying AI model."

---
# 🔁 The ReAct Loop — Reasoning + Acting

---

## The Loop — 4 Stages That Repeat

> Think of it like how **you** debug a problem at work. You don't know the answer upfront — you investigate, check, think again, check again, and stop when you find the fix.
> **ReAct makes the AI do exactly that.**

| Stage | Plain English |
|---|---|
| **Thought** | "What do I need to do next?" |
| **Action** | The AI does something — searches, checks a log, queries data |
| **Observation** | "Okay, here's what I found." |
| **Repeat** | Think again → Act again → Observe again |
| **Final Answer** | Loop stops when the task is done ✅ |

---

## Example — Regression Failure Analysis

**Task given to the AI:**
> *"Last night's regression run has failures. Find them and suggest fixes."*

---

💭 **Thought →** I need to pull last night's test report first.

⚡ **Action →** Fetch the test execution report.

👁️ **Observation →** 12 failures found — 8 in Payment, 4 in Login.

---

💭 **Thought →** Payment has more failures — investigate that first.

⚡ **Action →** Check the error logs for the 8 payment failures.

👁️ **Observation →** All 8 show a timeout error on the payment gateway API.

---

💭 **Thought →** Timeout on API call — could be an endpoint change in the latest deployment.

⚡ **Action →** Check if the payment API endpoint changed recently.

👁️ **Observation →** Yes — endpoint URL was updated but not reflected in the test environment.

---

✅ **Final Answer →**
- **Root Cause:** API endpoint mismatch between test environment and latest deployment
- **Fix:** Update test environment config → Re-run the 8 failed tests

---
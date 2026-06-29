# Context Windows

---

## Overview

The **context window** is the total amount of text LLM can "see" and work with at any one time. It is measured in tokens and covers everything — your instructions, the conversation history, any documents you attach, and LLM's own previous replies.

Understanding context windows is critical for:

- Designing long Agentic AI workflows
- Managing multi-turn conversations
- Deciding when to summarise or truncate history
- Avoiding failures caused by exceeding the limit

---

## What is a Context Window?

Think of the context window as LLM's **working memory** — like a whiteboard it can read from and write to during a task.

```
┌─────────────────────────────────────────────────────────┐
│                   CONTEXT WINDOW                        │
│                   (200,000 tokens)                      │
│                                                         │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐   │
│  │ System      │  │ Conversation │  │ LLM's         │   │
│  │ Prompt      │  │ History      │  │ Response      │   │
│  │ (your rules)│  │ (all turns)  │  │ (output)      │   │
│  └─────────────┘  └──────────────┘  └───────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```
---

## What Goes Inside the Context Window?

Every token in the context window counts against the limit. Here is what consumes space:

| Component | Token Consumption |
|---|---|
| System prompt | Fixed cost — same on every call |
| User messages (all turns) | Grows with every exchange |
| LLM's replies (all turns) | Grows with every exchange |
| Attached documents / files | Can be large — PDFs, logs, code |
| Tool results returned to LLM | Grows with each tool call in agentic loops |

### Why Conversation History is Expensive

LLM does not have persistent memory between API calls. Every time you send a new message, **you must re-send the entire conversation history** so LLM has context.

```
Turn 1:  Send [System] + [User msg 1]               → 50 tokens
Turn 2:  Send [System] + [User msg 1] + [LLM 1] + [User msg 2]  → 180 tokens
Turn 3:  Send [System] + [User msg 1] + [LLM 1] + [User msg 2] + [LLM 2] + [User msg 3]  → 420 tokens
...
Turn 20: The full history might be 5,000+ tokens — all re-sent every call
```

This is a key design consideration in Agentic AI systems.

---

## Checking Token Count Before Sending

Use the Token Counting API to verify your message fits before sending:

```python
token_check = client.messages.count_tokens(
    model="LLM-sonnet-4-6",
    system="You are a QA lead reviewing test results.",
    messages=[
        {"role": "user", "content": "Summarise these 50 test failures: [logs]"}
    ]
)

print(f"This request will use {token_check.input_tokens} input tokens")

if token_check.input_tokens > 190_000:
    print("Warning: approaching context limit — consider summarising history")
```
---

## Strategies for Managing Context in Agentic AI

Long-running agents are especially vulnerable to context window overflow. Here are the main strategies:

### Strategy 1: Sliding Window (Truncation)

Keep only the most recent N turns of conversation history.

```python
MAX_HISTORY_TURNS = 10

# Keep only the last 10 turns
if len(conversation_history) > MAX_HISTORY_TURNS * 2:
    conversation_history = conversation_history[-(MAX_HISTORY_TURNS * 2):]
```

**Risk:** LLM loses early context — may forget initial instructions or earlier findings.

---

### Strategy 2: Summarisation

When history grows large, ask LLM to summarise it, then replace the full history with the summary.

```python
summary_prompt = """
The following is a long conversation history. 
Summarise the key findings, decisions made, and current state in under 500 words.

[HISTORY]
{full_history}
"""

# Get summary, replace history with it
summary = call_LLM(summary_prompt)
conversation_history = [{"role": "assistant", "content": f"[Summary of prior work]: {summary}"}]
```

**Best for:** Multi-hour or multi-day agent runs.

---

### Strategy 3: External Memory

Store facts, findings, and intermediate results in an **external database** (vector DB or key-value store). Retrieve only what's relevant to the current step.

```
Agent detects test failure
    → Queries vector DB: "What do I know about this error type?"
    → Retrieves only the 3 most relevant past records
    → Includes only those in the context (not the full history)
```

**Best for:** Long-running Agentic AI systems with large knowledge bases.

---
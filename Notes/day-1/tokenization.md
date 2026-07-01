# Tokenization

---

## Overview

Before LLM reads your message or generates a response, it converts all text into **tokens**. Understanding tokenization helps you:

- Predict and control API costs
- Understand context window limits
- Write more efficient prompts
- Avoid hitting token limits mid-task

---

## What is a Token?

A token is the **smallest unit of text** that LLM processes. It is not the same as a word or a character — it sits somewhere in between.

### How Text Breaks Into Tokens

| Text | Approximate Tokens |
|---|--------------------|
| `Hello` | 1 token            |
| `Hello, world!` | 4 tokens           |
| `test` | 1 token            |
| `testing` | 1 tokens           |
| `testing123` | 2 tokens           |
| `Tokenization` | 2 tokens           |
| `supercalifragilisticexpialidocious` | 8–10 tokens        |

### General Rules of Thumb

- **1 token ≈ 4 characters** of English text
- **1 token ≈ ¾ of a word**
- **100 tokens ≈ 75 words**
- **1,000 tokens ≈ 750 words ≈ 1.5 pages of text**
- Code, symbols, and non-English text often use **more tokens per word**

---

## Why Does LLM Use Tokens Instead of Words?

Tokens allow LLM to handle:

- **Subwords** — `running` → `run` + `ning` (shares knowledge of `run`)
- **Punctuation** — `,` `.` `!` each become their own token
- **Prefixes/Suffixes** — `un` + `happy`, `re` + `start`
- **Multiple languages** — different scripts tokenise differently
- **Code** — keywords, operators, and identifiers tokenise specifically

This approach means LLM can generalise better across variations of the same concept.

---

## Input Tokens vs Output Tokens

Every LLM API interaction involves two types of tokens:

```
Your message (prompt) ──────────► INPUT TOKENS   → you are billed for these
LLM's reply  ────────────────► OUTPUT TOKENS  → you are billed for these
```

### What counts as input tokens?

- Your user message
- The system prompt (if you set one)
- The full conversation history (all previous turns)
- Any documents or files attached

---

## Tokenization: What You See in LLM.ai vs the API

| | LLM.ai (Web) | LLM API |
|---|---|---|
| Token visibility | Hidden — you don't see counts | Full visibility via `usage` field |
| Token counting tool | Not available | Token Counting API endpoint |
| Billing | Flat subscription (not per token) | Pay per token consumed |
| Context limit | 200K tokens (same model) | 200K tokens (same model) |
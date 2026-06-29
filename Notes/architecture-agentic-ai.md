# Architecture of Agentic AI

---

## Overview

The architecture of an Agentic AI system describes how all components — the AI model, memory, tools, agents, and humans — connect and work together.

A well-designed Agentic AI architecture has **six layers**, each with a distinct responsibility.

```
┌─────────────────────────────────────────────────────┐
│              Human-in-the-Loop Layer                │
├─────────────────────────────────────────────────────┤
│              Orchestration Layer                    │
├─────────────────────────────────────────────────────┤
│         Agent Layer  (Single or Multi-Agent)        │
├──────────────────────┬──────────────────────────────┤
│     Memory Layer     │     Tool & Action Layer      │
├──────────────────────┴──────────────────────────────┤
│                   LLM Core Layer                    │
└─────────────────────────────────────────────────────┘
```

---

## Layer 1: LLM Core

The LLM (Large Language Model) is the **brain** of every agent in the system. All reasoning, planning, and language understanding flows through it.

**What it does:**
- Understands the goal or instruction given to the agent
- Breaks the goal into a sequence of steps (planning)
- Generates final output or hands off to another agent

**Examples of LLMs used:**
- GPT-5o (OpenAI)
- Claude 4.6 Sonnet (Anthropic)
- Gemini 3.5 Pro (Google)

**Key point:** The LLM itself does not store memory, call tools, or take actions directly. The architecture wraps these capabilities around it.

---

## Layer 2: Memory Layer

Memory allows an agent to maintain context, learn from past interactions, and make informed decisions over time.

### 2.1 In-Context Memory (Short-Term)
- Everything in the current conversation or task session
- Lives inside the LLM's context window
- Lost when the session ends

### 2.2 External Memory (Long-Term)
- Stored outside the LLM in a database
- Persists across sessions and agent runs
- Retrieved using semantic search (vector databases)
- Tools: Pinecone, ChromaDB

### 2.3 Semantic Memory
- General knowledge and facts the agent has been given
- Includes domain knowledge, rules, and guidelines
- Example: "A test failure in the payment module is always high priority"

---

## Layer 3: Tool & Action Layer

This layer defines **what the agent can do** in the real world. Without tools, an agent can only generate text. With tools, it can interact with external systems and take real actions.

### Categories of Tools

**Read Tools** — gather information
- Search the web or internal docs
- Query a database
- Read a file or test log
- Call an API to fetch data

**Write / Execute Tools** — take action
- Create a Jira ticket
- Send a Slack message
- Run a test script
- Write or modify a file
- Trigger a CI/CD pipeline

---

## Layer 4: Agent Layer

This layer defines **how many agents** are involved and how they are structured.

### 4.1 Single-Agent Architecture

One agent handles the entire task end-to-end.

```
User Goal
   ↓
[Agent]
  ├── Reasons
  ├── Uses tools
  ├── Stores memory
  └── Delivers result
```

**Best for:** Focused, well-scoped tasks
**Example:** An agent that reads a test failure log and creates a Jira ticket

---

### 4.2 Multi-Agent Architecture

Multiple specialised agents work together, each with a defined role.

```
User Goal
   ↓
[Orchestrator Agent]
   ├── [Log Analyser Agent]   → reads and interprets test logs
   ├── [Classifier Agent]     → decides: flaky vs real bug
   ├── [Ticket Creator Agent] → raises Jira tickets
   └── [Reporter Agent]       → sends Slack summary
```

**Best for:** Complex, multi-step workflows that benefit from specialisation
**Example:** Full nightly regression triage pipeline

**Benefits of Multi-Agent:**
- Each agent is focused and easier to test and debug
- Agents can run in parallel, reducing total time
- Failure in one agent does not break the whole system
- Easier to scale by adding new specialist agents

---

## Layer 5: Orchestration Layer

Orchestration defines **how agents are coordinated** — the order they run in, how they communicate, and how decisions are made across agents.

### 5.1 Sequential (Pipeline)

Agents run one after another. Each agent's output is the next agent's input.

```
[Agent A] → [Agent B] → [Agent C] → Result
```

**Example:** Analyse log → Classify failure → Create ticket → Notify team

---

### 5.2 Parallel

Multiple agents run simultaneously and results are merged.

```
         ┌── [Agent A] ──┐
Goal ────┤── [Agent B] ──├──→ Aggregator → Result
         └── [Agent C] ──┘
```

**Example:** Three agents each analyse a different section of a large test suite at the same time

---

### 5.3 Hierarchical

A top-level orchestrator agent breaks down the goal and delegates sub-tasks to worker agents, then aggregates their results.

```
        [Orchestrator Agent]
         /        |        \
   [Worker A] [Worker B] [Worker C]
```

**Example:** A manager agent plans the regression strategy; worker agents execute specific test suites

---


## Layer 6: Human-in-the-Loop (HITL)

Agentic AI systems do not always operate fully autonomously. In many production systems, humans are deliberately placed at key decision points for oversight, safety, and accountability.

### Where Humans Plug In

**Before the agent acts (Approval Gate)**
- Agent proposes an action and waits for human approval before executing
- Example: "I am about to close 12 Jira tickets. Approve?"

**During execution (Monitoring)**
- A human watches the agent's progress in real time and can intervene
- Example: QA lead monitors the nightly triage agent via a dashboard

**After execution (Review)**
- Agent completes the task and a human reviews the output before it is finalised
- Example: Agent drafts a test report; QA manager reviews and publishes it

**On failure or uncertainty (Escalation)**
- Agent detects it cannot proceed with confidence and escalates to a human
- Example: "I cannot classify this failure — it does not match any known pattern. Please review."
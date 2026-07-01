# What is Agentic AI

---

## The Evolution of Testing

- **Manual QA:** Humans execute every test case and report bugs manually
- **Automation QA:** Scripts run tests but humans analyze failures and decide next steps
- **AI-Assisted QA:** AI suggests test cases or helps with analysis
- **Agentic AI QA:** AI autonomously plans, executes, learns, and takes actions

---

## AI vs Generative AI vs Agentic AI

Understanding these three terms is essential — they are related but represent very different levels of capability.

### Artificial Intelligence (AI)

AI is the broad field of building systems that can perform tasks that would normally require human intelligence.

- Encompasses rule-based systems, machine learning, and deep learning
- Trained on data to recognize patterns and make predictions
- Examples: spam filters, image recognition, fraud detection, recommendation engines
- **Key trait: Reactive** — responds to a specific input and produces a specific output; does not plan or act on its own

### Generative AI (Gen AI)

Generative AI is a subset of AI that can **create new content** — text, images, code, audio, or video — based on patterns learned from large datasets.

- Powered by Large Language Models (LLMs) such as GPT, Gemini, and Claude
- Works in a **prompt → response** model: you give it input, it generates output
- Examples: ChatGPT writing an email, GitHub Copilot suggesting code, DALL·E generating an image
- **Key trait: Generative but passive** — produces high-quality output but waits for the next prompt; it does not take actions in the real world or pursue goals independently

### Agentic AI

Agentic AI is a step beyond Generative AI. It uses an LLM as its reasoning core but wraps it with **autonomy, memory, tools, and the ability to take real-world actions** to pursue a goal over multiple steps — without needing a human prompt at every stage.

- Plans and executes workflows
- Uses tools: APIs, databases, browsers, ticketing systems

---

## Simple Comparison

**ChatGPT (Generative AI)**

- You ask: "Why did this test fail?"
- It responds: "Check the logs for network errors or timeout issues"
- Stops and waits for your next prompt

**Agentic AI**

- You set goal: "Ensure nightly regression is stable"
- It autonomously:
  - Runs the test suite
  - Detects 5 failures
  - Analyzes logs for each failure
  - Classifies 2 as flaky, 3 as genuine bugs
  - Reruns flaky tests to confirm
  - Creates Jira tickets for real bugs with full context
  - Sends summary report to team
  - Suggests preventive measures for future

---

## Anatomy of an Agentic AI System

**Four Core Components:**

**1. Reasoning Engine**

- Breaks down complex problems into steps
- Analyzes requirements, logs, and test results
- Makes logical decisions like a senior QA engineer
- Example: Determines if a failure is an environment issue vs. a code bug

**2. Memory System**

- Short-term: Current task context and conversation
- Long-term: Historical test results, known flaky tests, past bugs
- Remembers patterns across multiple test runs
- Example: Knows Test_Login has been flaky for 3 days on staging

**3. Tool Integration**

- APIs: REST endpoints, GraphQL queries
- Databases: MySQL, PostgreSQL, MongoDB
- Test Frameworks: Selenium, Playwright, Pytest
- Ticketing: Jira, Azure DevOps
- Communication: Slack, Email
- CI/CD: Jenkins, GitHub Actions

**4. Action Executor**

- Doesn't just suggest: Actually performs tasks
- Executes tests, queries databases, creates tickets
- Coordinates multiple tools in sequence
- Handles errors and retries intelligently

---
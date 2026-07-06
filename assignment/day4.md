# Day 4 — Implement 2 new agents

## Log Analyzer Agent

Implement an agent `log_analyzer_agent` that reads a system log file and produces a detailed technical analysis, a structured JSON summary, and a plain-language executive summary.

### Requirements

- Input: a log file from `data/logs/` (CLI: optional path as first argument; auto-pick if omitted).
- Output:
  - Text analysis report saved to `outputs/log_analyzer/<logfile>_analysis.txt`
  - JSON summary saved to `outputs/log_analyzer/<logfile>_analysis.json`
  - Executive summary saved to `outputs/log_analyzer/<logfile>_executive.txt`
- The LLM must be called once with a system prompt that instructs it to return all three sections in a single response.
- Parse the single response to split it into the three outputs using delimiters (`\`\`\`json` for JSON, `---EXECUTIVE---` for executive summary).

### System Prompt Requirements

The system prompt must instruct the LLM to act as a senior DevOps engineer and produce:

1. **Technical Analysis** (plain text) covering:
   - Summary of issues found
   - Critical errors with timestamps
   - Root cause analysis
   - Impact on systems/users
   - Step-by-step recommendations
   - Prevention strategies

2. **JSON block** (delimited by ` ```json `) with the following schema:

```json
{
  "summary": "Brief one-line summary",
  "error_count": 5,
  "critical_errors": [
    {"timestamp": "2026-01-04 10:24:12", "message": "Payment timeout", "severity": "high"}
  ],
  "root_causes": ["Cause 1", "Cause 2"],
  "affected_systems": ["payment", "database", "api"],
  "recommendations": ["Fix 1", "Fix 2"],
  "severity": "high"
}
```

3. **Executive Summary** (delimited by `---EXECUTIVE---`) in plain, non-technical language covering:
   - What happened
   - Business impact (users affected, downtime)
   - What is being done to fix it
   - When it will be resolved
   - Keep it to 3–5 sentences, no technical jargon

### Expected Output Files

| File | Description |
|---|---|
| `<logfile>_analysis.txt` | Full technical report (plain text) |
| `<logfile>_analysis.json` | Structured JSON summary |
| `<logfile>_executive.txt` | Non-technical executive summary |

## Constraints

- Make exactly **one LLM call** for all three outputs.
- Log LLM metadata: provider, model, token count, duration, and cost.
- Handle `json.JSONDecodeError` gracefully if JSON parsing fails.
- Use `pathlib.Path` for all file operations.
- Output directory must be created automatically if it does not exist.

---

## Edge / Negative Testcase Generator
Implement an agent `edgecase_agent` that reads a requirement text (single file) and produces a JSON array of test cases emphasizing edge and negative scenarios in addition to normal cases.

Requirements

- Input: a requirement text file from `data/requirements` (CLI: `--input PATH`).
- Output: a JSON array (printed or returned) and a CSV `outputs/testcase_generated/test_cases.csv`.
- Each test case object must include: `id`, `title`, `steps`, `expected`, `priority`, `tags`.
- At least 6 and at most 12 test cases. At least 30% must be tagged as `edge` or `negative`.

Expected output (JSON schema per case)

{
  "id": "TC-001",
  "title": "Short test title",
  "steps": ["step 1", "step 2"],
  "expected": "Expected result",
  "priority": "High|Medium|Low",
  "tags": ["edge"|"negative"|"happy"],
}

CSV columns: TestID, Title, Steps, Expected, Priority, Tags, Likelihood

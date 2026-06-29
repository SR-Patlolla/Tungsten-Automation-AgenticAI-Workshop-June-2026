# Temperature Settings

---

## Overview

**Temperature** is a parameter that controls how **creative or deterministic** LLM's responses are. It is one of the most important settings to understand when building Agentic AI systems because it directly affects the **reliability and variability** of LLM's output.

---

## What is Temperature?

Temperature controls the **randomness** in how LLM selects its next word (token) when generating a response.

### The Intuition

Imagine LLM is choosing the next word and has ranked all possible words by probability:

```
Next word candidates after "The test":
  "failed"   → 45% probability
  "passed"   → 30% probability
  "results"  → 15% probability
  "suite"    →  7% probability
  "was"      →  3% probability
```

- At **low temperature** → LLM almost always picks "failed" (the most likely word)
- At **high temperature** → LLM spreads its choices, sometimes picking "results" or "suite"

This happens at every single token in the response — so the effect compounds across an entire reply.

---

## The Temperature Scale

Temperature ranges from **0.0 to 1.0** in the LLM API.

```
0.0          0.3          0.5          0.7          1.0
 │────────────│────────────│────────────│────────────│
 │                                                   │
Deterministic                               Very Creative
(same answer                              (varied, surprising,
every time)                                  unpredictable)
```

| Temperature | Behaviour | Best For |
|---|---|---|
| `0.0` | Fully deterministic — same output every time | Classification, routing decisions |
| `0.1–0.3` | Very consistent with minor variation | Data extraction, structured output, bug analysis |
| `0.5` | Balanced — reliable but with some flexibility | General QA tasks, test case writing |
| `0.7–0.8` | Creative — varied responses | Brainstorming, test idea generation |
| `1.0` | Highly random — unpredictable | Experimental use only |

---
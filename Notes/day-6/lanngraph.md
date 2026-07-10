- Why LangGraph
    
    ## What We'll Cover
    
    Understanding Langchain limitations and why we need LangGraph for complex agent workflows
    
    ---
    
    ## What We've Built So Far
    
    ### Langchain Agents
    
    ```python
    # Our Langchain pattern
    chain = prompt_template | llm | parser
    result = chain.invoke({"input": data})
    
    ```
    
    **What we can do:**
    
    - ✅ Simple linear workflows
    - ✅ Automatic parsing
    - ✅ Clean component composition
    
    **What we cannot do:**
    
    - ❌ Conditional branching ("if good → save, if bad → retry")
    - ❌ State management across steps
    - ❌ Multi-step workflows with loops
    - ❌ Error recovery with fallbacks
    - ❌ Human-in-the-loop approvals
    
    ---
    
    ## Real-World Problem: TestCase Agent
    
    ### Current Langchain Implementation:
    
    ```python
    # agents_langchain/testcase_langchain.py
    
    chain = prompt_template | llm | parser
    testcases = chain.invoke({"requirement": requirement})
    
    # Save directly - no validation!
    save_to_csv(testcases)
    
    ```
    
    **Issues:**
    
    1. **No validation** - What if LLM returns bad JSON?
    2. **No retry** - What if generation fails?
    3. **No human approval** - Save directly without review
    4. **No recovery** - If save fails, everything fails
    
    ### What We Need:
    
    ```
    Read Requirement
        ↓
    Generate Test Cases
        ↓
    Validate Output ← [Conditional!]
        ↓ (if valid)
    Human Approval ← [Wait for human!]
        ↓ (if approved)
    Save Output
        ↓ (if invalid)
    Retry Generation ← [Loop back!]
    
    ```
    
    **This requires:**
    
    - Multiple nodes (steps)
    - Conditional routing (if/else)
    - State tracking (requirement, tests, retries)
    - Loops (retry logic)
    
    ---
    
    ## Visual: Langchain vs LangGraph
    
    ### Langchain (Linear):
    
    ```
    Input → [prompt | llm | parser] → Output
             (single chain)
    
    ```
    
    **Cannot do:**
    
    - Loops
    - Conditionals
    - Multi-step
    - State tracking
    
    ### LangGraph (Graph):
    
    ```
            ┌─────────────┐
       ┌───▶│  Generate   │
       │    └─────┬───────┘
       │          │
       │    ┌─────▼───────┐      ┌──────────┐
       │    │  Validate   │─────▶│   Save   │
       │    └─────┬───────┘ valid└──────────┘
       │          │
       └──────────┘ invalid (retry loop!)
    
    ```
    
    **Can do:**
    
    - ✅ Loops (retry)
    - ✅ Conditionals (if/else)
    - ✅ Multi-step (3+ nodes)
    - ✅ State tracking (shared data)
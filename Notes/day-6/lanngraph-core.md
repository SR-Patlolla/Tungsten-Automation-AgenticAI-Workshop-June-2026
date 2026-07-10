- LangGraph Core Concepts
    
    ## What We'll Cover
    
    Learn the 3 building blocks of LangGraph: State, Nodes, and Edges with simple examples
    
    ---
    
    ## The 3 Building Blocks
    
    LangGraph has only **3 core concepts**:
    
    1. **State** - Data shared between steps
    2. **Nodes** - Functions that do work
    3. **Edges** - Connections between nodes
    
    That's it! Let's learn each one.
    
    ---
    
    ## Concept 1: State (Shared Data)
    
    ### What is State?
    
    State is a **dictionary** that flows through your graph. All nodes can read and update it.
    
    ### Simple Example:
    
    ```python
    from typing import TypedDict
    
    class AgentState(TypedDict):
        count: int
        message: str
    
    ```
    
    **That's it!** A state is just a TypedDict defining what data you'll track.
    
    ---
    
    ## Concept 2: Nodes (Functions)
    
    ### What is a Node?
    
    A node is a **function** that:
    
    - Takes state as input
    - Does some work
    - Returns updated state
    
    ### Simple Example:
    
    ```python
    def increment(state: AgentState) -> AgentState:
        return {"count": state["count"] + 1}
    
    ```
    
    **That's it!** Read from state, do work, return update.
    
    ### Node Pattern:
    
    ```python
    def node_name(state: StateType) -> StateType:
        # 1. Read from state
        value = state["key"]
    
        # 2. Do work
        new_value = value + 1
    
        # 3. Return update
        return {"key": new_value}
    
    ```
    
    **Remember:** Return only what changed (LangGraph merges it automatically)!
    
    ---
    
    ## Concept 3: Edges (Connections)
    
    ### What is an Edge?
    
    An edge is a **connection** between nodes. It says "after Node A, go to Node B".
    
    ### Two Types:
    
    **1. Normal Edge (always goes there):**
    
    ```python
    graph.add_edge("node_a", "node_b")
    # Always: node_a → node_b
    
    ```
    
    **2. Conditional Edge (decides where to go):**
    
    ```python
    graph.add_conditional_edges(
        "node_a",
        decide_function,
        {"path1": "node_b", "path2": "node_c"}
    )
    # Dynamic: node_a → ? (depends on state)
    
    ```
    
    We'll learn conditional edges later. For now, focus on normal edges.
    
    ---
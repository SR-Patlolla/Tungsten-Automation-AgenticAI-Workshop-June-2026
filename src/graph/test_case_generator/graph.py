from langgraph.graph import StateGraph, END
from .state import TestCaseState
from .nodes import read_requirement, generate_tests, save_outputs

def build_graph():
    # Create a Graph
    workflow = StateGraph(TestCaseState)

    # Add nodes
    # Way 1
    workflow.add_node("read_requirement", read_requirement)
    # Way 2
    workflow.add_node("generate", generate_tests)
    workflow.add_node("save", save_outputs)

    # Connect nodes
    workflow.set_entry_point("read_requirement")
    workflow.add_edge("read_requirement", "generate")
    workflow.add_edge("generate", "save")
    workflow.add_edge("save", END)

    # Compile
    return workflow.compile()
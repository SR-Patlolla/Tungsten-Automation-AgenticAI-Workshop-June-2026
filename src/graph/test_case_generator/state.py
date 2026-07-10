from typing import TypedDict, List, Dict

class TestCaseState(TypedDict):
    """State for test case generation pipeline."""
    requirement: str
    test_cases: List[Dict]
    errors: List[str]
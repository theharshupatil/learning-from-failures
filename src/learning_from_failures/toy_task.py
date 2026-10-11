"""A tiny deterministic task for exercising the experiment loop."""
def check_answer(task: str, answer: str) -> bool:
    answers = {"two_plus_two": "4", "capital_of_france": "paris"}
    if task not in answers:
        raise KeyError(f"Unknown task: {task}")
    return answer.strip().lower() == answers[task]

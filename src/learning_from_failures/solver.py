from .experience import Experience, ExperienceStore
from .toy_task import check_answer

def baseline_attempt(task: str) -> str:
    # Intentionally tiny baseline; replace with a model adapter later.
    return {"two_plus_two": "4", "capital_of_france": "paris"}.get(task, "")

def memory_assisted_attempt(task: str, store: ExperienceStore) -> str:
    lessons = store.lessons_for(task)
    # This toy example uses the most recent recorded successful attempt.
    for item in reversed(store.all()):
        if item.task == task and item.success:
            return item.attempt
    return baseline_attempt(task)

def run_attempt(task: str, answer: str, store: ExperienceStore) -> bool:
    success = check_answer(task, answer)
    lesson = f"Use answer: {answer}" if success else "Reconsider the answer; previous attempt failed."
    store.add(Experience(task=task, attempt=answer, success=success, lesson=lesson))
    return success

from pathlib import Path
from tempfile import TemporaryDirectory
from .experience import ExperienceStore
from .solver import baseline_attempt, memory_assisted_attempt, run_attempt

def main():
    with TemporaryDirectory() as d:
        store = ExperienceStore(Path(d) / "experience.jsonl")
        task = "two_plus_two"
        answer = baseline_attempt(task)
        print(f"Baseline answer: {answer!r}")
        print(f"Success: {run_attempt(task, answer, store)}")
        print(f"Memory-assisted answer: {memory_assisted_attempt(task, store)!r}")
        print(f"Stored lessons: {store.lessons_for(task)}")

if __name__ == "__main__":
    main()

from learning_from_failures.experience import Experience, ExperienceStore
from learning_from_failures.solver import run_attempt

def test_store_round_trip(tmp_path):
    store = ExperienceStore(tmp_path / "experience.jsonl")
    store.add(Experience("t", "wrong", False, "try another route"))
    store.add(Experience("t", "right", True, "verified"))
    assert [x.attempt for x in store.all()] == ["wrong", "right"]
    assert store.lessons_for("t") == ["try another route", "verified"]

def test_attempt_is_recorded(tmp_path):
    store = ExperienceStore(tmp_path / "experience.jsonl")
    assert run_attempt("two_plus_two", "4", store)
    assert store.all()[0].success

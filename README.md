# Learning from Failures

A research sandbox for testing whether a system can improve by recording failed attempts, retrieving relevant experience, and changing its strategy on later attempts.

## First milestone

This repository starts with a deterministic toy task, an append-only JSONL experience store, and a simple memory-assisted solver. It is a **research baseline**, not yet an LLM agent.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
python -m learning_from_failures.demo
```

## Layout

- `src/learning_from_failures/experience.py`: save and retrieve prior attempts.
- `src/learning_from_failures/toy_task.py`: a deterministic test environment.
- `src/learning_from_failures/solver.py`: baseline and memory-assisted strategies.
- `tests/`: small behavioral tests.
- `experiments/`: place experiment configs and results here.

## Research questions

1. Does experience improve success rate over a no-memory baseline?
2. Does retrieval help on genuinely new task variants, or only repeat seen cases?
3. What happens when the memory contains misleading or obsolete experience?
4. Does improvement persist under a fixed token, time, or tool-call budget?

## Next milestones

- [ ] Add a model adapter (local model or API) behind a stable interface.
- [ ] Compare no-memory, nearest-neighbor retrieval, and curated lessons.
- [ ] Add held-out task families and confidence intervals.
- [ ] Track compute budget and report success per unit cost.

Do not claim that memory improves reasoning until controlled experiments demonstrate it.

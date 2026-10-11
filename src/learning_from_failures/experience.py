"""Minimal JSONL-backed store for prior attempts."""
from __future__ import annotations
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

@dataclass
class Experience:
    task: str
    attempt: str
    success: bool
    lesson: str = ""

class ExperienceStore:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def add(self, item: Experience) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(item)) + "\n")

    def all(self) -> list[Experience]:
        if not self.path.exists():
            return []
        items = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                items.append(Experience(**json.loads(line)))
        return items

    def lessons_for(self, task: str) -> list[str]:
        # Deliberately simple exact-match retrieval baseline.
        return [x.lesson for x in self.all() if x.task == task and x.lesson]

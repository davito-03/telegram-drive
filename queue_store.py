"""Disk queue for telegram-drive. JSON file; not a broker."""
from __future__ import annotations

import json
import os
from typing import Any

QUEUE_FILE = os.environ.get("QUEUE_FILE", "queue.json")


def load_queue() -> list[dict[str, Any]]:
    if os.path.exists(QUEUE_FILE):
        try:
            with open(QUEUE_FILE, encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
        except Exception:
            return []
    return []


def save_queue(queue: list[dict[str, Any]]) -> None:
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)


def add_to_queue(task_dict: dict[str, Any]) -> None:
    q = load_queue()
    q.append(task_dict)
    save_queue(q)


def remove_from_queue(task_id: str) -> None:
    q = [x for x in load_queue() if x.get("task_id") != task_id]
    save_queue(q)

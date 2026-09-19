import importlib


def test_queue_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setenv("QUEUE_FILE", str(tmp_path / "q.json"))
    import queue_store

    importlib.reload(queue_store)
    queue_store.save_queue([])
    queue_store.add_to_queue({"task_id": "a", "name": "x.mp4"})
    q = queue_store.load_queue()
    assert len(q) == 1
    assert q[0]["task_id"] == "a"
    queue_store.remove_from_queue("a")
    assert queue_store.load_queue() == []

# tests/test_memory.py

from memory.memory_store import MemoryStore

store = MemoryStore()
rows = store.fetch_all()

print("\n🧠 Memory Store Contents:")
for row in rows:
    print(row)

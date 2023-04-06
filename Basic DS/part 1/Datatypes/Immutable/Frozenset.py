ids = {101, 102, 103, 104}
ids.add(105)
print(ids)

f = frozenset(ids)
print(type(f))
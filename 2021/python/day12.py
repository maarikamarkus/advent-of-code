from collections import defaultdict

def find_paths(room, visited, twice, counter = 0):
  if room == 'end':
    return 1

  for r in maze[room]:
    if r.isupper():
      counter += find_paths(r, visited, twice)
    else:
      if r not in visited:
        counter += find_paths(r, visited | {r}, twice)
      elif twice and  r not in {'start', 'end'}:
        counter += find_paths(r, visited, False)

  return counter

input_data = []
with open('../data/day12-input.txt') as f:
  input_data = [line.strip().split('-') for line in f.readlines()]

maze = defaultdict(list)
for start, end in input_data:
  maze[start].append(end)
  maze[end].append(start)

print("Part I:", find_paths('start', {'start'}, False))
print("Part II:", find_paths('start', {'start'}, True))
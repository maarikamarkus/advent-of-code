from math import prod

def part1(input):
  low_pos = set()
  w = len(input[0])
  h = len(input)

  for i in range(h):
    for j in range(w):
      el = height_map[(i, j)]
      el_neighbours = [height_map[p] for p in neighbours(i, j)]

      add_to_low = True
      for n in el_neighbours:
        if n <= el:
          add_to_low = False
      if add_to_low:
        low_pos.add((i, j))

  result = sum([height_map[p] + 1 for p in low_pos])
  return result, low_pos


def part2(low_pos):
  basins = [count_basin(p) for p in low_pos]
  return prod(sorted(basins)[-3:])

def count_basin(p):
  if height_map[p] == 9:
    return 0
  del height_map[p]
  return 1 + sum(map(count_basin, neighbours(*p)))

def neighbours(x, y):
  return (filter(lambda p: p in height_map, [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]))


input_data = []
with open('../data/day9-input.txt') as f:
  input_data = [list(map(int, line.strip())) for line in f.readlines()]

height_map = {(j, i): input_data[j][i] for i in range(len(input_data[0])) for j in range(len(input_data))}

r, low_pos = part1(input_data)
print("Part I:", r) # 537
print("Part II:", part2(low_pos)) # 1142757

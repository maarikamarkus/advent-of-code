
def part1(data):
  octopuses = data.copy()

  flashes = 0
  for _ in range(100):
    flashes += count_flashes(octopuses)
    
  return flashes

def part2(data):
  octopuses = data.copy()

  step = 1
  while True:
    if count_flashes(octopuses) == 100:
      return step
    step += 1

def count_flashes(octopuses):
  flashes = 0
  ks = octopuses.keys()

  while ks:
    oct_neighbours = []

    for k in ks:
      if not 0 <= k[0] < 10 or not 0 <= k[1] < 10:
        continue
      
      octopuses[k] += 1
      if octopuses[k] == 10:
        oct_neighbours.extend(neighbours(*k))
      
    ks = oct_neighbours
  
  for k in octopuses.keys():
    if octopuses[k] >= 10:
      flashes += 1
      octopuses[k] = 0
  
  return flashes


def neighbours(x, y):
  return filter(lambda p: p in octopuses, [(x, y-1), (x, y+1), (x-1, y-1), (x+1, y+1), (x-1, y), (x+1, y), (x-1, y+1), (x+1, y-1)])

input_data = []
with open('../data/day11-input.txt') as f:
  input_data = [list(map(int, line.strip())) for line in f.readlines()]

octopuses = {(x, y): input_data[x][y] for y in range(len(input_data[0])) for x in range(len(input_data))}

print("Part I:", part1(octopuses))
print("Part II:", part2(octopuses))
import math

def cheapest_align_pos(input, triangular_cost = False):
  positions = [int(x) for x in input[0]]

  cheapest_cost = -1
  for pos in range(max(positions) + 1):
    cost = 0
    for p in positions:
      diff = abs(pos-p)
      cost += diff if not triangular_cost else math.comb((diff + 1), 2)
    if cost < cheapest_cost or cheapest_cost == -1:
      cheapest_cost = cost

  return cheapest_cost



input_data = []
with open('../data/day7-input.txt') as f:
  input_data = [line.strip().split(',') for line in f.readlines()]


print("Part I:", cheapest_align_pos(input_data)) # 344297
print("Part II:", cheapest_align_pos(input_data, triangular_cost = True)) # 97164301
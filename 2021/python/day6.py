from itertools import chain

def solution(input, days):
  fish = [int(x) for x in input[0]]
  population = {k: 0 for k in range(9)}
  
  for fh in fish:
    population[fh] += 1
  for d in range(days):
    new_fish = population[0]
    population = {k: population[k+1] for k in range(8)}
    population[6] += new_fish
    population[8] = new_fish

  return sum(population[k] for k in population)

input_data = []
with open('../data/day6-input.txt') as f:
  input_data = [line.strip().split(',') for line in f.readlines()]


print("Part I:", solution(input_data, 80)) # 383160
print("Part II:", solution(input_data, 256)) # 1721148811504

def part1(input):
  opening = ['(', '[', '{', '<']
  closing = [')', ']', '}', '>']

  closing_scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}
  score = 0
  for l in input:
    last_opening = []
    for b in l:
      if b in opening:
        last_opening.append(b)
      elif b in closing:
        open_match = opening[closing.index(b)]
        if open_match == last_opening[-1]:
          last_opening.pop(-1)
        else:
          score += closing_scoring[b]
          break
  return score

def part2(input):
  opening = ['(', '[', '{', '<']
  closing = [')', ']', '}', '>']

  closing_scoring = {')': 1, ']': 2, '}': 3, '>': 4}
  scores = []
  for l in input:
    illegals = []
    last_opening = []
    for b in l:
      if b in opening:
        last_opening.append(b)
      elif b in closing:
        open_match = opening[closing.index(b)]
        if open_match == last_opening[-1]:
          last_opening.pop(-1)
        else:
          illegals.append(b)
          break

    if len(illegals) == 0:
      score = 0
      while len(last_opening) > 0:
        closing_match = closing[opening.index(last_opening.pop(-1))]
        score *= 5
        score += closing_scoring[closing_match]
      scores.append(score)
  return sorted(scores)[int(len(scores) / 2)]

input_data = []
with open('../data/day10-input.txt') as f:
  input_data = [list(line.strip()) for line in f.readlines()]

print("Part I:", part1(input_data)) # 442131
print("Part II:", part2(input_data)) # 3646451424
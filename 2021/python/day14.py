from collections import Counter

def part1(template):
  steps = 10
  for _ in range(steps):
    template = extend_template_slow(template)
  
  counter = Counter(template).most_common()
  most_common = counter[0]
  least_common = counter[-1]
  return most_common[1] - least_common[1]

def extend_template_slow(template):
  new_template = []
  for i in range(len(template) - 1):
    pair = "".join(template[i : i+2])
    middle = rules[pair]
    new_template.extend([template[i], middle])

  new_template.append(template[-1])
  return new_template

def part2(template):
  extend_template(template, 40)

def extend_template(template, steps):
  letter_counts = Counter(template)
  pair_counts = Counter(template[i:i+2] for i in range(len(template) - 1))

  for _ in range(steps):
    ndict = Counter()
    for k, v in pair_counts.items():
        if k in rules:
            ndict.update({k[0] + rules[k]: v,  rules[k] + k[1]: v})
            letter_counts.update({rules[k]: v})
    pair_counts = ndict

  print(letter_counts.most_common()[0][1] - letter_counts.most_common()[-1][1])

with open('../data/day14-input.txt') as f:
  template, rules = f.read().split('\n\n')
  rules = {pair: middle for pair, middle in (row.strip().split(" -> ") for row in rules.splitlines())}

print("Part I:", part1(template))
print("Part II: ", end="")
part2(template)
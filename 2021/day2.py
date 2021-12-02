
data = []
with open("day2-input.txt") as f:
    data = [line.strip() for line in f.readlines()]


def part1():
  x = 0
  y = 0
  for el in data:
    command = el.split(" ")
    dir = command[0]
    amount = int(command[1])

    if dir == 'forward':
      x += amount
    elif dir == 'up':
      y -= amount
    else:
      y += amount
  
  return x * y


def part2():
  x = 0
  y = 0
  aim = 0

  for el in data:
    command = el.split(" ")
    dir = command[0]
    amount = int(command[1])

    if dir == 'down':
      aim += amount
    elif dir == 'up':
      aim -= amount
    else:
      x += amount
      y += aim*amount
  
  return x * y

print("Part I:", part1())
print("Part II:", part2())


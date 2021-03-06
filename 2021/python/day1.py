
# PART I
def part1():
  previous = None
  counter = 0

  with open("1_input.txt") as f:
    data = [int(line.strip()) for line in f.readlines()]

    for el in data:
      if previous == None:
        previous = el
        continue

      if el > previous:
        counter += 1
      
      previous = el

  return counter


# PART II
def part2():
  previous = None
  counter = 0

  with open("1_input.txt") as f:
    data = [int(line.strip()) for line in f.readlines()]

    for i in range(len(data)):
      if i >= len(data) - 2:
        break
      
      window_sum = data[i] + data[i+1] + data[i+2]

      if previous == None:
        previous = window_sum
        continue

      if window_sum > previous:
        counter += 1

      previous = window_sum

  return counter

print("Part I", part1())      
print("Part II", part2())      


def part1(input):
  gamma = []
  epsilon = [] 

  for i in range(len(input[0])):
    position_elements = get_digits_from_pos(input, i)
    gamma.append(max(position_elements, key = position_elements.count))
    epsilon.append(1-gamma[-1])

  gamma_dec = binary_array_to_decimal(gamma)
  epsilon_dec = binary_array_to_decimal(epsilon)
  return gamma_dec * epsilon_dec


def part2(input):
  oxygen = input
  co2 = input

  for i in range(len(input[0])):
    if len(oxygen) == 1:
      break

    position_elements = sorted(get_digits_from_pos(oxygen, i), reverse=True)
    position_max = max(position_elements, key=position_elements.count)
    oxygen = list(filter(lambda x : x[i] == position_max, oxygen))

  for i in range(len(input[0])):
    if len(co2) == 1:
      break
    position_elements = sorted(get_digits_from_pos(co2, i))
    position_min = min(position_elements, key=position_elements.count)
    co2 = list(filter(lambda x : x[i] == position_min, co2))

  ox_rate = binary_array_to_decimal(oxygen[0])
  co_rate = binary_array_to_decimal(co2[0])

  return ox_rate * co_rate

def get_digits_from_pos(digit_array, pos):
  return [x[pos] for x in digit_array]

def binary_array_to_decimal(digit_array):
  return int(''.join(map(str, digit_array)), 2)

data = []
with open("../data/day3-input.txt") as f:
    data = [list(map(int, line.strip())) for line in f.readlines()]

print("Part I:", part1(data)) # 3969000
print("Part II:", part2(data)) # 4267809



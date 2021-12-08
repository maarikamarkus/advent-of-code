



def part1(input):
  output_values = [x.split(' | ')[1] for x in input]
  output_digits = [x.split(' ') for x in output_values]

  counter = 0
  for sub in output_digits:
    for d in sub:
      l = len(d)
      if l == 2 or l == 3 or l == 4 or l == 7:
        counter += 1 
  return counter

def part2(input):
  input_values = [x.split(' | ')[0] for x in input]
  input_digits = [x.split(' ') for x in input_values]
  output_values = [x.split(' | ')[1] for x in input]
  output_digits = [x.split(' ') for x in output_values]

  result = 0
  for i in range(len(input_values)):
    custom_mapping = {k: set() for k in range(10)}
    for j in range(10):
      d = input_digits[i][j]
      l = len(d)

      if l == 2:
        custom_mapping[1] = set(d)
      elif l == 3:
        custom_mapping[7] = set(d)
      elif l == 4:
        custom_mapping[4] = set(d)
      elif l == 7:
        custom_mapping[8] = set(d)
    
    five_len = list(filter(lambda x: len(x) == 5, input_digits[i]))
    for d in five_len:
      d_chars = set(d)
      diff_8 = (custom_mapping[8].difference(d))
      if len(diff_8.difference(custom_mapping[4])) == 0:
         custom_mapping[2] = d_chars
      elif len(d_chars.difference(custom_mapping[1])) == 3:
        custom_mapping[3] = d_chars
      else:
        custom_mapping[5] = d_chars
    
    six_len = list(filter(lambda x: len(x) == 6, input_digits[i]))
    for d in six_len:
      d_chars = set(d)
      diff_8 = (custom_mapping[8].difference(d_chars))
      if len(diff_8.difference(custom_mapping[1])) == 0:
        custom_mapping[6] = d_chars
      elif len(custom_mapping[4].difference(d_chars)) == 0:
        custom_mapping[9] = d_chars
      else:
        custom_mapping[0] = d_chars

    comb_to_num = {"".join(sorted(v)): k for k, v in custom_mapping.items()}
    digit = ''
    for out in output_digits[i]:
      out_sorted = "".join(sorted(out))
      digit += str(comb_to_num[out_sorted])
    result += int(digit)

  return result




input_data = []
with open('../data/day8-input.txt') as f:
  input_data = [line.strip() for line in f.readlines()]


print("Part I:", part1(input_data)) # 514
print("Part II:", part2(input_data)) # 1012272
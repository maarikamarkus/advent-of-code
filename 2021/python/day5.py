
def get_lines(input, include_diagonals = False):
  lines = []

  for row in input:
    ends = [ tuple(map(int, r.split(','))) for r in row.split(' -> ')]
    x1 = ends[0][0]
    x2 = ends[1][0]
    y1 = ends[0][1]
    y2 = ends[1][1]
    
    if x1 == x2:
      line = []
      x = x1
      y_start = y1
      y_end = y2

      if y_start < y_end:
        for y in range(y_start, y_end + 1):
          line.append((x, y))
        lines.append(line)
      else:
        for y in range(y_start, y_end - 1, -1):
          line.append((x, y))
        lines.append(line)

    elif y1 == y2:
      line = []
      y = y1
      x_start = x1
      x_end = x2

      if x_start < x_end:
        for x in range(x_start, x_end + 1):
          line.append((x, y))
        lines.append(line)
      else:
        for x in range(x_start, x_end - 1, -1):
          line.append((x, y))
        lines.append(line)
    
    elif y2 - y1 == x1 - x2 and include_diagonals:
      x = x1
      y = y1
      line = []

      if y2 > y1:      
        while x >= x2 and y <= y2:
          line.append((x, y))
          x -= 1
          y += 1
        lines.append(line)
      else:
        while x <= x2 and y >= y2:
          line.append((x, y))
          x += 1
          y -= 1
        lines.append(line)
    
    elif y1 - y2 == x1 - x2 and include_diagonals:
      x = x1
      y = y1
      line = []

      if y2 < y1:
        while x >= x2 and y >= y2:
          line.append((x, y))
          x -= 1
          y -= 1
        lines.append(line)

      else:
        while x <= x2 and y <= y2:
          line.append((x, y))
          x += 1
          y += 1
        lines.append(line)

  return lines

def get_cols_rows(flat):
  col = max(flat, key = lambda x : x[0])[0]
  row = max(flat, key = lambda x : x[1])[1]
  return col, row

def part1(input):
  lines = get_lines(input)
  flat = [item for sublist in lines for item in sublist]
  cols, rows = get_cols_rows(flat)
  field = [ [0] * (cols + 1) for i in range(rows + 1)]
  for pair in flat:
    row = pair[1]
    col = pair[0]
    field[row][col] += 1

  #print('\n'.join([' '.join([str(cell) for cell in row]) for row in field]))
  flat_field = [item for sublist in field for item in sublist]
  return len(list(filter(lambda x : x >= 2, flat_field)))

def part2(input):
  lines = get_lines(input, include_diagonals=True)

  flat = [item for sublist in lines for item in sublist]
  cols, rows = get_cols_rows(flat)
  field = [ [0] * (cols + 1) for i in range(rows + 1)]
  for pair in flat:
    row = pair[1]
    col = pair[0]
    field[row][col] += 1

  #print('\n'.join([' '.join([str(cell) for cell in row]) for row in field]))
  flat_field = [item for sublist in field for item in sublist]
  return len(list(filter(lambda x : x >= 2, flat_field)))

input_data = []
with open('../data/day5-input.txt') as f:
  input_data = [line.strip() for line in f.readlines()]


print("Part I:", part1(input_data)) # 7438
print("Part II:", part2(input_data)) # 21406
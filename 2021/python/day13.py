
def part1(dots, folds):
  
  axis, pos = folds[0]
  dots = fold(dots, axis, pos)

  return len(dots)

def part2(dots, folds):
  
  for fd in folds:
    axis, pos = fd
    dots = fold(dots, axis, pos)
  
  show_dots(dots)

def fold(dots, axis, pos):
  if axis == 'x':
    dots = {dot if dot[0] < pos else (dot[0] - ((dot[0] - pos)*2), dot[1]) for dot in dots}
  else:
    dots = {dot if dot[1] < pos else (dot[0], dot[1] - ((dot[1] - pos)*2)) for dot in dots}
  return dots

def show_dots(dots):
  width = max(x for x, y in dots) + 1
  height = max(y for x, y in dots) + 1
  grid = [[" " for _ in range(width)] for _ in range(height)]
  
  for dot in dots:
    grid[dot[1]][dot[0]] = '#'

  for row in grid:
    print("".join(row))


with open('../data/day13-input.txt') as f:
  dots, folds = f.read().split('\n\n')
  dots = {(int(x), int(y)) for x, y in (row.split(',') for row in dots.splitlines())}
  folds = [(axis, int(pos)) for axis, pos in (row.split(" ")[-1].split('=') for row in folds.splitlines())]


print("Part I:", part1(dots, folds))
print("Part II:")
part2(dots, folds)

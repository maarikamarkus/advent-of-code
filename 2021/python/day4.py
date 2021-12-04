def get_data(input):
  input = list(filter(lambda x: x != '', input))
  lottery_numbers = input[0].split(',')
  boards = []

  for i in range(1, len(input[1:]), 5):
    sub_board = []
    for j in range(5):
      sub_board.append(input[i+j].split())
    boards.append(sub_board)

  return lottery_numbers, boards

def exists_winning_board(boards):
  winning_row = ['-' for i in range(5)]
  exists = False
  winners = []
  for i in range(len(boards)):
    bd = boards[i]
    # rows
    for row in bd:
      if row == winning_row:
        exists = True
        if i not in winners:
          winners.append(i)

    # columns
    for j in range(5):
      col = [row[j] for row in bd]
      if col == winning_row:
        exists = True
        if i not in winners:
          winners.append(i)

  return exists, winners

def get_unmarked_nums_sum(board):
  result = 0
  for row in board:
    for el in row:
      if el == '-':
        continue
      result += int(el)
  return result

def part1(input):
  lottery_nums, boards = get_data(input) 
  
  for num in lottery_nums:
    for sub_board in boards:
      for i in range(5):
        sub_board[i] = ['-' if x == num else x for x in sub_board[i]]
    win, board_nums = exists_winning_board(boards)
    if win:
      unmarked_sum = get_unmarked_nums_sum(boards[board_nums[0]])
      return unmarked_sum * int(num)

  return -1

def part2(input):
  lottery_nums, boards = get_data(input)
  winners = []

  for num in lottery_nums:
    for sub_board in boards:
      for i in range(5):
        sub_board[i] = ['-' if x == num else x for x in sub_board[i]]
    win, board_nums = exists_winning_board(boards)
    if win:
      for bd_num in board_nums:
        if bd_num not in winners:
          winners.append(bd_num)
      if len(winners) == len(boards):
        return get_unmarked_nums_sum(boards[winners[-1]]) * int(num)

  return -1


input_data = []
with open('../data/day4-input.txt') as f:
  input_data = [line.strip() for line in f.readlines()]


print("Part I:", part1(input_data)) # 51034
print("Part II:", part2(input_data)) # 5434
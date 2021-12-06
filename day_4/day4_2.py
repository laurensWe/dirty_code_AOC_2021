from collections import defaultdict

f = open("day_4/input_data_1.txt", "r")
bingo_input = f.readlines()

random_bingo_numbers = bingo_input.pop(0)
bingo_input.pop(0) # pop the empty line
boards = []

# Parse the boards in a dictionary
new_board = {}
row = 0
if bingo_input[-1] != '\n':
    bingo_input.append('\n')
for line in bingo_input:
    if line != "\n":
        row_numbers = line.split()
        for col, number in enumerate(row_numbers):
            new_board[number] = (row, col)
    else:
        new_board['visited'] = []
        new_board['has_won'] = False
        new_board['row_count'] = defaultdict(int)
        new_board['col_count'] = defaultdict(int)
        boards.append(new_board)
        new_board = {}
        row = 0
    row += 1

# Update all boards
all_boards_done = False
amount_boards = len(boards)
amount_won = 0
for draw_number in random_bingo_numbers.split(','):
    for board_idx, board in enumerate(boards):
        if draw_number in board.keys() and not board['has_won']:
            board['visited'].append(draw_number)
            pos_number = board[draw_number]
            row_count = board['row_count'][pos_number[0]] + 1
            col_count = board['col_count'][pos_number[1]] + 1
            board['row_count'][pos_number[0]] = row_count
            board['col_count'][pos_number[1]] = col_count
            
            # boards[board_idx] = board
            if row_count == 5 or col_count == 5:
                bingo_reached = True
                board['has_won'] = True
                amount_won += 1
                if amount_won == amount_boards:
                    all_boards_done = True
                    print("LAST BINGO!!")
                    break
    
    if all_boards_done:
        break

# Calculate score of the board
not_visited = set(board.keys()) - set(board['visited']) - set(['visited', 'row_count', 'col_count', 'has_won'])
not_visited = [int(x) for x in not_visited]
print(sum(not_visited) * int(draw_number))

from checkmate import checkmate
import random

def kpos_generator():
    return random.randint(0, 15)

def is_attacked(board, yk, xk):
    size = len(board)
    directions = {
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'Q': [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)],
    }

    for piece, dirs in directions.items():
        for dy, dx in dirs:
            ny, nx = yk + dy, xk + dx
            while 0 <= ny < size and 0 <= nx < size:
                if board[ny][nx] == '.':
                    ny += dy
                    nx += dx
                    continue
                if board[ny][nx] == piece:
                    return True
                break

    for dy, dx in [(1, -1), (1, 1)]:
        ny, nx = yk + dy, xk + dx
        if 0 <= ny < size and 0 <= nx < size and board[ny][nx] == 'P':
            return True

    for dy, dx in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                   (1, -2), (1, 2), (2, -1), (2, 1)]:
        ny, nx = yk + dy, xk + dx
        if 0 <= ny < size and 0 <= nx < size and board[ny][nx] == 'H':
            return True

    return False

# Creative bonus: Suggest King's safe moves
def suggest_safe_king_moves(board, yk, xk):
    print("Suggested safe King moves:")
    safe_moves = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            ny, nx = yk + dy, xk + dx
            if 0 <= ny < 16 and 0 <= nx < 16 and board[ny][nx] == '.':
                board[yk][xk] = '.'
                board[ny][nx] = 'K'
                if not is_attacked(board, ny, nx):
                    safe_moves.append((ny, nx))
                board[ny][nx] = '.'
                board[yk][xk] = 'K'

    if not safe_moves:
        print("No safe squares. King is surrounded!")
    else:
        for y, x in safe_moves:
            print(f"→ Row {y}, Col {x}")

def chessgame():
    print("==== Let's Play Chess Game (Catch The KING If You Can!!!) ====")
    piece_list = ['B', 'R', 'Q', 'P', 'H']
    positions = {}
    used_positions = set()

    for piece in piece_list:
        while True:
            try:
                row = int(input(f"{piece} Write Which Row Do You Want to Put Between (0-15): "))
                col = int(input(f"{piece} Write Which Col Do You Want to Put Between (0-15): "))
                if not (0 <= row <= 15 and 0 <= col <= 15):
                    print("Out of Range. Try again!")
                    continue
                if (row, col) in used_positions:
                    print(f"Error: Another piece already at ({row}, {col}! Choose Other Position!)")
                    continue
                positions[piece] = (row, col)
                used_positions.add((row, col))
                break
            except ValueError:
                print("Please Enter Valid Integers!")

    board = [['.' for _ in range(16)] for _ in range(16)]
    for p, (r, c) in positions.items():
        board[r][c] = p

    while True:
        king_row, king_col = kpos_generator(), kpos_generator()
        if board[king_row][king_col] == '.':
            board[king_row][king_col] = 'K'
            break

    print("Final Board:")
    for row in board:
        print(" ".join(row))

    board_str = "\n".join(" ".join(row) for row in board)

    print("Checking with checkmate.py:")
    checkmate(board_str)

    # if is_attacked(board, king_row, king_col):
    #     suggest_safe_king_moves(board, king_row, king_col)

def checkmate(board_str):
    # Parse each line based on whether it contains spaces
    board = []
    for row in board_str.strip().split('\n'):
        if ' ' in row:
            board.append(row.strip().split())  # spaced format
        else:
            board.append(list(row.strip()))  
    
    size = len(board)

    #Checking square board or not!
    for row in board:
        if len(row) != len(board):
            print("Error: The board is not square!")
            return
    # Find the King position
    king_pos = None
    for y in range(size):
        for x in range(size):
            if board[y][x] == 'K':
                king_pos = (y, x) #assing the position of the King
                break
        if king_pos:
            break

    if not king_pos: #if the King is not found
        print("Fail")
        return

    yk, xk = king_pos # unpack the position of the King

    # Directions for each piece type
    directions = {
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],       # Up, Down, Left, Right
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],     # Up-Left, Up-Right, Down-Left, Down-Right
        'Q': [(-1, 0), (1, 0), (0, -1), (0, 1), 
              (-1, -1), (-1, 1), (1, -1), (1, 1)],     # Rook + Bishop
    }

    # Check for directional attackers: Rook, Bishop, Queen
    for piece, dirs in directions.items():
        for dy, dx in dirs:
            curr_y, curr_x = yk + dy, xk + dx
            while 0 <= curr_y < size and 0 <= curr_x < size:
                curr = board[curr_y][curr_x]
                if curr == '.':
                    curr_y += dy
                    curr_x += dx
                    continue
                if curr == piece or (piece == 'Q' and curr == 'Q'):
                    print("Success")
                    return
                else:
                    break

    # if there are no directional attackers, check for Pawns
    for dy, dx in [(1, -1), (1, 1)]:
        curr_y, curr_x = yk + dy, xk + dx
        if 0 <= curr_y < size and 0 <= curr_x < size:
            if board[curr_y][curr_x] == 'P':
                print("Success")
                return

    print("Fail")
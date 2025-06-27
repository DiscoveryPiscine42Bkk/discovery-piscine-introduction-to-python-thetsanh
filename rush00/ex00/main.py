from checkmate import checkmate

def main():
    board = """\
. . . . . . . .
. . . . . . . .
. . . . K . . .
. . . P . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . .
"""

    board2 = """\
........
........
.....K..
........
........
........
.....J..
........
    """

    board3 = """\
. K .
P . .
    """

    board4 = """\
.....
.....
....Q
    """

    board5 = """\
. . . . . . . .
. . . K . . . 
. . . . . . . .
. . . . . Q . .
. . . . . . . .
    """


# Expected: Success

    checkmate(board)
    checkmate(board2)
    checkmate(board3)
    checkmate(board4)
    checkmate(board5)

if __name__ == "__main__":
    main()

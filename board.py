#!/usr/bin/python3


class vars():
    board ="""
    ---------------------------------------------------------
    |      |      |      |      |      |      |      |      |
    |  a8  |  b8  |  c8  |  d8  |  e8  |  f8  |  g8  |  h8  | 8
    |      |      |      |      |      |      |      |      |
    ---------------------------------------------------------
    |      |      |      |      |      |      |      |      |
    |  a7  |  b7  |  c7  |  d7  |  e7  |  f7  |  g7  |  h7  | 7
    |      |      |      |      |      |      |      |      |
    ---------------------------------------------------------
    |      |      |      |      |      |      |      |      |
    |  a6  |  b6  |  c6  |  d6  |  e6  |  f6  |  g6  |  h6  | 6
    |      |      |      |      |      |      |      |      |
    ---------------------------------------------------------
    |      |      |      |      |      |      |      |      |
    |  a5  |  b5  |  c5  |  d5  |  e5  |  f5  |  g5  |  h5  | 5
    |      |      |      |      |      |      |      |      |
    ---------------------------------------------------------
    |      |      |      |      |      |      |      |      |
    |  a4  |  b4  |  c4  |  d4  |  e4  |  f4  |  g4  |  h4  | 4
    |      |      |      |      |      |      |      |      |
    ---------------------------------------------------------
    |      |      |      |      |      |      |      |      |
    |  a3  |  b3  |  c3  |  d3  |  e3  |  f3  |  g3  |  h3  | 3
    |      |      |      |      |      |      |      |      |
    ---------------------------------------------------------
    |      |      |      |      |      |      |      |      |
    |  a2  |  b2  |  c2  |  d2  |  e2  |  f2  |  g2  |  h2  | 2
    |      |      |      |      |      |      |      |      |
    ---------------------------------------------------------
    |      |      |      |      |      |      |      |      |
    |  a1  |  b1  |  c1  |  d1  |  e1  |  f1  |  g1  |  h1  | 1
    |      |      |      |      |      |      |      |      |
    ---------------------------------------------------------
       a      b      c      d      e      f      g      h
    """
    alpha = ["a","b","c","d","e","f","g","h"]



def cleaning(board):
    # alpha = ["a","b","c","d","e","f","g","h"]
    alpha = vars.alpha
    length = len(alpha)+1
    for i in range(0,length):
        # alpha_index = alpha[i]
        for j in range(0,length):
            if i<j:
                alpha_index = alpha[i]
                old = alpha_index + str(j)
                #old = old_print
                # print(old) ---> important for # DEBUG: list the first triangle
                new = "  "
                board = board.replace(old,new)

    i_i = 7
    j_j = 0
    for l in range(0,length+1):
        # alpha_index = alpha[i]

        for m in range(0,length+1):
            if i_i>j_j:
                alpha_index_j = alpha[i_i]
                empty_str = ""
                old_j = alpha_index_j + str(j_j+1)
                #old = old_print
                # print(old_j) ---> important for # DEBUG: list the second triangle
                new_j = "  "
                board = board.replace(old_j,new_j)
                j_j = j_j + 1
        i_i = i_i - 1
        j_j = 0

    return board




# printx = input("[Move]:")
#
# board_txt = board_txt.replace(str(printx),"🌎")
#
# print(cleaning(vars.board))

import board as bd

board_s = bd.vars.board
alpha = bd.vars.alpha



for i in range(0, len(alpha)):
    out = alpha[i] + "2"
    board_se = board_s.replace(out,"👨🏾‍🎤")
for i in range(0, len(alpha)):
    out = alpha[i] + "7"
    board_se = board_s.replace(out,"👨‍🎤")
print(board_se)

print_from = input("[Move from]:")
print_to = input("[Move to]:")
board_s = board_s.replace(str(print_from),"  ")
board_s = board_s.replace(str(print_to),"👨🏾‍🎤")



# printx = input("[Move]:")
# board_s = board_s.replace(str(printx),"🌎")



clean_board = bd.cleaning(board_s)
print(clean_board)

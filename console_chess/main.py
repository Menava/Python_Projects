from board import Board
from Pieces import *

board=Board()
gameOver=False

black_pieces=board.create_pieces('L','B')
white_pieces=board.create_pieces('R','W')

board.fill_positions()
board.set_pieces(black_pieces,white_pieces)

while gameOver!=True:
    board.draw_board()
    user_input = input("Enter poisitons:")
    locations=user_input.split(' ')
    board.move_piece(locations[0],locations[1])
# board.clear_console()
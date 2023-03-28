from board import Board
from Pieces import *

board=Board()
pawn1=Pawn('Pawn 1','Pawn','left','Black')
king1=King('King','King','left','Black')
queen1=Queen('Queen','Queen','left','Black')

board.fill_positions()
board.draw_board()
board.set_pieces()
# board.clear_console()
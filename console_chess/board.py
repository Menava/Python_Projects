import os

class Board:
    board_row=['a','b','c','d','e','f','g','h']
    board_col=[1,2,3,4,5,6,7,8]
    board_position={}

    def __init__(self):
       pass

    def draw_board(self):
        for i in self.board_row:
            for j in self.board_col:
                if self.board_position[i+str(j)]!=None:
                    print(self.board_position[i+str(j)],end='')
                else:
                    print(self.board_position[i+str(j)].key(),end='')
            print('',end='\n')
    
    def fill_positions(self):
        for i in self.board_row:
            for j in self.board_col:
                self.board_position[i+str(j)]=''
    
    def set_pieces(self):
        pass
    
    def clear_console(self):
        os.system('cls')


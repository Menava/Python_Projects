import os

class Board:
    board_col=['a','b','c','d','e','f','g','h']
    board_row=[8,7,6,5,4,3,2,1]
    board_position={}

    def __init__(self):
       pass

    def draw_board(self):
        for i in self.board_row:
            for j in self.board_col:
                if self.board_position[j+str(i)]!=None:
                    print(self.board_position[j+str(i)],end=' ')
                else:
                    print(j+str(i),end=' ')
            print('',end='\n')
    
    def fill_positions(self):
        for i in self.board_row:
            for j in self.board_col:
                self.board_position[j+str(i)]=None
    
    def set_pieces(self):
        # for i in dict(list(self.board_position.items())[:16]): #add pieces for right side
        #     print(i)
        for i in dict(list(self.board_position.items())[:]): #add pieces for right side
            print(i)
    
    def clear_console(self):
        os.system('cls')


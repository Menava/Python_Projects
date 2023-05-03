import os
from Pieces import *

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
                    print(self.board_position[j+str(i)].name,end=' ')
                else:
                    print(j+str(i),end=' ')
            print('',end='\n')
    
    def fill_positions(self):
        for i in self.board_row:
            for j in self.board_col:
                self.board_position[j+str(i)]=None
    
    def set_pieces(self,black_pieces,white_pieces):
        right_counter=0
        left_counter=15

        for i in dict(list(self.board_position.items())[48:64]): #add pieces for right side
            self.board_position[i]=black_pieces[right_counter]
            right_counter+=1
        
        for i in dict(list(self.board_position.items())[0:16]): #add pieces for left side
            self.board_position[i]=white_pieces[left_counter]
            left_counter-=1
    
    def clear_console(self):
        os.system('cls')

    def create_pieces(self,side,color):
        pieces_array=[]
        for i in range(8):
            pawn=Pawn(f'p{color}',side,color)
            pieces_array.append(pawn)

        rook=Queen(f'r{color}',side,color)
        knight=Queen(f'n{color}',side,color)
        bishop=Queen(f'b{color}',side,color)
        queen=Queen(f'q{color}',side,color)
        king=King(f'k{color}',side,color)
        bishop1=Queen(f'b{color}',side,color)
        knight1=Queen(f'k{color}',side,color)
        rook1=Queen(f'r{color}',side,color)
        
        pieces_array.append(rook)
        pieces_array.append(knight)
        pieces_array.append(bishop)
        
        if color=='B':
            pieces_array.append(queen)
            pieces_array.append(king)
        else:
            pieces_array.append(king)
            pieces_array.append(queen)

        pieces_array.append(bishop1)
        pieces_array.append(knight1)
        pieces_array.append(rook1)

        return pieces_array
    
    def move_piece(self,current_location,new_location):
        if self.check_input(current_location,new_location):
            if new_location in self.board_position[current_location].possible_moves(current_location,self.board_position,self.board_col,self.board_row):
                pass
            else:
                pass
            self.board_position[new_location]=self.board_position[current_location]
            self.board_position[current_location]=None
    
    def is_possible():
        pass
    
    def check_input(self,current_location,new_location):
        if current_location in self.board_position.keys() and new_location in self.board_position.keys():
            if self.board_position[current_location]!=None:
                return True
            else:
                return False
        return False
        



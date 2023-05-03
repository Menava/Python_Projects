from .piece import Piece
class Pawn(Piece):
    piece_type='pawn'
    operation_sign=None

    def __init__(self,name,side,color):
        if side=='L':
            self.operation_sign='+'
        else:
            self.operation_sign='-'
        super().__init__(name, side,color)

    def possible_moves(self,current_location,board_position,board_col,board_row):
        calculated_moves=[]
        splited_input=self.split_input(current_location)

        outcome=splited_input[0]+str(eval(splited_input[1]+self.operation_sign+str(1)))

        calculated_moves.append(outcome)

        returned_moves=self.takable_positions(outcome,board_position,board_col,board_row)

        calculated_moves.extend(returned_moves)

        print(calculated_moves)
        
        return calculated_moves
    
    def split_input(self,input):
        return super().split_input(input)
    
    def takable_positions(self,outcome,board_position,board_col,board_row):
        splited_outcome=self.split_input(outcome)
        col_location=int(board_col.index(splited_outcome[0]))
        if col_location==0:
            temp_moves=[board_col[col_location+1]+splited_outcome[1]]
        elif col_location==7:
            temp_moves=[board_col[col_location-1]+splited_outcome[1]]
        else:
            temp_moves=[board_col[col_location-1]+splited_outcome[1],board_col[col_location+1]+splited_outcome[1]]

        for i in temp_moves:
            print(board_position[i])
        return temp_moves
    
    


class Piece:

    def __init__(self,name,side,color):
        self.name=name
        self.side=side
        self.color=color
    
    def possible_moves(self):
        pass
    
    def split_input(self,input):
        splited_list=[*input]
        return splited_list
        
    
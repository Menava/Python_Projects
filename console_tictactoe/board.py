class Board:

    board_position=[]
    def __init__(self,row,col):
        self.row=row
        self.col=col
    
    def drawBoard(self):
        count=0
        for i in range(self.row):
            for j in range(self.col):
                print(self.board_position[count],end=' ')
                count+=1
            print('',end='\n')
    
    def fillBoard(self):
        for i in range(self.row*self.col):
            self.board_position.append('*')
    
    def insertPieces(self,position,piece_type):
        self.board_position[position-1]=piece_type



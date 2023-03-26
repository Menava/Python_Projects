class Game_State:
    current_turn=None

    def __init__(self,user1,user2,board):
        self.user1=user1
        self.user2=user2
        self.board=board
    
    def print_gameState(self):
            print('User 1 remaining time:',self.current_turn.remaining_seconds)

    def change_UserTurn(self):
        if self.current_turn==self.user1:
            self.current_turn=self.user2
        else:
            self.current_turn=self.user1

    def set_currentUser(self,user):
        self.current_turn=user
    
    def init_game(self,user):
            self.set_currentUser(user)
    
    def check_win(self):
        if self.check_horizontal(self.current_turn.piece_type) or self.check_vertical(self.current_turn.piece_type) or self.check_diagonal(self.current_turn.piece_type):
            return True,self.current_turn
        else:
            return False,None

    def check_horizontal(self,piece_type):
        if self.board.board_position[0]==self.board.board_position[3]==self.board.board_position[6]==piece_type or\
        self.board.board_position[1]==self.board.board_position[4]==self.board.board_position[7]==piece_type or\
        self.board.board_position[2]==self.board.board_position[5]==self.board.board_position[8]==piece_type:
            return True
        else:
            return False
    
    def check_vertical(self,piece_type):
        if self.board.board_position[0]==self.board.board_position[1]==self.board.board_position[2]==piece_type or\
        self.board.board_position[3]==self.board.board_position[4]==self.board.board_position[5]==piece_type or\
        self.board.board_position[6]==self.board.board_position[7]==self.board.board_position[8]==piece_type:
            return True
        else:
            return False
    
    def check_diagonal(self,piece_type):
        if self.board.board_position[0]==self.board.board_position[4]==self.board.board_position[8]==piece_type or\
        self.board.board_position[2]==self.board.board_position[4]==self.board.board_position[6]==piece_type:
            return True
        else:
            return False


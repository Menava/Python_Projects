from board import Board
from user import User
from game_state import Game_State

#Main variables
gameOver=False
winner=None

#Class variables
b=Board(3,3)
user1=User('user1','X')
user2=User('user2','O')
gstate=Game_State(user1,user2,b)


b.fillBoard()
b.drawBoard()
gstate.init_game(user1) #start the game with this user


while gameOver!=True:
    user_input = int(input('Please enter your input {}: '.format(gstate.current_turn.name)))
    while gstate.check_exist(user_input) !=True:
        user_input = int(input('This position is not avaiable! Please reenter your peiece position {}: '.format(gstate.current_turn.name)))
    b.insertPieces(user_input,gstate.current_turn.piece_type)
    b.drawBoard()
    gameOver,winner=gstate.check_win()
    gstate.change_UserTurn()

print('Winner is {}!'.format(winner.name))
    
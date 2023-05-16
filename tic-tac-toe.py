class Box:
    def __init__(self, position):
        self.position = position
        self.val = " "
        

class Board:
    def __init__(self, n):
        self.size = n
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]

    def create_board(self):
        current_position = 1
        for i in range(self.size):
            for j in range(self.size):
                box = Box(current_position)
                box.val = current_position
                self.board[i][j] = box
                current_position += 1

    def show_board(self):
        for i in range(self.size):
            print('---'*self.size)
            for j in range(self.size):
                print(f"|{self.board[i][j].val}|", end='')
            print()

        print("---"*self.size)

    def get_left_positions(self):
        positionsLeft = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].position != 0:
                    positionsLeft.append(self.board[i][j].position)
        return positionsLeft  
    
    def change_the_box(self, player_input):
        for i in range(self.size):
            exit = False
            for j in range(self.size):
                if (self.board[i][j].position == int(player_input[0])):
                    self.board[i][j].position = 0
                    self.board[i][j].val = player_input[1]
                    exit = True
            if exit:
                break              


class Player:
    def __init__(self, player_val):
        self.val = player_val
        self.player_input = ""
    
    def get_input(self, positionsLeft):

        while True:
            self.player_input = input("Enter your move: ")
            if len(self.player_input) == 2:
                if int(self.player_input[0]) in positionsLeft:
                    if self.player_input[1] == self.val:
                        return self.player_input
                    else:
                        print(f"You can use only {self.val} value")
                else:
                    print("You must choose only not taken positions")
            else:
                print("Your inputs takes only 2 characters like in the example above")
                

class Game(Board):
    def __init__(self):
        self.game_status = True
        self.move = ""

    def check_the_winner(self, board):
        i = 0
        j = 0
                    
        if (board.board[i][j].val == board.board[i+1][j+1].val == board.board[i+2][j+2].val and board.board[i][j].val!=" "):
            return False
        elif (board.board[i][j+2].val == board.board[i+1][j+1].val == board.board[i+2][j].val and board.board[i][j+2].val!=" "):
            return False
        elif (board.board[i][j].val == board.board[i][j+1].val == board.board[i][j+2].val and board.board[i][j].val!=" "):
            return False
        elif (board.board[i+1][j].val == board.board[i+1][j+1].val == board.board[i+1][j+2].val and board.board[i+1][j+1].val!=" "):
            return False
        elif (board.board[i+2][j].val == board.board[i+2][j+1].val == board.board[i+2][j+2].val and board.board[i+2][j].val!=" "):
            return False
        elif(board.board[i][j].val == board.board[i+1][j].val == board.board[i+2][j].val and board.board[i][j].val!=" "):
            return False
        elif(board.board[i][j+1].val == board.board[i+1][j+1].val == board.board[i+2][j+1].val and board.board[i][j+1].val!=" "):
            return False
        elif(board.board[i][j+2].val == board.board[i+1][j+2].val == board.board[i+2][j+2].val and board.board[i][j+2].val!=" "):
            return False

        return self.game_status

    def __repr__(self):
        MyField = Board(3)
        MyField.create_board()
        MyField.show_board()

        Player1 = Player("X")
        Player2 = Player("O")

        while self.game_status:
            
            self.move = Player1.get_input(MyField.get_left_positions())
            MyField.change_the_box(self.move)
            MyField.show_board()
            self.game_status = (self.check_the_winner(MyField))

            if not(self.game_status):
                return "You win."
            
            if (len(MyField.get_left_positions()) == 0):
                return "Draw"

            self.move = Player2.get_input(MyField.get_left_positions())
            MyField.change_the_box(self.move)
            MyField.show_board()
            self.game_status = (self.check_the_winner(MyField))

            if not(self.game_status):
                return "You win."
            

MyGame = Game()
print(MyGame)


    


        
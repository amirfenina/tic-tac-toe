class TicTacToe:
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.current_player = 'X'

    def display_board(self):
        print("\n[", self.board[0], "][", self.board[1], "][", self.board[2], "]\n[", self.board[3], "][", self.board[4], "][", self.board[5], "]\n[", self.board[6], "][", self.board[7], "][", self.board[8], "]\n")

    def pick_position(self):
        while not self.check_win():
            try:
                number = input("Where do you want to place: ")
                if int(number) in range(1, 10) and self.board[int(number) - 1] != 'X' and self.board[int(number) - 1] != 'O':
                    self.board[int(number) - 1] = self.current_player
                    self.display_board()
                    self.current_player = 'X' if self.current_player == 'O' else 'O'
                else:
                    print('Please enter a number 1-9 that is not taken')
            except:
                print('Please enter a number 1-9 that is not taken')

    def check_win(self):
        if board[0] == board[1] == board[2]:
            if board[0] == 'X':
                print('X WIN')
                endgame()
            else:
                print('O WIN')
                endgame()
            return True
        if board[3] == board[4] == board[5]:
            if board[3] == 'X':
                print('X WIN')
                endgame()
            else:
                print('O WIN')
                endgame()
            return True
        if board[6] == board[7] == board[8]:
            if board[6] == 'X':
                print('X WIN')
                endgame()
            else:
                print('O WIN')
                endgame()
            return True
        if board[0] == board[3] == board[6]:
            if board[0] == 'X':
                print('X WIN')
                endgame()
            else:
                print('O WIN')
                endgame()
            return True
        if board[1] == board[4] == board[7]:
            if board[1] == 'X':
                print('X WIN')
                endgame()
            else:
                print('O WIN')
                endgame()
            return True
        if board[2] == board[5] == board[8]:
            if board[2] == 'X':
                print('X WIN')
                endgame()
            else:
                print('O WIN')
                endgame()
            return True
        if board[0] == board[4] == board[8]:
            if board[0] == 'X':
                print('X WIN')
                endgame()
            else:
                print('O WIN')
                endgame()
            return True
        if board[2] == board[4] == board[6]:
            if board[2] == 'X':
                print('X WIN')
                endgame()
            else:
                print('O WIN')
                endgame()
            return True
        if board.count('X')+board.count('O') == 9:
            print('IS A DRAW')
            endgame()
            return True
        else:
            return False
        pass

    def end_game(self):
        again = input('\nDo you want to play again? (Y/n)')
        if again == 'Y':
            self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.current_player = 'X'
            self.start_game()
        elif again == 'n':
            return
        else:
            print("Please answer Y or n")
            self.end_game()

    def start_game(self):
        print("Welcome to the XO game! (Tic Tac Toe)")
        self.display_board()
        self.pick_position()


if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
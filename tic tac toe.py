import sys

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
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] or \
               self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2]:
                winner = self.board[i]  # Get the winner
                print(winner, 'WIN')
                self.end_game()
                return True

        if self.board[0] == self.board[4] == self.board[8] or \
           self.board[2] == self.board[4] == self.board[6]:
            winner = self.board[4]  # Get the winner
            print(winner, 'WIN')
            self.end_game()
            return True

        if all(isinstance(cell, str) for cell in self.board):
            print('IT\'S A DRAW')
            self.end_game()
            return True

        return False

    def end_game(self):
        again = input('\nDo you want to play again? (Y/n)')
        if again == 'Y':
            self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.current_player = 'X'
            self.display_board()
            self.pick_position()
        elif again == 'n':
            sys.exit(0)
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

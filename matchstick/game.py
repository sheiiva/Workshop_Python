######################################################
#                                                    #
#                   Workshop Python3                 #
#                      ---------                     #
#               Corentin COUTRET-ROZET               #
#                                                    #
# Github: https://github.com/sheiiva/Workshop_Python #
######################################################


from sys import argv


class Game():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._max = int(argv[1])
        self._sticks = 30

    def getSticks(self, player) -> int:

        """
        Ask to player for how much stick.s they want to remove.
        """

        def isValidInput(sticks):
            if sticks < 1 or sticks > self._max:
                print("Enter a number between 1 and {}.".format(self._max))
                return False
            return True

        try:
            sticks = int(input("Player {}: ".format(player)))
        except ValueError:  # If input cannot be cast to an int
            print("Wrong input. Please enter an integer.")
            sticks = self.getSticks(player)
        except KeyboardInterrupt:  # Quit the game if get a Ctrl+'C'
            print("\nexit")
            exit(0)
        else:
            if not isValidInput(sticks):
                sticks = self.getSticks(player)
        return sticks

    def play(self, player) -> None:

        """
        Player's turn.
        """

        self._sticks -= self.getSticks(player)
        if self._sticks <= 0:
            print("Player {} lost the game!".format(player))
            exit(0)

    def run(self) -> None:

        """
        Run the main loop of the game.
        """

        def printBoard() -> None:
            print(self._sticks * '|', end="\n\n")

        print("WELCOME ON MATCHSTICK GAME!\n")
        printBoard()
        while True:
            self.play(1)
            printBoard()
            self.play(2)
            printBoard()

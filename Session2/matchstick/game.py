######################################################
#                                                    #
#                Workshop Python3 (2/4)              #
#                      ---------                     #
#                Corentin COUTRET-ROZET              #
#                                                    #
# Github: https://github.com/sheiiva/Workshop_Python #
######################################################


from sys import argv

PLAYER1 = 1
PLAYER2 = 2


MAX = int(argv[1])
STICKS = 30

def getSticks(player: int) -> int:
    """
    Ask to player for how much stick.s they want to remove.

    Args:
        player (int): Player's number.

    Returns:
        int: Number of sticks removed.
    """

    def isValidInput(sticks: int) -> bool:
        """
        Check for input validity.

        Args:
            sticks (int): Input sticks number to be checked.

        Returns:
            bool: Ture if valid. False otherwise.
        """

        if sticks < 1 or sticks > MAX:
            print("Enter a number between 1 and {}.".format(MAX))
            return False
        return True

    try:
        sticks = int(input("Player {}: ".format(player)))
    except ValueError:  # If input cannot be cast to an int
        print("Wrong input. Please enter an integer.")
        sticks = getSticks(player)
    except KeyboardInterrupt:  # Quit the game if get a Ctrl+'C'
        print("\nexit")
        exit(0)
    else:
        if not isValidInput(sticks):
            sticks = getSticks(player)
    return sticks

def play(player: int) -> None:
    """
    Player's turn.

    Args:
        player (int): Player's number.
    """

    STICKS -= getSticks(player)
    if STICKS <= 0:
        print("Player {} lost the game!".format(player))
        exit(player)

def run() -> None:

    """
    Run the main loop of the game.
    """

    def printBoard() -> None:
        print(STICKS * '|', end="\n\n")

    print("WELCOME ON MATCHSTICK GAME!\n")
    while True:
        printBoard()
        play(PLAYER1)
        printBoard()
        play(PLAYER2)

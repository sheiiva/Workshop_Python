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


def getSticks(player: int, maxSticks: int) -> int:
    """
    Ask to player for how much stick.s they want to remove.

    Args:
        player (int): Player's number.

    Returns:
        int: Number of sticks removed.
    """

    def isValidInput(sticks: int, maxSticks: int) -> bool:
        """
        Check for input validity.

        Args:
            sticks (int): Input sticks number to be checked.

        Returns:
            bool: Ture if valid. False otherwise.
        """

        if sticks < 1 or sticks > maxSticks:
            print("Enter a number between 1 and {}.".format(maxSticks))
            return False
        return True

    try:
        sticks = int(input("Player {}: ".format(player)))
    except ValueError:  # If input cannot be cast to an int
        print("Wrong input. Please enter an integer.")
        sticks = getSticks(player, maxSticks)
    except KeyboardInterrupt:  # Quit the game if get a Ctrl+'C'
        print("\nexit")
        exit(0)
    else:
        if not isValidInput(sticks, maxSticks):
            sticks = getSticks(player, maxSticks)
    return sticks


def play(player: int, sticks: int, maxSticks: int) -> int:
    """
    Player's turn.

    Args:
        player (int): Player's number.
    """

    n_sticks = sticks - getSticks(player, maxSticks)
    if n_sticks <= 0:
        print("Player {} lost the game!".format(player))
        exit(player)
    return n_sticks


def run(maxSticks: int) -> None:

    """
    Run the main loop of the game.
    """

    sticks = 30

    def printBoard(sticks: int) -> None:
        print(sticks * '|', end="\n\n")

    print("WELCOME ON MATCHSTICK GAME!\n")
    while True:
        printBoard(sticks)
        sticks = play(PLAYER1, sticks, maxSticks)
        printBoard(sticks)
        sticks = play(PLAYER2, sticks, maxSticks)

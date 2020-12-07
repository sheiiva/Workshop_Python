######################################################
#                                                    #
#                Workshop Python3 (2/4)              #
#                      ---------                     #
#                Corentin COUTRET-ROZET              #
#                                                    #
# Github: https://github.com/sheiiva/Workshop_Python #
######################################################


def checkArgs(argv: list) -> int:
    """
    Check for arguments validity.

    Args:
        argv (list): Input arguments.

    Returns:
        int: 0 if success. 84 otherwise.
    """

    def isNum(value) -> bool:
        """
        Check values type.

        Args:
            value (any): Value to be checked.

        Returns:
            bool: True if value is an int. False otherwise.
        """

        try:
            int(value)
        except ValueError:
            False
        else:
            return True

    if len(argv) != 2:
        print("Wrong number of arguments. Please retry with -h.")
        return 84
    elif not isNum(argv[1]):
        print("Arguments must be integers. Please retry with -h.")
        return 84
    elif int(argv[1]) <= 0 or int(argv[1]) >= 30:
        print("Wrong input value. Please retry with -h.")
        return 84
    return 0


def needHelp(argv: list) -> bool:
    """
    Check if user is asking for help.

    Args:
        argv (list): Input arguments.

    Returns:
        bool: True if help flag. Flase otherwise.
    """

    if "-h" in argv or "--help" in argv:
        return True
    return False

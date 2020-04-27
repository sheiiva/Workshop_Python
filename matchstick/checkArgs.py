######################################################
#                                                    #
#                   Workshop Python3                 #
#                      ---------                     #
#               Corentin COUTRET-ROZET               #
#                                                    #
# Github: https://github.com/sheiiva/Workshop_Python #
######################################################


class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for arguments validity.
        """

        def isNum(value) -> bool:

            """Return True if value is a digit. Return False otherwise."""

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

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False

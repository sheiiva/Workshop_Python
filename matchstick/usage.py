######################################################
#                                                    #
#                   Workshop Python3                 #
#                      ---------                     #
#               Corentin COUTRET-ROZET               #
#                                                    #
# Github: https://github.com/sheiiva/Workshop_Python #
######################################################

class Help():

    def __init__(self):
        self.help()

    def help(self) -> None:
        """
        Show usage of the program.
        """

        print("USAGE\n"
            "\t./matchstick max\n\n"
            "DESCRIPTION\n"
            "\tmax\tthe maximum number of matchsticks that can be taken out each turn (must be > 0)")

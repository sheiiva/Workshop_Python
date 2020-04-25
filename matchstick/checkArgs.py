#!/usr/bin/env python3
#coding: utf-8

class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for arguments validity.
        """

        def isNum(value):

            """Return True if value is a digit."""

            try:
                int(value)
            except:
                False
            else:
                return True

        if len(argv) != 3:
            print("Wrong number of arguments. Please retry with -h.")
            return 84
        elif not isNum(argv[1]) or not isNum(argv[2]):
            print("Arguments must be integers. Please retry with -h.")
            return 84
        elif int(argv[1]) <= 0 or not (int(argv[2]) > 0 and int(argv[2]) <= 100):
            print("Wrong input value. Please retry with -h.")
            return 84
        return 0


    def needHelp(self, argv):

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False

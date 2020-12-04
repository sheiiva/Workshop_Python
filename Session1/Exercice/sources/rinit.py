#!/usr/bin/env python3
#coding: utf-8

######################################################
#                                                    #
#                Workshop Python3 (1/4)              #
#                      ---------                     #
#                Corentin COUTRET-ROZET              #
#                                                    #
# Github: https://github.com/sheiiva/Workshop_Python #
######################################################

from os import getcwd, system
from sys import argv, stderr

PATH_TO_TEMPLATE = "/home/co/Documents/Epitech/HUB/Workshop_Python/Session1/Exercice/deps/template"
CURRENT_PATH = getcwd()

commands = []

# COPY FROM TEMPLATE
commands.append("cp -r {}/* {}".format(PATH_TO_TEMPLATE, CURRENT_PATH))
commands.append("cp -r {}/.gitignore {}".format(PATH_TO_TEMPLATE, CURRENT_PATH))

for command in commands:
    system(command)

# CHANGE BINARY NAME
BINARY = 'binary'
FILE = 'Makefile'

if (len(argv) != 2):
    print("ERROR: please enter the binary that might be created by the Makefile.", file=stderr)
    exit(84)

# Read input file
fin = open(FILE, "rt")
# Read file contents to string
data = fin.read()
# Replace all occurrences of the required string
data = data.replace('binary', '{}'.format(argv[1]))
# Close the input file
fin.close()
# Open the input file in write mode
fin = open(FILE, "wt")
# Overrite the input file with the resulting data
fin.write(data)
# Close the file
fin.close()

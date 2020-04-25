Matchstick
===

Language:   Python


The project
----
This project is based on a very famous game based on matchsticks.
There is a certain number of matchstick lines.
The two players take turns; each player can, on a same line, take one or several matchsticks.
The losing player is the one to take the last matchstick.

The two players take turns; each player can, on a same line, take one or several matchsticks.
The losing player is the one to take the last matchstick.

The goal of the project is to create a program that you can play against.
The basic version must generate a game board with n matchstick lines (1 < n < 100).

When matchsticks are removed, they must be removed starting from the right.
In case of bad input, you must ask for the line by displaying “Line: ” again, and it’s up to the player to indicate again the line they wants to play on.


##### OUTPUT
If the user wins, the program must return 1.
If the AI wins, it must return 2.


## USAGE:

```
>> ./matchstick -h
USAGE
	./matchstick lines max

DESCRIPTION
	lines		the number of lines (n in ]0, 100])
	max			the maximum number of matchsticks that can be taken out each turn (must be > 0)
```

Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva)

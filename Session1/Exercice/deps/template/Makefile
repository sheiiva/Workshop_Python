##
## W O R K S H O P  P Y T H O N
## Corentin COUTRET-ROZET
##
## MAKEFILE
##

LD			=	gcc
PRINT		=	@echo -e
RM          =   @rm -f

override CFLAGS 	+=	-W -Wall -Werror -Wextra
override CFLAGS 	+=	-I./include

SRC		=	sources/main.c

OBJ 	= 	$(SRC:.c=.o)

NAME 		= 	$(ROOT_PATH)binary

$(NAME): $(OBJ)
	$(PRINT) "\n------->\tCOMPILED SRC DEPENDENCIES.\n\nLET'S LINK IT ALL:\n"
	$(LD) $^ $(LDFLAGS) $(LDLIBS) -o $@
	$(PRINT) "\n------->\tCONGRATS !\n"

all: $(NAME)

clean:
	$(PRINT) "\n------->\tREMOVE GENERATOR TMP FILES\n"
	$(RM) $(OBJ) $(OBJ:.o=.gcno) $(OBJ:.o=.gcda)

fclean: clean
	$(PRINT) "------->\tREMOVE GENERATOR\n"
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
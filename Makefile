##
## EPITECH PROJECT, 2022
## 204ducks
## File description:
## Makefile
##

BIN	=	204ducks

all:
	cp 204ducks.py $(BIN)

clean:
	rm -rf $(BIN)

fclean:	clean

re:	clean	all

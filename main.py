import game
import sys

from terminal.colors import *
from terminal.term import Term


if __name__ == "__main__":
    args = sys.argv[1:]

    random_colors = False
    if args and args[0] in ["random", "r", "-r", "--random"]:
        random_colors = True

    term = Term()
    tetris = game.GameTetris(term, random_colors)
    tetris.run()

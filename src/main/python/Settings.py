"""Konstanten für TicTacToe"""
import pygame as pg

NAME_PLAYER_1 = "Spieler 1"
NAME_PLAYER_2 = "Spieler 2"
START_PLAYER = NAME_PLAYER_1

GRID_DIMENSION = 3
BOARD_SIZE = 400
CELL_SIZE = int(BOARD_SIZE // GRID_DIMENSION)
BOARD_HEIGHT = int(BOARD_SIZE + CELL_SIZE)

SYMBOL_SIZE = int(CELL_SIZE * 0.75)
SYMBOL_PLAYER_1 = pg.transform.scale(pg.image.load("../../../images/X.png"), (SYMBOL_SIZE, SYMBOL_SIZE))
SYMBOL_PLAYER_2 = pg.transform.scale(pg.image.load("../../../images/O.png"), (SYMBOL_SIZE, SYMBOL_SIZE))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

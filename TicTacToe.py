"""TicTacToe-Spiel zur Bearbeitung der Aufgaben im Modul SWE im WS 21/22"""
import sys
import pygame as pg
import time
from pygame.locals import QUIT
from Grid import Grid
from Settings import NAME_PLAYER_1, NAME_PLAYER_2, START_PLAYER, BOARD_SIZE, CELL_SIZE, BOARD_HEIGHT
from Settings import SYMBOL_PLAYER_1, SYMBOL_PLAYER_2, WHITE, BLACK, RED

pg.init()
FPS = 30
CLOCK = pg.time.Clock()

actual_player = ""
screen = pg.display.set_mode((BOARD_SIZE, BOARD_HEIGHT))
winner = ""
draw = False


def initialize_board():
    """Spielbrett initialisieren"""
    global winner, draw, grid, cells_array, actual_player
    pg.display.set_caption("Tic Tac Toe")
    screen.fill(BLACK)
    winner = None
    draw = False
    actual_player = START_PLAYER
    grid = Grid()
    cells_array = Grid.get_cells_array(grid)
    screen.blit(Grid.get_grid_surface(grid), (0, 0))
    schrift = pg.font.Font(None, 30)
    text = schrift.render(START_PLAYER + " ist dran!", True, WHITE)
    screen.fill(BLACK, (0, BOARD_SIZE, BOARD_SIZE + CELL_SIZE, CELL_SIZE))
    text_rect = text.get_rect(center=(BOARD_SIZE / 2, BOARD_SIZE + CELL_SIZE
                                      - CELL_SIZE / 2))
    screen.blit(text, text_rect)
    pg.display.flip()


def evaluate_turn():
    """abgeschlossenen Zug Spielende überprüfen"""
    check_vertical()
    check_horizontal()
    check_diagonal()
    check_if_draw()
    set_message()


def check_vertical():
    """3 gleiche Symbole in Zeile?"""
    global winner
    for row in range(0, 3):
        if cells_array[row][0] == cells_array[row][1] == cells_array[row][2] and cells_array[row][0] is not None:
            winner = cells_array[row][0]
            pg.draw.line(screen, (250, 0, 0),
                         (0, (row + 1) * CELL_SIZE - CELL_SIZE / 2),
                         (BOARD_SIZE, (row + 1) * CELL_SIZE - CELL_SIZE / 2),
                         4)


def check_horizontal():
    """3 x gleiches Symbol in einer Spalte?"""
    global winner
    for column in range(0, 3):
        if (cells_array[0][column] == cells_array[1][column] == cells_array[2][column]
                and (cells_array[0][column] is not None)):
            winner = cells_array[0][column]
            pg.draw.line(screen, RED, ((column + 1) * CELL_SIZE - CELL_SIZE / 2, 0),
                         ((column + 1) * CELL_SIZE - CELL_SIZE / 2, BOARD_SIZE), 4)


def check_diagonal():
    """ 3x gleiches Symbol diagonal?"""
    global winner
    if cells_array[0][0] == cells_array[1][1] == cells_array[2][2] and (cells_array[0][0] is not None):
        # diagonal links nach rechts
        winner = cells_array[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
    if cells_array[0][2] == cells_array[1][1] == cells_array[2][0] and (cells_array[0][2] is not None):
        # diagonal rechts nach links
        winner = cells_array[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)


def check_if_draw():
    """ Alle Felder voll, aber kein Gewinner? Unentschieden"""
    global draw
    if all([all(zeile) for zeile in cells_array]) and winner is None:
        draw = True


def evaluate_click():
    """Mausklick auf Grid auswerten, Symbol zeichnen"""
    global actual_player
    spacing = 15
    click_pos = grid.get_grid_coords(pg.mouse.get_pos())

    row_clicked, column_clicked = click_pos[0]
    symbol_x_pos = click_pos[1][0] + spacing
    symbol_y_pos = click_pos[1][1] + spacing
    cells_array[row_clicked][column_clicked] = actual_player
    if actual_player == NAME_PLAYER_1:
        screen.blit(SYMBOL_PLAYER_1, (symbol_x_pos, symbol_y_pos))
        actual_player = NAME_PLAYER_2
    else:
        screen.blit(SYMBOL_PLAYER_2, (symbol_x_pos, symbol_y_pos))
        actual_player = NAME_PLAYER_1
    pg.display.update()
    evaluate_turn()


def set_message():
    """Statuszeile anpassen"""
    global winner, draw
    if winner is None:
        message = actual_player + " ist dran"
    else:
        message = winner + " hat gewonnen !"
    if draw:
        message = "Unentschieden !"
    schrift = pg.font.Font(None, 30)
    text = schrift.render(message, True, WHITE)
    # Statusmeldung einblenden
    screen.fill(BLACK, (0, BOARD_SIZE, BOARD_HEIGHT, 100))
    text_rect = text.get_rect(center=(400 / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()


def reset_game():
    """automatischer Neustart 3 Sekunden nach Ende eines Spiels"""
    time.sleep(2)
    initialize_board()
    set_message()


initialize_board()
"""Spielschleife"""
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            evaluate_click()
        if winner or draw:
            reset_game()
    pg.display.update()
    CLOCK.tick(FPS)

import sys
import time
import pygame as pg
from pygame.locals import *
from Grid import *
from Settings import *

pg.init()
fps = 30
CLOCK = pg.time.Clock()
global winner, draw


actual_player = ""
screen = pg.display.set_mode((BOARD_SIZE, BOARD_HEIGHT))


def initialize_board():
    global winner, draw, grid, cells_array, actual_player
    pg.display.set_caption("Tic Tac Toe")
    screen.fill(BLACK)
    winner = None
    draw = None
    actual_player = START_PLAYER
    grid = Grid()
    cells_array = Grid.get_cells_array(grid)
    screen.blit(Grid.get_grid_surface(grid), (0, 0))
    schrift = pg.font.Font(None, 30)
    text = schrift.render(START_PLAYER + " ist dran!", True, (WHITE))
    screen.fill(BLACK, (0, BOARD_SIZE, BOARD_SIZE + CELL_SIZE, CELL_SIZE))
    text_rect = text.get_rect(center=(BOARD_SIZE / 2, BOARD_SIZE + CELL_SIZE - CELL_SIZE/2))
    screen.blit(text, text_rect)
    pg.display.flip()

def evaluate_turn():
    global winner, draw
    # 3 Zeilen gleiches Symbol?
    for row in range(0, 3):
        if (cells_array[row][0] == cells_array[row][1] == cells_array[row][2] and cells_array[row][0] is not None):
            # print(str(zeile) + " voll: " + str(cells_array[zeile[0]]))
            winner = cells_array[row][0]
            print(winner)
            pg.draw.line(screen, (250, 0, 0),
                         (0, (row + 1) * CELL_SIZE - CELL_SIZE/2),
                         (BOARD_SIZE, (row + 1) * CELL_SIZE - CELL_SIZE/2),
                         4)
            break
    # 3 Spalten gleiches Symbol?
    for column in range(0, 3):
        if (cells_array[0][column] == cells_array[1][column] == cells_array[2][column]
                and (cells_array[0][column] is not None)):
            print(cells_array[0][column])
            winner = cells_array[0][column]
            pg.draw.line(screen, (RED), ((column + 1) * CELL_SIZE - CELL_SIZE/2, 0), ((column + 1)
                                    * CELL_SIZE - CELL_SIZE/2, BOARD_SIZE), 4)
            break
    # 3x gleiches Symbol diagonal?
    if (cells_array[0][0] == cells_array[1][1] == cells_array[2][2] and (cells_array[0][0] is not None)):
        # diagonal links nach rechts
        winner = cells_array[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
    if (cells_array[0][2] == cells_array[1][1] == cells_array[2][0] and (cells_array[0][2] is not None)):
        # diagonal rechts nach links
        winner = cells_array[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
    # Alle Felder voll, aber kein Gewinner? Unentschieden
    if (all([all(zeile) for zeile in cells_array]) and winner is None):
        draw = True
    set_message()




def evaluate_click():
    # global row, column, actual_player
    global actual_player
    spacing = 15
    click_pos = grid.get_grid_coords(pg.mouse.get_pos())

    row_clicked, column_clicked = click_pos[0]
    print("row_clicked, column")
    print(row_clicked, column_clicked)
    symbol_x_pos = click_pos[1][0] + spacing
    symbol_y_pos = click_pos[1][1] + spacing
    print(row_clicked, column_clicked, (cells_array[row_clicked][column_clicked]))
    # if (row and column and (cells_array[row][column] is not None)):
    cells_array[row_clicked][column_clicked] = actual_player
    print(cells_array[row_clicked][column_clicked])
    print(actual_player + ", " + NAME_PLAYER_1)
    if (actual_player == NAME_PLAYER_1):
        print("actual: " + actual_player + "player1: " + NAME_PLAYER_1)
        screen.blit(SYMBOL_PLAYER_1, (symbol_x_pos, symbol_y_pos))
        actual_player = NAME_PLAYER_2
    # wenn Spieler 2 geklickt hat, Y einblenden, Spielerwechsel
    else:
        screen.blit(SYMBOL_PLAYER_2, (symbol_x_pos, symbol_y_pos))
        actual_player = NAME_PLAYER_1
    pg.display.update()
    evaluate_turn()


def set_message():
    global winner, draw
    print("Gewinner: " + str(winner))
    if winner is None:
        message = actual_player + " ist dran"
    else:
        message = winner + " hat gewonnen !"
    if draw:
        message = "Unentschieden !"
    # Schriftobjekt erstellen
    schrift = pg.font.Font(None, 30)
    # Schriftfarbe = (255,255,255)
    text = schrift.render(message, True, ((WHITE)))
    # Statusmeldung einblenden
    screen.fill((BLACK), (0, BOARD_SIZE, BOARD_HEIGHT, 100))
    text_rect = text.get_rect(center=(400 / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()


def reset_game():
    time.sleep(2)
    initialize_board()
    set_message()

initialize_board()
while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            evaluate_click()
        if (winner or draw):
            print("reset aufrufen")
            reset_game()
    pg.display.update()
    CLOCK.tick(fps)

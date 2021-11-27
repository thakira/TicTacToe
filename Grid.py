# Kästchenmuster für Spielbrett erstellen
import pygame as pg
from Settings import BOARD_SIZE, CELL_SIZE, GRID_DIMENSION, WHITE, BLACK


class Grid:

    def __init__(self):
        self.grid_size = BOARD_SIZE
        self.dimension = GRID_DIMENSION
        self.cell_size = int(CELL_SIZE)
        self.surface = pg.Surface((self.grid_size, self.grid_size))
        # self.surface.set_alpha(150)
        self.surface.fill(WHITE)

        # Liste für Zelleninhalte erstellen
        self.cells = []
        for self.row in range(self.dimension):
            self.cells.append([])
            for self.column in range(self.dimension):
                self.cells[self.row].append(None)

        # Hintergrund und Zwischenlinien zeichnen
        for x in range(0, self.grid_size, self.cell_size):
            pg.draw.lines(self.surface, BLACK, False,
                          [[0, x], [self.grid_size, x]], 1)
            pg.draw.lines(self.surface, BLACK, False,
                          [[x, 0], [x, self.grid_size]], 1)

    def get_grid_surface(self):
        return self.surface

    def get_cells_array(self):
        return self.cells

    # Column und Row aus den übergebenen Bildschirmkoordinaten ermitteln
    def get_grid_coords(self, pos):
        column = pos[0] // self.cell_size
        row = pos[1] // self.cell_size
        coords = (row, column)
        x = column * self.cell_size
        y = row * self.cell_size
        cellcenter = (x, y)
        return coords, cellcenter

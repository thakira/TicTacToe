# Kästchenmuster für Schiffe erstellen
import pygame as pg


class Grid:

    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.cell_size = int(grid_size/3)
        # self.grid_pos_x = 0
        # self.grid_pos_y = 0
        # Anzeige für Grid erstellen
        self.surface = pg.Surface((self.grid_size, self.grid_size))
        self.surface.set_alpha(180)
        self.surface.fill((155, 181, 196))

        # Array für Zelleninhalte erstellen
        self.cells = []
        for self.row in range(3):
            self.cells.append([])
            for self.column in range(3):
                self.cells[self.row].append(0)

        # Hintergrund und Zwischenlinien zeichnen
        for x in range(0, self.grid_size, self.cell_size):
            pg.draw.lines(self.surface, (255, 255, 255), False,
                          [[0, x], [self.grid_size, x]], 1)
            pg.draw.lines(self.surface, (255, 255, 255), False,
                          [[x, 0], [x, self.grid_size]], 1)


    def get_grid_surface(self):
        return self.surface

    # Column und Row aus den übergebenen Bildschirmkoordinaten ermitteln
    def get_grid_coords(self, pos):
        print("Zellengrösse")
        print(self.cell_size)
        column = pos[0] // self.cell_size
        row = pos[1] // self.cell_size
        coords = (row +1, column+1)
        x = column * (self.cell_size)
        y = row * (self.cell_size)
        cellcenter = (x, y)
        return coords, cellcenter




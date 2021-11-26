import pygame as pg
import sys
import time
from pygame.locals import *
from Grid import *

aktueller_spieler = '1'
gewinner = None
unentschieden = None
spielbrett = [[None] * 3, [None] * 3, [None] * 3]
pg.init()
fps = 30
CLOCK = pg.time.Clock()
anzeige = pg.display.set_mode((400, 400 + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")
x_img = pg.image.load("images/X.png")
y_img = pg.image.load("images/O.png")
x_img = pg.transform.scale(x_img, (100, 100))
o_img = pg.transform.scale(y_img, (100, 100))
newGrid = Grid(400)
# newGrid_surface = Grid.get_grid_surface(Grid(400))

def start_spielbrett():

    anzeige.fill((255,255,255))
    anzeige.blit(Grid.get_grid_surface(newGrid), (0, 0))
    # pg.draw.line(anzeige, (0,0,0), (400 / 3, 0), (400 / 3, 400), 4)
    # pg.draw.line(anzeige, (0,0,0), (400 / 3 * 2, 0), (400 / 3 * 2, 400), 4)
    # pg.draw.line(anzeige, (0,0,0), (0, 400 / 3), (400, 400 / 3), 4)
    # pg.draw.line(anzeige, (0,0,0), (0, 400 / 3 * 2), (400, 400 / 3 * 2), 4)
    pg.display.update()
    statusmeldung_anpassen()
def statusmeldung_anpassen():
    global unentschieden
    if gewinner is None:
        statusmeldung = "Spieler " + aktueller_spieler + " ist dran"
    else:
        statusmeldung = "Spieler " + gewinner + " hat gewonnen !"
    if unentschieden:
        statusmeldung = "Unentschieden !"
    # Schriftobjekt erstellen
    schrift = pg.font.Font(None, 30)
    # Schriftfarbe = (255,255,255)
    text = schrift.render(statusmeldung, True, ((255,255,255)))
    # Statusmeldung einblenden
    anzeige.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(400 / 2, 500 - 50))
    anzeige.blit(text, text_rect)
    pg.display.update()
def zug_auswerten():
    global spielbrett, gewinner, unentschieden
    # 3 Zeilen gleiches Symbol?
    for zeile in range(0, 3):
        if ((spielbrett[zeile][0] == spielbrett[zeile][1] == spielbrett[zeile][2]) and (spielbrett[zeile][0] is not None)):
            gewinner = spielbrett[zeile][0]
            pg.draw.line(anzeige, (250, 0, 0),(0, (zeile + 1) * 400 / 3 - 400 / 6),(400, (zeile + 1) * 400 / 3 - 400 / 6),4)
            break
    # 3 Spalten gleiches Symbol?
    for spalte in range(0, 3):
        if ((spielbrett[0][spalte] == spielbrett[1][spalte] == spielbrett[2][spalte]) and (spielbrett[0][spalte] is not None)):
            gewinner = spielbrett[0][spalte]
            pg.draw.line(anzeige, (250, 0, 0), ((spalte + 1) * 400 / 3 - 400 / 6, 0),((spalte + 1) * 400 / 3 - 400 / 6, 400), 4)
            break
    # 3x gleiches Symbol diagonal?
    if (spielbrett[0][0] == spielbrett[1][1] == spielbrett[2][2]) and (spielbrett[0][0] is not None):
        # diagonal links nach rechts
        gewinner = spielbrett[0][0]
        pg.draw.line(anzeige, (250, 70, 70), (50, 50), (350, 350), 4)
    if (spielbrett[0][2] == spielbrett[1][1] == spielbrett[2][0]) and (spielbrett[0][2] is not None):
        # diagonal rechts nach links
        gewinner = spielbrett[0][2]
        pg.draw.line(anzeige, (250, 70, 70), (350, 50), (50, 350), 4)
    # Alle Felder voll, aber kein Gewinner? Unentschieden
    if (all([all(zeile) for zeile in spielbrett]) and gewinner is None):
        unentschieden = True
    statusmeldung_anpassen()

def mausklick_auswerten():
    abstand = 15
    click_pos = newGrid.get_grid_coords(pg.mouse.get_pos())
    zeile, spalte = click_pos[0]
    symbol_x_pos = click_pos[1][0]+abstand
    symbol_y_pos = click_pos[1][1]+abstand
    if (zeile and spalte and spielbrett[zeile -1 ][spalte -1] is None):
        global aktueller_spieler
        spielbrett[zeile - 1][spalte - 1] = aktueller_spieler
        if (aktueller_spieler == '1'):
            # Wenn Spieler 1 geklickt hat, X einblenden, Spielerwechsel
            #anzeige.blit(x_img, (pos_y, pos_x))
            # anzeige.blit(x_img, (pos_x + 15, pos_y + 15))
            anzeige.blit(x_img, (symbol_x_pos, symbol_y_pos))
            aktueller_spieler = '2'
        # wenn Spieler 2 geklickt hat, Y einblenden, Spielerwechsel
        else:
            anzeige.blit(o_img, (symbol_x_pos, symbol_y_pos))
            aktueller_spieler = '1'
        pg.display.update()
        zug_auswerten()
def spielelemente_initialisieren():
    global spielbrett, gewinner, aktueller_spieler, unentschieden
    time.sleep(3)
    aktueller_spieler = '1'
    unentschieden = False
    start_spielbrett()
    gewinner = None
    spielbrett = [[None] * 3, [None] * 3, [None] * 3]
start_spielbrett()
while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mausklick_auswerten()
            if (gewinner or unentschieden):
                spielelemente_initialisieren()
    pg.display.update()
    CLOCK.tick(fps)

import random

# Constantes représentant la taille de la grille
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Classe représentant un navire
class Ship:
    def __init__(self, length):
        self.length = length
        self.hit_points = length
        self.sunk = False

# Classe représentant une grille de jeu
class Grid:
    def __init__(self):
        self.grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.ships = []

    # Fonction pour placer un navire sur la grille
    def place_ship(self, ship, x, y, horizontal):
        if horizontal:
            for i in range(ship.length):
                self.grid[y][x + i] = ship
        else:
            for i in range(ship.length):
                self.grid[y + i][x] = ship
        self.ships.append(ship)

    # Fonction pour tirer sur une coordonnée de la grille

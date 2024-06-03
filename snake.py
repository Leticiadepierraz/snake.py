'''
Nom: Leticia Dépierraz
Programme : Début de Pygame, recréation du snake
Date : 1 juin 2024
'''

import pygame
from random import randint
from tkinter import *

# Partie Tkinter pour le premier menu
def start_game():
    win.destroy()  # Fermer la fenêtre Tkinter et commencer le jeu Pygame

# Configuration de la fenêtre Tkinter
win = Tk()
win.title("Menu Principal")
#définir la couleur de la fenêtre
win.configure(bg='#B8D9CD')

def center_window(window, width, height):
    """
    Permet de centrer la fenêtre.
    :param window: la fenêtre à centrer
    :param width: largeur de la fenêtre
    :param height: hauteur de la fenêtre
    """
    # Calcul de la taille de l'écran
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcul des coordonnées pour centrer la fenêtre
    center_x = int(screen_width / 2 - width / 2)
    center_y = int(screen_height / 2 - height / 2)

    # Positionnement de la fenêtre
    window.geometry(f"{width}x{height}+{center_x}+{center_y}")

center_window(win, 300, 200)

# Frame
frame_nom_jeu = Frame(win,bg="#B8D9CD")
frame_nom_jeu.pack(pady=20)

# Label
label = Label(frame_nom_jeu, text="Jeu du Snake", background="#B8D9CD")
label.pack()

# Ajout d'un bouton pour démarrer le jeu
start_button = Button(win, text="Démarrer le jeu", command=start_game,bg="#DCF2EC")
start_button.pack(pady=20)

win.mainloop()

# Partie Pygame
def drawFood():
    food_color = pygame.Color(255, 0, 0)
    food_rect = pygame.Rect((food[0] * tile_W, food[1] * tile_H), (tile_W, tile_H))
    pygame.draw.rect(root, food_color, food_rect)

def drawSnake():
    snake_color = pygame.Color(60, 215, 60)
    for cell in snake:
        cell_rect = pygame.Rect((cell[0] * tile_W, cell[1] * tile_H), (tile_W, tile_H))
        pygame.draw.rect(root, snake_color, cell_rect)

def updateSnake(direction):
    global food
    dirX, dirY = direction
    head = snake[0].copy()
    head[0] = (head[0] + dirX) % tiles_X
    head[1] = (head[1] + dirY) % tiles_Y

    if head in snake[1:]:
        return False
    elif head == food:
        food = None
        while food is None:
            newfood = [
                randint(0, tiles_X - 1),
                randint(0, tiles_Y - 1)
            ]
            food = newfood if newfood not in snake else None
    else:
        snake.pop()

    snake.insert(0, head)
    return True

# Initialisation de Pygame
pygame.init()

# Variable
score = 0
font = pygame.font.SysFont('Arial', 25)

# Générer la fenêtre de notre jeu
pygame.display.set_caption("Snake")
sw = 640
sh = 480

root = pygame.display.set_mode((sw, sh))

# Importer et charger l'arrière-plan de notre jeu
bg_color = pygame.Color(22, 41, 85)

# Définir où on va jouer
tiles_X = 32
tiles_Y = 24

tile_W = sw // tiles_X
tile_H = sh // tiles_Y

# Définir le snake
snk_x, snk_y = tiles_X // 4, tiles_Y // 2

snake = [
    [snk_x, snk_y],
    [snk_x - 1, snk_y],
    [snk_x - 2, snk_y]
]

# Définir notre nourriture
food = [tiles_X // 2, tiles_Y // 2]

# Boucle principale du jeu
running = True
direction = [1, 0]

while running:
    pygame.time.Clock().tick(20)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RIGHT and direction != [-1, 0]:  # Touche pour aller à droite
                direction = [1, 0]
            elif event.key == pygame.K_LEFT and direction != [1, 0]:  # Touche pour aller à gauche
                direction = [-1, 0]
            elif event.key == pygame.K_UP and direction != [0, 1]:  # Touche pour aller en haut
                direction = [0, -1]
            elif event.key == pygame.K_DOWN and direction != [0, -1]:  # Touche pour aller en bas
                direction = [0, 1]

    # Mettre à jour le snake
    if not updateSnake(direction):
        print("Game over")
        running = False

    # Dessiner
    root.fill(bg_color)
    drawFood()
    drawSnake()

    pygame.display.update()

pygame.quit()

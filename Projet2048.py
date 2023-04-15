import tkinter as tk
import random

#Initialisation de la grille de jeu 
grid = [[0 for i in range(4)] for j in range(4)]

#Fonction pour ajouter une tuile aléatoire sur la grille
def add_random_tile():
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_tiles:
        x, y = random.choice(empty_tiles)
        grid[x][y] = random.choice([2, 4])

#Fonction pour empiler les tuiles d'une ligne vers la gauche
def move_left():
    global grid
    for i in range(4):
        j = 0
        while j < 3:
            if grid[i][j] == 0:
                k = j + 1
                while k < 4 and grid[i][k] == 0:
                    k += 1
                if k < 4:
                    grid[i][j], grid[i][k] = grid[i][k], grid[i][j]
            elif grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0
                j += 1
            j += 1

#Fonction pour empiler les tuiles d'une ligne vers la droite
def move_right():
    global grid
    for i in range(4):
        j = 3
        while j > 0:
            if grid[i][j] == 0:
                k = j - 1
                while k >= 0 and grid[i][k] == 0:
                    k -= 1
                if k >= 0:
                    grid[i][j], grid[i][k] = grid[i][k], grid[i][j]
            elif grid[i][j] == grid[i][j-1]:
                grid[i][j] *= 2
                grid[i][j-1] = 0
                j -= 1
            j -= 1

#Fonction pour empiler les tuiles d'une colonne vers le haut
def move_up():
    global grid
    for j in range(4):
        i = 0
        while i < 3:
            if grid[i][j] == 0:
                k = i + 1
                while k < 4 and grid[k][j] == 0:
                    k += 1
                if k < 4:
                    grid[i][j], grid[k][j] = grid[k][j], grid[i][j]
            elif grid[i][j] == grid[i+1][j]:
                grid[i][j] *= 2
                grid[i+1][j] = 0
                i += 1
            i += 1

#Fonction pour empiler les tuiles d'une colonne vers le bas
def move_down():
    global grid
    for j in range(4):
        i = 3
        while i > 0:
            if grid[i][j] == 0:
                k = i - 1
                while k >= 0 and grid:
                 [k][j] == 0
                k -= 1
            if k >= 0:
                grid[i][j], grid[k][j] = grid[k][j], grid[i][j]
            elif grid[i][j] == grid[i-1][j]:
             grid[i][j] *= 2
            grid[i-1][j] = 0
            i -= 1
        i -= 1

#Fonction pour afficher la grille de jeu
def display_grid():
    for i in range(4):
        for j in range(4):
            cell = tk.Label(root, text=str(grid[i][j]), font=('Helvetica', 20), width=4, height=2, borderwidth=1, relief='solid')
            cell.grid(row=i+1, column=j)

#Fonction pour commencer une partie
def start_game():
    global grid
    grid = [[0 for i in range(4)] for j in range(4)]
    add_random_tile()
    add_random_tile()
    display_grid()

#Fonction pour sauvegarder une partie en cours dans un fichier texte
def save_game():
    with open('saved_game.txt', 'w') as f:
        for i in range(4):
            for j in range(4):
                f.write(str(grid[i][j]) + ' ')
                f.write('\n')

#Fonction pour charger une partie enregistrée dans un fichier
def load_game():
    global grid
    with open('saved_game.txt', 'r') as f:
        for i in range(4):
            line = f.readline()
            cells = line.split()
            for j in range(4):
                grid[i][j] = int(cells[j])
                display_grid()

#Création de la fenêtre principale
root = tk.Tk()

#Création des boutons
play_button = tk.Button(root, text='Play', command=start_game)
play_button.grid(row=0, column=0)

left_button = tk.Button(root, text='Left', command=move_left)
left_button.grid(row=0, column=1)

right_button = tk.Button(root, text='Right', command=move_right)
right_button.grid(row=0, column=2)

down_button = tk.Button(root, text='Down', command=move_down)
down_button.grid(row=1, column=1)

up_button = tk.Button(root, text='Up', command=move_up)
up_button.grid(row=1, column=2)

exit_button = tk.Button(root, text='Exit', command=root.quit)
exit_button.grid(row=2, column=0)

save_button = tk.Button(root, text='Save', command=save_game)
save_button.grid(row=2, column=1)

load_button = tk.Button(root, text='Load', command=load_game)
load_button.grid(row=2, column=2)

#Lancement de la fenêtre principale
root.mainloop()
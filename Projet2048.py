import tkinter as tk
import random

# Fonction pour ajouter une tuile de manière aléatoire
def add_random_tile():
    global grid
    empty_cells = [(i,j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])

# Fonction pour déplacer les tuiles vers la gauche
def move_left():
    global grid
    for i in range(4):
        new_row = []
        merged = []
        for j in range(4):
            if grid[i][j] != 0:
                if not new_row:
                    new_row.append(grid[i][j])
                else:
                    if grid[i][j] == new_row[-1] and (i,j) not in merged:
                        new_row[-1] *= 2
                        merged.append((i,j))
                    else:
                        new_row.append(grid[i][j])
        new_row += [0] * (4 - len(new_row))
        grid[i] = new_row
    move_left_button = tk.Button(root, text="Déplacer à gauche", width=20, command=move_left)

# Fonction pour déplacer les tuiles vers la droite
def move_right():
    global grid
    for i in range(4):
        new_row = []
        merged = []
        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                if not new_row:
                    new_row.append(grid[i][j])
                else:
                    if grid[i][j] == new_row[-1] and (i,j) not in merged:
                        new_row[-1] *= 2
                        merged.append((i,j))
                    else:
                        new_row.append(grid[i][j])
        new_row = [0] * (4 - len(new_row)) + new_row
        grid[i] = new_row

# Fonction pour déplacer les tuiles vers le haut
def move_up():
    global grid
    for j in range(4):
        new_column = []
        merged = []
        for i in range(4):
            if grid[i][j] != 0:
                if not new_column:
                    new_column.append(grid[i][j])
                else:
                    if grid[i][j] == new_column[-1] and (i,j) not in merged:
                        new_column[-1] *= 2
                        merged.append((i,j))
                    else:
                        new_column.append(grid[i][j])
        new_column += [0] * (4 - len(new_column))
        for i in range(4):
            grid[i][j] = new_column[i]

# Fonction pour déplacer les tuiles vers le bas
def move_down():
    global grid
    for j in range(4):
        new_column = []
        merged = []
        for i in range(3, -1, -1):
            if grid[i][j] != 0:
                if not new_column:
                    new_column.append(grid[i][j])
                else:
                    if grid[i][j] == new_column[-1] and (i,j) not in merged:
                        new_column[-1] *= 2
                        merged.append((i,j))
                    else:
                        new_column.append(grid[i][j])
        new_column = [0] * (4 - len(new_column)) + new_column
        for i in range(4):
            grid[i][j] = new_column[i]

# Fonction pour sauvegarder une partie en cours dans
# fichier texte
def save_game():
    global grid
    with open("saved_game.txt", "w") as file:
        for row in grid:
            line = ",".join(str(tile) for tile in row)
            file.write(line + "\n")
    print("Partie sauvegardée !")

# Fonction pour charger une partie enregistrée
def load_game():
    global grid
    with open("saved_game.txt", "r") as file:
        lines = file.readlines()
        grid = [[int(tile) for tile in line.strip().split(",")] for line in lines]
    print("Partie chargée !")

# Fonction pour afficher la grille
def display_grid():
    global grid
    for i in range(4):
        for j in range(4):
            value = grid[i][j]
            if value == 0:
                label = tk.Label(root, text="", width=4, height=2, font=("Arial", 30), relief="solid", borderwidth=1)
            else:
                label = tk.Label(root, text=str(value), width=4, height=2, font=("Arial", 30), relief="solid", borderwidth=1)
            label.grid(row=i+1, column=j)

# Fonction pour commencer une partie
def start_game():
    global grid
    for i in range(4):
        for j in range(4):
            grid[i][j] = 0
    add_random_tile()
    add_random_tile()
    display_grid()

# Fonction pour quitter le jeu et afficher le score
def exit_game():
    global grid
    score = sum([sum(row) for row in grid])
    print("Score : {}".format(score))
    root.destroy()

# Initialisation de la grille et création de la fenêtre
grid = [[0]*4 for i in range(4)]
root = tk.Tk()
root.title("2048")

# Création des boutons
play_button = tk.Button(root, text="Jouer", command=start_game)
play_button.grid(row=0, column=0, padx=10, pady=10)

left_button = tk.Button(root, text="Gauche", command=move_left)
left_button.grid(row=0, column=1, padx=10, pady=10)

right_button = tk.Button(root, text="Droite", command=move_right)
right_button.grid(row=0, column=2, padx=10, pady=10)

down_button = tk.Button(root, text="Bas", command=move_down)
down_button.grid(row=0, column=3, padx=10, pady=10)

up_button = tk.Button(root, text="Haut", command=move_up)
up_button.grid(row=0, column=4, padx=10, pady=10)

save_button = tk.Button(root, text="Sauvegarder", command=save_game)
save_button.grid(row=0, column=5, padx=10, pady=10)

load_button = tk.Button(root, text="Charger", command=load_game)
load_button.grid(row=0, column=6, padx=10, pady=10)

exit_button = tk.Button(root, text="Quitter", command=exit_game)
exit_button.grid(row=0, column=7, padx=10, pady=10)




# Affichage de la fenêtre
root.mainloop()
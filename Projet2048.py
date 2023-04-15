import tkinter as tk
import random

# Fonction pour ajouter une tuile aléatoire dans la grille
def add_random_tile():
    global grid
    empty_cells = [(i,j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2,4])

# Fonction pour déplacer les tuiles vers la gauche
def move_left(event=None):
    global grid
    moved = False
    for i in range(4):
        row = grid[i]
        row = [tile for tile in row if tile != 0]
        while len(row) < 4:
            row.append(0)
        for j in range(3):
            if row[j] == row[j+1] and row[j] != 0:
                row[j] *= 2
                row[j+1] = 0
                moved = True
        row = [tile for tile in row if tile != 0]
        while len(row) < 4:
            row.append(0)
        grid[i] = row
    if moved:
        add_random_tile()
        display_grid()

# Fonction pour déplacer les tuiles vers la droite
def move_right(event=None):
    global grid
    moved = False
    for i in range(4):
        row = grid[i]
        row = [tile for tile in row if tile != 0]
        while len(row) < 4:
            row.insert(0,0)
        for j in range(3, 0, -1):
            if row[j] == row[j-1] and row[j] != 0:
                row[j] *= 2
                row[j-1] = 0
                moved = True
        row = [tile for tile in row if tile != 0]
        while len(row) < 4:
            row.insert(0,0)
        grid[i] = row
    if moved:
        add_random_tile()
        display_grid()

# Fonction pour déplacer les tuiles vers le haut
def move_up(event=None):
    global grid
    moved = False
    for j in range(4):
        column = [grid[i][j] for i in range(4)]
        column = [tile for tile in column if tile != 0]
        while len(column) < 4:
            column.append(0)
        for i in range(3):
            if column[i] == column[i+1] and column[i] != 0:
                column[i] *= 2
                column[i+1] = 0
                moved = True
        column = [tile for tile in column if tile != 0]
        while len(column) < 4:
            column.append(0)
        for i in range(4):
            grid[i][j] = column[i]
    if moved:
        add_random_tile()
        display_grid()

# Fonction pour déplacer les tuiles vers le bas
def move_down(event=None):
    global grid
    moved = False
    for j in range(4):
        column = [grid[i][j] for i in range(4)]
        column = [tile for tile in column if tile != 0]
        while len(column) < 4:
            column.insert(0,0)
        for i in range(3, 0, -1)            
         if column[i] == column[i-1] and column[i] != 0:
                column[i] *= 2
                column[i-1] = 0
                moved = True
        column = [tile for tile in column if tile != 0]
        while len(column) < 4:
            column.insert(0,0)
        for i in range(4):
            grid[i][j] = column[i]
    if moved:
        add_random_tile()
        display_grid()

# Fonction pour afficher la grille
def display_grid():
    global grid, tiles
    for i in range(4):
        for j in range(4):
            value = grid[i][j]
            if value == 0:
                tiles[i][j].config(text="", bg="#ccc0b3")
            else:
                tiles[i][j].config(text=str(value), bg=tile_colors[value], fg=text_colors[value])
    score_label.config(text="Score: " + str(sum(sum(row) for row in grid)))

# Fonction pour sauvegarder la grille dans un fichier
def save_grid():
    global grid
    with open("saved_game.txt", "w") as f:
        for i in range(4):
            for j in range(4):
                f.write(str(grid[i][j]) + " ")
            f.write("\n")

# Fonction pour charger la grille depuis un fichier
def load_grid():
    global grid
    try:
        with open("saved_game.txt", "r") as f:
            for i in range(4):
                line = f.readline().strip().split()
                for j in range(4):
                    grid[i][j] = int(line[j])
            display_grid()
    except FileNotFoundError:
        pass

# Initialisation de la grille
grid = [[0 for j in range(4)] for i in range(4)]

# Ajout de deux tuiles aléatoires pour commencer
add_random_tile()
add_random_tile()

# Couleurs des tuiles et du texte
tile_colors = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}
text_colors = {
    2: "#776e65",
    4: "#776e65",
    8: "#f9f6f2",
    16: "#f9f6f2",
    32: "#f9f6f2",
    64: "#f9f6f2",
    128: "#f9f6f2",
    256: "#f9f6f2",
    512: "#f9f6f2",
    1024: "#f9f6f2",
    2048: "#f9f6f2"
}

# Création de la fenêtre principale et de la grille de jeu
root = tk.Tk()
root.title("2048")
root.geometry("400x500")
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

tiles = []
for i in range(4):
    row = [] 
    for j in range(4):
        tile = tk.Label(root, text="", width=4, height=2, font=("Helvetica", 32, "bold"), bg="#ccc0b3")
        tile.grid(row=i+1, column=j, padx=5, pady=5)
        row.append(tile)
    tiles.append(row)

# Ajout des boutons
play_button = tk.Button(root, text="Play", width=10, command=reset_game)
play_button.grid(row=0, column=0, padx=5, pady=5)

save_button = tk.Button(root, text="Save", width=10, command=save_grid)
save_button.grid(row=0, column=1, padx=5, pady=5)

load_button = tk.Button(root, text="Load", width=10, command=load_grid)
load_button.grid(row=0, column=2, padx=5, pady=5)

exit_button = tk.Button(root, text="Exit", width=10, command=root.destroy)
exit_button.grid(row=0, column=3, padx=5, pady=5)

score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 16, "bold"))
score_label.grid(row=5, columnspan=4)

# Affichage de la grille initiale
display_grid()

# Boucle principale de la fenêtre
root.mainloop()
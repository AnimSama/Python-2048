import tkinter as tk
import random

# Initialisation de la grille
grid = [[0] * 4 for _ in range(4)]

# Fonction pour ajouter une tuile de manière aléatoire
def add_random_tile():
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
    add_random_tile()
    display_grid()

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
    add_random_tile()
    display_grid()

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
    add_random_tile()
    display_grid()

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
        new_column += [0] * (4 - len(new_column))
        for i in range(4):
            grid[i][j] = new_column[i]
        add_random_tile()
    display_grid()


# Fonction pour afficher la grille
def display_grid():
    for i in range(4):
        for j in range(4):
            tile_label = tile_labels[i][j]
            value = grid[i][j]
            if value == 0:
                tile_label.configure(text="", bg="gray")
            else:
                tile_label.configure(text=str(value), bg=TILE_COLORS[value],
                                     fg="white" if value <= 4 else "black")
#Création de la fenêtre principale
window = tk.Tk()
window.title("2048")

#Création des étiquettes pour les tuiles
TILE_COLORS = {
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
2048: "#edc22e",
}
tile_labels = []
for i in range(4):
    row_labels = []
    for j in range(4):
        label = tk.Label(window, text="", font=("Arial", 32), width=4, height=2, borderwidth=5, relief="groove")
        label.grid(row=i, column=j, padx=5, pady=5)
        row_labels.append(label)
        tile_labels.append(row_labels)

#Ajout de deux tuiles aléatoires au début
add_random_tile()
add_random_tile()

#Fonction pour gérer les touches de direction
def handle_key(event):
    if event.keysym == "Left":
        move_left()
    elif event.keysym == "Right":
        move_right()
    elif event.keysym == "Up":
        move_up()
    elif event.keysym == "Down":
        move_down()

#Ajout d'un gestionnaire d'événements pour les touches de direction
window.bind("<Left>", handle_key)
window.bind("<Right>", handle_key)
window.bind("<Up>", handle_key)
window.bind("<Down>", handle_key)

#Affichage de la grille initiale
display_grid()

# Fonction pour commencer une partie
def start_game():
    global grid
    for i in range(4):
        for j in range(4):
            grid[i][j] = 0
    add_random_tile()
    add_random_tile()
    display_grid()

#Fonction pour sauvegarder une partie en cours dans
#fichier texte
def save_game():
    global grid
    with open("saved_game.txt", "w") as file:
        for row in grid:
            line = ",".join(str(tile) for tile in row)
            file.write(line + "\n")
            print("Partie sauvegardée !")

#Fonction pour charger une partie enregistrée
def load_game():
    global grid
    with open("saved_game.txt", "r") as file:
        for row in grid:
            line = ",".join(str(tile) for tile in row)
            file.write(line + "\n")
    print("Partie sauvegardée !")

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


#Affichage de la fenêtre principale
window.mainloop()
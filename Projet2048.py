#on importe les module
import tkinter as tk
import random

#on commence par definir la fonction principal
class Game(tk.Frame):
    

    Couleur_grille = "#b8afa9"
    Couleur_CelluleVide = "#ffd5b5"
    Police_ScoreLabel = ("Verdana", 24)
    Police_Score = ("Helvetica", 48, "bold")
    Police_GameOver = ("Helvetica", 48, "bold")
    Police_Couleur_GameOver = "#ffffff"
    Winner_BG = "#ffcc00"
    Loser_BG = "#a39489" 

    Couleur_Cellule = {
        2: "#fcefe6",
        4: "#f2e8cb",
        8: "#f5b682",
        16: "#f29446",
        32: "#ff775c",
        64: "#e64c2e",
        128: "#ede291",
        256: "#fce130",
        512: "#ffdb4a",
        1024: "#f0b922",
        2048: "#fad74d"    
    }

    Couleur_Nombre = {
        2: "#695c57",
        4: "#695c57",
        8: "#ffffff",
        16: "#ffffff",
        32: "#ffffff",
        64: "#ffffff",
        128: "#ffffff",
        256: "#ffffff",
        512: "#ffffff",
        12048: "#ffffff"
    }

    Police_Nombre = {
        2: ("Helvetica", 55, "bold"),
        4: ("Helvetica", 55, "bold"),
        8: ("Helvetica", 55, "bold"),
        16: ("Helvetica", 50, "bold"),
        32: ("Helvetica", 50, "bold"),
        64: ("Helvetica", 50, "bold"),
        128: ("Helvetica", 45, "bold"),
        256: ("Helvetica", 45, "bold"),
        512: ("Helvetica", 45, "bold"),
        1024: ("Helvetica", 40, "bold"),
        2048: ("Helvetica", 40, "bold"),
    }    

       #Fonction principal
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048 L1MIASHS ")

        self.grid_main = tk.Frame(
            self, bg=Game.Couleur_grille, bd=3, width=600, height=600
        )
        self.grid_main.grid(pady=(110,0))

        self.GUI_maker()
        self.start_game()

        self.master.bind("<Gauche>", self.left)
        self.master.bind("<Droite>", self.right)
        self.master.bind("<Haut>", self.up)
        self.master.bind("<Bas>", self.down)

        self.mainloop()
    
    #Interface graphique
    def GUI_maker(self):
        #création de la grille principale
        self.cellule = []
        for i in range(4):
            row = []
            for j in range(4):
                frame_cells = tk.Frame(
                    self.grid_main,
                    bg=Game.Couleur_CelluleVide,
                    width=150,
                    height=150
                    
                )
                frame_cells.grid(row=i, column=j, padx=5, pady=5)
                Cellule_Nombre = tk.Label(self.grid_main, bg=Game.Couleur_CelluleVide)
                Cellule_Data = {"image":frame_cells, "nombre": Cellule_Nombre}

                Cellule_Nombre.grid(row=i, column=j)
                row.append(Cellule_Data)
            self.cellule.append(row)

        #Creation entête Score

        image_score = tk.Frame(self)
        image_score.place(relx=0.5, y=60, anchor="center")
        tk.Label(
            image_score,
            text="Score",
            police=Game.Police_ScoreLabel
        ).grid(row=0)
        self.label_score = tk.Label(image_score, text="0", police= Game.Police_Score)
        self.label_score.grid(row=1)

        image_score = tk.Frame(self)
        image_score.place(relx=0.5, y=60, anchor="center")
        tk.Label(
            image_score,
            text="Score",
            police=Game.Police_ScoreLabel
        ).grid(row=0)
        self.label_score = tk.Label(image_score, text="0", police= Game.Police_Score)
        self.label_score.grid(row=1)

   #fonction pour lancer le jeux
    def start_game(self):
        #creation de matrice avec pour contenant le chiffre zero
        self.matrice = [[0] * 4 for _ in range(4)]

        #Remplir deux cellule au hasard avec deux seconde d'eccart
        row = random.randint(0,3)
        col = random.randint(0,3)
        self.matrice[row][col] = 2
        self.cellule[row][col]["image"].configure(bg=Game.Couleur_Cellule[2])
        self.cellule[row][col]["nombre"].configure(
            bg=Game.Couleur_Cellule[2],
            fg=Game.Couleur_Nombre[2],
            police=Game.Police_Nombre[2],
            text="2"
        )
        while(self.matrice[row][col] != 0):
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrice[row][col] = 2
        self.cellule[row][col]["image"].configure(bg=Game.Couleur_Cellule[2])
        self.cellule[row][col]["nombre"].configure(
            bg=Game.Couleur_Cellule[2],
            fg=Game.Couleur_Nombre[2],
            police=Game.Police_Nombre[2],
            text="2"
        )

        self.score = 0

def main():
    Game()

if __name__ == "__main__":
    main()
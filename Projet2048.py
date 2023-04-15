import tkinter as tk
import random as rd # libraire pour choisir aléatoirement des tuiles
import numpy as np # libraire pour appliquer des probabilités sur les apparitions de tuiles
import pickle as pc # librairie pour la sauvegarde et le chargement de parties  



#couleurs 


Couleur_Grille = "#a39489" 
Couleur_Cellule_Vide = "#c2b3a9" 
Police_Score_Etiq = ("Verdana", 24)
Police_Score =("Helvetica", 36, "bold")
Police_Fin_Jeux = ("Helvetica", 48, "bold")
Police_Fin_Jeux_Couleur = "#ffffff" 
Fond_Gagnant = "#ffcc00" 
Fond_Perdant = "#a39489" 



Couleurs_Cellules = {
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

Nombres_Cellules = {
	2: "#695c57",
	4: "#695c57",
	8: "#ffffff",
	16: "#ffffff",
	32: "#ffffff",
	64: "#ffffff",
	128: "#ffffff",
	256: "#ffffff",
	512: "#ffffff",
	1024: "#ffffff",
	2048: "#ffffff"
}

Fonts_Cellules= {
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







          
    # Interface graphique
    
racine = tk.Tk()
racine.title("2048")


    # Variables globales
        
cellules = []   # contient chaque détail de chaque tuile (couleur+nombre)
matrice = [] # contient les nombres présents sur la grille
end = None   # cette variable donnera si la partie est gagnée ou perdue,
              # 1 = gagné et 0 = perdu


    # Fonctions premières  
       
def Creation_Interface():
    """Cette fonction va créer la plateforme de jeu"""
    global cellules
    for i in range (4):
        ligne = []
        for j in range (4):
            cellule_frame = tk.Frame(background, bg=Couleur_Cellule_Vide, width=120, height=120)
            cellule_frame.grid(row=i, column=j, padx=5, pady=5)
            cellule_number = tk.Label(background, bg=Couleur_Cellule_Vide)
            cellule_number.grid(row=i, column=j)
            cellule_data = {"frame": cellule_frame, "number": cellule_number}
            ligne.append(cellule_data)
        cellules.append(ligne)
    
    
def Actualisation_Interface():
    """Cette fonction va actualiser les couleurs/affichages dans le plateau"""
    global cellules
    for i in range (4):
        for j in range (4):
            valeur_cellule = matrice[i][j]
            if valeur_cellule == 0:
                cellules[i][j]["frame"].config(bg=Couleur_Cellule_Vide)
                cellules[i][j]["number"].config(bg=Couleur_Cellule_Vide, text="") 
            else:
                cellules[i][j]["frame"].config(bg=Couleurs_Cellules[valeur_cellule])
                cellules[i][j]["number"].config(bg=Couleurs_Cellules[valeur_cellule], 
                                             fg=Nombres_Cellules[valeur_cellule],
                                             font=Fonts_Cellules[valeur_cellule],
                                             text=str(valeur_cellule))
    

def Generateur_Tuile(mat):
    """ Cette fonction donne à matrice une tuile créée aléatoirement"""
    row = rd.randint(0,3)
    col = rd.randint(0,3)
    if Zero_In_Mat() == True:
        while mat[row][col]!=0:
            row = rd.randint(0,3)
            col = rd.randint(0,3)
        mat[row][col] = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    else:
        pass
    return mat


    # Empilation
def Empiler_Gauche(mat):
    """Place les tuiles vers la gauche"""
    matrice2 = [[0]*4 for _ in range (4)]
    for i in range (4):
        pos = 0
        for j in range (4):
            if mat[i][j] != 0:
                matrice2[i][pos] = mat[i][j]
                pos+=1
    mat = matrice2  
    return mat
    
def Empiler_Droite(mat):
    """Place les tuiles vers la droite"""
    matrice2 = [[0]*4 for _ in range (4)]
    for i in range (4):
        pos = -1
        for j in range (1,5):
            if mat[i][-j] != 0:
                matrice2[i][pos] = mat[i][-j]
                pos-=1
    mat = matrice2
    return mat

def Empiler_Haut(mat):
    """Place les tuiles vers le haut"""
    matrice2 = [[0]*4 for _ in range (4)]
    for j in range (4):
        pos = 0
        for i in range (4):
            if mat[i][j] != 0:
                matrice2[pos][j] = mat[i][j]
                pos+=1
    mat = matrice2
    return mat

def Empiler_Bas(mat):
    """Place les tuiles vers le bas"""
    matrice2 = [[0]*4 for _ in range (4)]
    for j in range (4):
        pos = -1
        for i in range (1,5):
            if mat[-i][j] != 0:
                matrice2[pos][j] = mat[-i][j]
                pos-=1
    mat = matrice2
    return mat
    
    # Combinaison
def Combiner_Gauche(mat):
    """ Cette fonction permettra de combiner 2 tuiles de même nombre vers la gauche"""
    for i in range (4):
        for j in range (3):
            if mat[i][j] != 0 and mat[i][j] == mat[i][j+1]:
                mat[i][j] *= 2
                mat[i][j+1] = 0
    return mat
                
def Combiner_Droite(mat):
    """ Cette fonction permettra de combiner 2 tuiles de même nombre vers la droite"""
    for i in range (4):
        for j in range (1,4):
            if mat[i][-j] != 0 and mat[i][-j] == mat[i][-j-1]:
                mat[i][-j] *= 2
                mat[i][-j-1] = 0
    return mat
                
def Combiner_Haut(mat):
    """ Cette fonction permettra de combiner 2 tuiles de même nombre vers le haut"""
    for i in range (3):
        for j in range (4):
            if mat[i][j] != 0 and mat[i][j] == mat[i+1][j]:
                mat[i][j] *= 2
                mat[i+1][j] = 0
    return mat
                
def Combiner_Bas(mat):
    """ Cette fonction permettra de combiner 2 tuiles de même nombre vers le bas"""
    for i in range (1,4):
        for j in range (4):
            if mat[-i][j] != 0 and mat[-i][j] == mat[-i-1][j]:
                mat[-i][j] *= 2
                mat[-i-1][j] = 0
    return mat
                
    

    # Fonctions associées aux boutons
       
def Generateur():
    """ Cette fonction génère 2 tuiles aléatoirement et les affiche dans le jeu """
    global cellules
    global matrice
    # réinitialiser la plateforme de jeu ainsi que les 2 tuiles placées
    matrice = []
    cellules = []
    Creation_Interface()
    
    # début du code
    matrice = [[0]*4 for _ in range (4)]
    
    # générer 2 tuiles aléatoires
    row = rd.randint(0,3)
    col = rd.randint(0,3)
    tuile = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    matrice[row][col] = tuile 
    cellules[row][col]["frame"].config(bg=Couleurs_Cellules[tuile])
    cellules[row][col]["number"].config(bg=Couleurs_Cellules[tuile], 
                                     fg=Nombres_Cellules[tuile], 
                                     font=Fonts_Cellules[tuile], 
                                     text=str(tuile)
                                     )
    while matrice[row][col]!=0:
        row = rd.randint(0,3)
        col = rd.randint(0,3)
    tuile = np.random.choice(np.arange(2, 5, 2), p=[0.9, 0.1])
    matrice[row][col] = tuile 
    cellules[row][col]["frame"].config(bg=Couleurs_Cellules[tuile])
    cellules[row][col]["number"].config(bg=Couleurs_Cellules[tuile], 
                                     fg=Nombres_Cellules[tuile], 
                                     font=Fonts_Cellules[tuile], 
                                     text=str(tuile)
 
                                     )
def Start_Button():
    """ Cette fonction est destinée au bouton 'Start' """
    Generateur() 

       
def Exit_Button():
    """ Cette fonction est destinée au bouton 'Exit' """
    racine.destroy()
    
    
def Sauvegarde_Button():
    """ Cette fonction est destinée au bouton 'Sauvegarde' """
    fic = open("Sauvegarde_liste.txt", "wb") 
    pc.dump(matrice, fic)
    fic.close()
    

def Load_Button():
    """ Cette fonction est destinée au bouton 'Load' """
    global matrice
    
    matrice2 = []
    fic = open("Sauvegarde_liste.txt", "rb")
    b = pc.load(fic)
    fic.close()
    
    for line in b:
        matrice2.append(line)
    
    matrice = matrice2

    Actualisation_Interface()
    

    # Fonctions associées aux déplacements

def Left_Button():
    global matrice
    matrice = Empiler_Gauche(matrice)
    matrice = Combiner_Gauche(matrice)
    matrice = Empiler_Gauche(matrice)
    matrice = Generateur_Tuile(matrice)
    Actualisation_Interface()
    Game_Over()


def Right_Button():
    global matrice
    matrice = Empiler_Droite(matrice)
    matrice = Combiner_Droite(matrice)
    matrice = Empiler_Droite(matrice)
    matrice = Generateur_Tuile(matrice)
    Actualisation_Interface()
    Game_Over()


def Up_Button():
    global matrice
    matrice = Empiler_Haut(matrice)
    matrice = Combiner_Haut(matrice)
    matrice = Empiler_Haut(matrice)
    matrice = Generateur_Tuile(matrice)
    Actualisation_Interface()
    Game_Over()


def Down_Button():
    global matrice
    matrice = Empiler_Bas(matrice)
    matrice = Combiner_Bas(matrice)
    matrice = Empiler_Bas(matrice)
    matrice = Generateur_Tuile(matrice)
    Actualisation_Interface()
    Game_Over()
    
            
    # Fonctions associées aux tests au cours du jeu

def Mouv_Hozizontale():
    """Regarde si on peut toujours se déplacer de manière horizontale"""
    for i in range (4):
        for j in range (1,3):
            if matrice[i][j] == matrice[i][j+1] or matrice[i][j] == matrice[i][j-1]:
                return True
    return False

def Mouv_Verticale():
    """Regarde si on peut toujours se déplacer de manière verticale"""
    for i in range (1,3):
        for j in range (4):
            if matrice[i][j] == matrice[i+1][j] or matrice[i][j] == matrice[i-1][j]:
                return True
    return False

def Zero_In_Mat():
    """Regarde s'il y a encore des espaces vides'"""
    for i in range(4):
        if 0 in matrice[i]:
            return True
    return False

def Game_Over():
    global end
    if any(2048 in row for row in matrice):
        end = 1
        Affich_Game_Over()
    elif Zero_In_Mat()==False and Mouv_Hozizontale()==False and Mouv_Verticale()==False: 
        end = 0
        Affich_Game_Over()
    else:
        pass

def Affich_Game_Over(): #//créer un fond tout blanc pour afficher winner ou looser
    Creation_Interface()
    Actualisation_Interface()
    if end==1:
        game_over_frame = tk.Frame(background, borderwidth=2)
        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(game_over_frame,
                 text="Gagné!",
                 bg=Fond_Gagnant,
                 fg=Police_Fin_Jeux_Couleur,
                 font=Police_Fin_Jeux).pack()
    elif end==0:
        game_over_frame = tk.Frame(background, borderwidth=2)
        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(game_over_frame,
                 text="Perdu!",
                 bg=Fond_Perdant,
                 fg=Police_Fin_Jeux_Couleur,
                 font=Police_Fin_Jeux).pack()
    else:
        pass
     
      
    # Boutons fonctionnement   
    
Start = tk.Button(text="Commencé", 
                    height=1, width=8,
                    font=("Helvetica", "10"),
                    command=Start_Button
                  )
Start.grid(row=0, column=0)

Exit = tk.Button(text="Quitter", 
                    height=1, width=8,
                    font=("Helvetica", "10"),
                    command=Exit_Button
                  )
Exit.grid(row=1, column=0)


Sauvegarde = tk.Button(text="Sauvegarde", 
                    height=1, width=8,
                    font=("Helvetica", "10"),
                    command=Sauvegarde_Button
                  )
Sauvegarde.grid(row=0, column=1)

Load = tk.Button(text="Charger", 
                    height=1, width=8,
                    font=("Helvetica", "10"),
                    command=Load_Button
                  )
Load.grid(row=1, column=1)


    # Boutons déplacement  
    
Haut = tk.Button(text="Haut", 
                    height=1, width=6,
                    font=("Helvetica", "10"),
                    command=Up_Button
                  )
Haut.grid(row=0, column=16)

Bas = tk.Button(text="Bas", 
                    height=1, width=6,
                    font=("Helvetica", "10"),
                    command=Down_Button
                  )
Bas.grid(row=2, column=16)


Gauche = tk.Button(text="Gauche", 
                    height=1, width=6,
                    font=("Helvetica", "10"),
                    command=Left_Button
                  )
Gauche.grid(row=1, column=15)

Droite = tk.Button(text="Droite", 
                    height=1, width=6,
                    font=("Helvetica", "10"),
                    command=Right_Button
                  )
Droite.grid(row=1, column=17)


    # Background
        
background = tk.Frame(racine, 
                bg=Couleur_Grille, 
                bd=3, width=570, 
                height=570
                ) 
                
background.grid(pady=40, columnspan=20) #columnspan=20 pour placer correctement les boutons


Creation_Interface()


racine.mainloop()
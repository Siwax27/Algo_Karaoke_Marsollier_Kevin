import random

class Player :
    def __init__(self, name, score):
        self.nom = name
        self.point = score
    def getname(self):
        return self.nom

    def getNombreJ(self):
        return self.chiffre 

class classement :
    def __init__(self, classement):
        self.tableau = classement 

class Chanson :
    def __init__(self, nombre, single):
        self.numero = nombre
        self.titre = single



def initializeList():
    l = []
    _input = input
    if hasattr(__builtins__, 'raw_input'):
        _input = raw_input
    while True:
        d = _input("--> ").strip()
        if d == '':
            break
        else:
            try:
                l.append(int(d))
            except ValueError:
                try:
                    l.append(float(d))
                except ValueError:
                    l.append(d)
    return l
 






#programme principale
NombreJ = int(input("combien de joueur veulent jouer ? \n"))#permet de savoir combien de joueurs il y aura 
JoueurActuel = NombreJ
print("il y a", JoueurActuel,"joueur") #dit le nombre de joueur
Joueur= initializeList() #permet de crée une list des pseudo de chaque joueur 
print(Joueur) #affiche la liste des pseudo des joueur
JoueurN = len(Joueur) 
ScoreMax = 100
ScoreMini = 50
if (len(Joueur) > JoueurActuel): #si un joueur a été ajouter en trop 
    choix=int(input("il y a un pseudo en trop ! voulez vous le garder ? 1 oui / 2 non")) #les joueurs choisit si il reste ou non 
    if (choix == 1): 
        print("le joueur peut rester !") #si les joueur choisisse qu'il reste rien ne change
    if (choix == 2): 
        print("vous venez de supprimer le pseudo")# si les joueur choississe de l'exclure alors le pseudo est supprimer
        del Joueur[len(Joueur)-1]
print(Joueur) 

chanson = [0,1,2,3,4] #nombre de chanson 
#le meilleur score de chaque chanson
chanson[0] = 78
chanson[1] = 50
chanson[2] = 64
chanson[3] = 99
chanson[4] = 56
choixM = int(input("veuillez choisir une chanson entre 0-4 : \n")) # permet au joueur de choisir la chanson 
if (choixM == 0):
    print("vous avez choisi la chanson : n°", choixM, ",le meilleur score sur cette chanson est : ",chanson[0]) #affiche le n° et le score de la première chanson

if (choixM == 1):
    print("vous avez choisi la chanson : n°", choixM, ",le meilleur score sur cette chanson est : ",chanson[1]) #affiche le n° et le score de la deuxième chanson

if (choixM == 2):
    print("vous avez choisi la chanson : n°", choixM, ",le meilleur score sur cette chanson est : ",chanson[2]) #affiche le n° et le score de la troisième chanson

if (choixM == 3):
    print("vous avez choisi la chanson : n°", choixM, ",le meilleur score sur cette chanson est : ",chanson[3]) #affiche le n° et le score de la quatrième chanson

if (choixM == 4):
    print("vous avez choisi la chanson : n°", choixM, ",le meilleur score sur cette chanson est : ",chanson[4]) #affiche le n° et le score de la cinquième chanson







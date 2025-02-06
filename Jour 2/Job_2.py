class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre    
        self.__auteur = auteur 
        self.__pages = pages  

    def getTitre(self):
        return self.__titre
    
    def setTitre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def getAuteur(self):
        return self.__auteur
    
    def setAuteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def getPages(self):
        return self.__pages
    
    def setPages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.__pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def afficher(self):
        return f"Titre : {self.__titre}\nAuteur : {self.__auteur}\nNombre de pages : {self.__pages}"

livre = Livre("Le Petit ", "Saint-Exupéry", 96)
print(livre.afficher())
livre.setPages(120)
print("\nAprès modification du nombre de pages :")
print(livre.afficher())
livre.setPages(-50)

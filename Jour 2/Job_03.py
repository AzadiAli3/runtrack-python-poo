class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre  # Attribut privé
        self.__auteur = auteur  # Attribut privé
        self.__pages = pages  # Attribut privé
        self.__disponible = True  # Attribut privé pour la disponibilité

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
        return f"Titre : {self.__titre}\nAuteur : {self.__auteur}\nNombre de pages : {self.__pages}\nDisponible : {self.__disponible}"
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():  # Vérifie si le livre est disponible
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.verification():  # Vérifie si le livre a été emprunté
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu.")
        else:
            print(f"Le livre '{self.__titre}' n'a pas été emprunté, donc il ne peut pas être rendu.")

livre = Livre("Le Petit", "Saint-Exupéry", 96)

print(livre.afficher())

livre.emprunter()
livre.emprunter()
livre.rendre()
print("\nAprès avoir rendu le livre :")
print(livre.afficher())
livre.rendre()
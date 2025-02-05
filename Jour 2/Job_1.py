class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def afficherDimensions(self):
        print(f"Longueur : {self.longueur}, Largeur : {self.largeur}")

    def changerLongueur(self, nouvelle_longueur):
        self.longueur = nouvelle_longueur

    def changerLargeur(self, nouvelle_largeur):
        self.largeur = nouvelle_largeur

rectangle = Rectangle(10, 5)
rectangle.afficherDimensions()
rectangle.changerLongueur(15)
rectangle.changerLargeur(8)
rectangle.afficherDimensions()

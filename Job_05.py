class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées de valeur sont ({self.x} ({self.y})")

    def afficherx(self):
        print(f"Valeur de x : {self.x}")

    def affichery(self):
        print(f"Valeur de y : {self.y}")

    def changerx(self, new_x):
        self.x = new_x
    
    def changery(self, new_y):
        self.y = new_y

point1 = Point(3, 5)

point1.afficherLesPoints()
point1.afficherx()
point1.affichery()

point1.changerx(7)
point1.changery(9)

point1.afficherLesPoints()
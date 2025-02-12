class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):

        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50 

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def __verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print(f"La voiture {self.__marque} {self.__modele} a démarré.")
        else:
            print("Le réservoir est trop vide pour démarrer. Veuillez faire le plein.")

    def arreter(self):
        self.__en_marche = False
        print(f"La voiture {self.__marque} {self.__modele} est arrêtée.")

    def afficher_info(self):
        print(f"Marque: {self.__marque}")
        print(f"Modèle: {self.__modele}")
        print(f"Année: {self.__annee}")
        print(f"Kilométrage: {self.__kilometrage} km")
        print(f"En marche: {'Oui' if self.__en_marche else 'Non'}")
        print(f"Réservoir: {self.__reservoir} litres")

ma_voiture = Voiture(" Porsche", "Taycan Sport Turismo", 2020, 15000)

ma_voiture.afficher_info()

ma_voiture.demarrer()

ma_voiture._Voiture__reservoir = 3 

ma_voiture.demarrer()

ma_voiture.arreter()

ma_voiture.afficher_info()
class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Résultat de l'addition: {resultat}")

operation1 = Operation()
print(operation1)

operation2 = Operation(5, 10)
print(operation2)

operation2.addition()

        
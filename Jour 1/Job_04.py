class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Bonjour, je m'appelle {self.prenom} {self.nom}."

personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupond")
personne3 = Personne("Azadi", "Ali")

print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())

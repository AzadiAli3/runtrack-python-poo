class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation_instance = Operation()

print(operation_instance)

print(f"Nombre1: {operation_instance.nombre1}, Nombre2: {operation_instance.nombre2}")
print("Valeur de nombre1:", operation_instance.nombre1)
print("Valeur de nombre2:", operation_instance.nombre2)


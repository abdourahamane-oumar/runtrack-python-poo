class operation:
    def __init__(self, nombre1=2, nombre2=8):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
      
    def addition(self):
        print("Le résultat de l'addition est:", self.nombre1 + self.nombre2 )

operation_instance = operation()

print("Le nombre1 est:", operation_instance.nombre1)
print("Le nombre2 est:", operation_instance.nombre2)
operation_instance.addition()
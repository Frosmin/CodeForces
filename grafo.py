class Perro:
    def __init__(self, nombre, raza,edad, tamnio):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamnio = tamnio
        
        
    def ladrar(self):
        print("Guau Guau")
        
    def decir_nombre(self):
        print("mi nombre es " + self.nombre)
        
pero_juan = Perro("Juan", "Pastor Aleman", 5, "Grande")
pero_juan.ladrar()
pero_juan.decir_nombre()
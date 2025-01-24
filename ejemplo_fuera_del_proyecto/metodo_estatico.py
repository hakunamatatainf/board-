class MiClase:
    def saludar(nombre):
        return f"Hola, {nombre}"


class MiClaseS:
    @staticmethod
    def saludar(nombre):
        return f"Hola, {nombre}"


s=MiClase
print(s.saludar("Javier"))

#llamar al método estático sin crear una instancia de la clase
print(MiClaseS.saludar("Javier"))
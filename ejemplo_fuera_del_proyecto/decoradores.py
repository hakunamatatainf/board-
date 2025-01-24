def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Suma, Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

def mi_decorador_resta(funcion):
    def nueva_funcion(a, b):
        print("Resta, Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

def valida_division_cero(funcion):
    def nueva_funcion(a, b):
        if b != 0:
            c = funcion(a, b)
            return c
        else:
            print("No se puede dividir por cero")
    return nueva_funcion

@mi_decorador
def suma(a, b): # esta es la funcion pasada al decorador
    print("Entra en funcion suma")
    print("suma ",a+b)
    return a + b

@mi_decorador_resta
def resta(a, b):
    print("Entra en funcion resta")
    print("resta ",a-b)
    return  a - b

@valida_division_cero
def divide(a, b):
    print("Entra en funcion division")
    print("division ",a/b)
    return  a/b

@valida_division_cero
def divide2(a, b):
    print("Entra en funcion division")
    print("division ",a/b)
    return  a/b

suma(5,8) # equivale a mi_decorador(suma(5,8))
resta(8,5)
divide(8,5)
divide(8,0)
divide2(10,0)
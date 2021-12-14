#calculadora con funciones

#Crear las funciones de las operaciones

def suma():

    num1 = int(input("Introduzca un numero a calcular: "))
    num2 = int(input("Introduzca otro numero, por favor: "))
    sumar = num1 + num2
    print('El resultado es: ',sumar)

def resta(num1, num2):

    num1 = int(input("Introduzca un numero a calcular: "))
    num2 = int(input("Introduzca otro numero, por favor: "))
    restar = num1 - num2
    print('El resultado es: ',restar)

def multiplicar(num1, num2):

    num1 = int(input("Introduzca un numero a calcular: "))
    num2 = int(input("Introduzca otro numero, por favor: "))
    mult = num1 * num2
    print ('El resultado es: ',mult)

def DivisionModulo(num1, num2):

    num1 = int(input("Introduzca un numero a calcular: "))
    num2 = int(input("Introduzca otro numero, por favor: "))
    mod = num1 % num2
    print ('El resultado es: ',mod)

def DivisionEntera(num1, num2):

    num1 = int(input("Introduzca un numero a calcular: "))
    num2 = int(input("Introduzca otro numero, por favor: "))
    div = num1 // num2
    print ('El resultado es: ',div)

#Crear un valor booleano para despues ejecutar la calculadora
ejecucion = True

while ejecucion:

    elegir = input("""Menu de la calculadora:
    1. sumar
    2. restar
    3. multiplicar
    4. Dividir con resultado en el resto
    5. Dividir con resultado en el cociente
    6. Salir
    Que operacion quieres realizar: """)

    if elegir == 1:
        suma()

    elif elegir == 2:
        resta()

    elif elegir == 3:
        multiplicar()

    elif elegir == 4:
        DivisionModulo()

    elif elegir == 5:
        DivisionEntera()

    elif elegir == 6:
        break

print ("Fin del programa, gracias por participar")
#calculadora
eleccion = True
while eleccion:
    num1 = int(input("Introduzca un numero, por favor: "))
    num2 = int(input("Introduzca otro numero, por favor: "))
    elegir = input("Elige una de las opciones para calcular:\n1. sumar\n2. restar\n3. multiplicar\n4. Dividir\n5. Salir\nQue operacion quieres realizar: ")
    if elegir == 1:
        sumar = num1 + num2
        print ("El resultado es:",sumar)
    elif elegir == 2:
        restar = num1 - num2
        print ("El resultado es: ",restar)
    elif elegir == 3:
        mul = num1 * num2
        print ("El resultado es: ",mul)
    elif elegir == 4:
        div = num1 / num2
        print ("El resultado es: ",div)
    elif elegir == 5:
        break
print ("Fin del programa de la calculadora")
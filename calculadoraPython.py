print("Bienvenido a la calculadora con Python ")
print('Para salir deber poner "salir" ')
PrimerNumero = input("ingrese un numero ")
while True:
    PrimerNumero = int(PrimerNumero)
    if PrimerNumero == int(PrimerNumero):
        print("Las operaciones diponibles son: Suma, Resta, Multi, Div")
        operacion = input("Elija la operacion ").lower()
        if operacion == "salir":
            print("hasta la proxima ")
            break
        if operacion not in ("suma", "resta", "multi", "div"):
            print("No es una operacion valida")
            continue
    segundo_numero = int(input("Ingrese el segundo numero "))

    if operacion == "suma":
        resultado = PrimerNumero+segundo_numero
        print(resultado)
    elif operacion == "resta":
        resultado = PrimerNumero-segundo_numero
        print(resultado)
    elif operacion == "div":
        resultado = PrimerNumero/segundo_numero
        print(resultado)
    elif operacion == "multi":
        resultado = PrimerNumero*segundo_numero
        print(resultado)
    PrimerNumero = resultado

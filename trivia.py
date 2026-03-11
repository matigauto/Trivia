
puntos = 0
puntos2 = 0
putnos3 = 0
print('------------------------------SUPER TRIVIA DE OLAF---------------------------------')
def hacer_pregunta(pregunta, respuesta_correcta):
    respuesta = input(pregunta + " ")

    if respuesta == respuesta_correcta:
        print("Correcto")
        return 1
    else:
        print("Incorrecto")
        return 0

puntos = hacer_pregunta("¿Capital del pais de olaf?", "olaf")
puntos2 = hacer_pregunta("¿Como es el pelo de olaf?", "olaf")
puntos3 = hacer_pregunta("¿Animal rey de la selva?", "olaf")

print("Tu puntaje final es:", puntos + puntos2 + puntos3)






























""" Calcula la edad en dias """

#función  que calcula la edad y convertirá en dias
def calcDias(edad):
    anos = int(edad) #Edad en años
    meses = int(edad) * 12 #Edad en meses
    dias = int(edad) * 365 #Edad en dias

    print("Ya ha vivido ",anos, "años") #Mostrando la edad en años
    print("Ya ha vivido ", meses, "meses") #Mostrando la edad en meses

    return dias #devuelve la edad en dias

edad = int(input("¿Cual tu edad? ")) #informando la edad
total = calcDias(edad) #llamando la función para calcular la edad en dias

print("Tú ya ha vivido ", total,"dias")#mostrando la edad en dias

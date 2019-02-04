"""Calculando área de um retângulo e dobrando seu valor!!!"""

#função que calculará a área do quadrado
def quadrado(l1, l2):
    area = float(l1 * l2) #formula para calcular a área de um quadrado
    return area #retornando o valor de area

#função que dobrará o valor da área do quadrado
def dobro(a):
    dobrar = float(a * 2) #formula para dobrar a área do quadrado
    return dobrar #retornando o valor em dobro

l1 = float(input("LADO 1 = ")) #informando o primeiro lado do quadrado
l2 = float(input("LADO 2 = ")) #informando o segundo lado do quadrado

a = quadrado(l1,l2) #chamando a função para calcular a área
print("\n Área do quadrado = ", a, "m") #exibindo o valor de área

d = dobro(a) #chamando a função para calcular o dobro da área
print("\n Dobro da área = ", d, "m") #exibindo o valor da área em dobro

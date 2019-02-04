"""Calculando e mostrando o salário no referido mês"""

###Convertendo os dias trabalhados em horas
def diasTrabalhados(ht):
    horas = float(ht * 8) ###Formula para a conversão
    return horas ###retornando o valor de horas trabalhadas

###Calculando o salário bruto no mês
def salarioBruto(horas, sh):
    total = float(sh * horas)###Formula para calcular o salário
    return total ###retornando o valor de salário bruto

sh = float(input("Salário por hora: ")) ###informar o quanto ganha por hora
ht = float(input("Dias trabalhados: ")) ###informar os dias trabalhados

horas = diasTrabalhados(ht) ###chamando a função para converter dias em horas
sb = salarioBruto(horas, sh) ###chamando a função para calcular o salário

print("Horas trabalhadas ", horas, "hs") ###exibindo as horas trablhadas
print("Salário R$",sb) ###exibindo salário

"""Convertendo m em cm"""

#função que converterá a medida em cm
def metros(m):
    conversao = m * 100 #formula da conversão

    return conversao #retornando o valor obitdo pelo calculo

m = int(input("Informe o valor em metros: "))#informando a medida em metros
c = metros(m)#chamando a função para fazer a conversçao de m em cm

print(c, "cm")#exibindo o valor

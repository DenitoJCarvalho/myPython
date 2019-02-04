""" Calculando o valor final de carro novo ao consumidor final"""

def  custoFinal(cf):
    dist = cf * 0.28
    imposto = cf * 0.45
    valorFinal = cf + dist + imposto

    return valorFinal

cf = float(input("Informe o custo de fábrica: R$"))
cn = custoFinal(cf)
dif = cn - cf

print("Valor de carro ao consumidor = R$",cn)
print("Total de imposotso R$",dif)



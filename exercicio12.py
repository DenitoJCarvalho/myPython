""" Calculando o reajuste que o funcionário receberá """

#função para calcular o rajuste e o novo salário
def novoSalario(sla):
    reaj = sla * 0.12 ###calculando o reajuste
    nsla = sla + reaj ###somando o salário antigo ao reajuste

    return nsla ###retornando o novo salário


sla = (float(input("Salário atual: R$")))###informando o salário atual

novoSal = novoSalario(sla) ###chamando a função para calcular o novo salário
print("Novo salário R$",round(novoSal, 2)) ###exibindo novo salário

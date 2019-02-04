""" Calculando el salario de los vendedores"""

sal = float(input("Salário Fijo R$"))#informando salario fijo
carVend = int(input("Cantidad de coches vendidos "))#informando la cantidad de coches vendidos

#função que calculará o salário do vendedor no final do mês
def vendasTotalCarros(sal, carVend):
    valores = [] #array que almacenará los valores de coche
    porVenda = [] #array que almacenará las comisiones a la cada venda
    i = 0 #contador

    #loop que introducirá el valor a cada venda de acuerdo con la cantidad
    #de coche vendido informado
    while i < carVend:
        n = float(input("Valor de coche R$")) #informandolos valores de los coches
        valores.append(n) #añadiendo los valores  a la array valores
        total = sum(valores) # somando los valores de la array

        pv = n * 0.05 #calculando los 5%
        porVenda.append(pv) #añadiendo las comisiones a la array porVendas
        comPorVendas = sum(porVenda) #somando los valores de la array

        i = i + 1 #pasando un paso de acuerdo con la variable carVend

    comFixo = total * 0.10 #calculando lso 10% fijos
    salFinal = sal + comPorVendas + comFixo #calculando el salario del mes
        
    print("\nSalario fijo R$", sal) #mostrando el salaario fijo
    print("Total de las vendas R$",total) #mostrando los totales de las vendas
    print("Comisión por las vendas R$", comPorVendas) #mostrando la comisión poor vendas
    print("Comisión fija R$",comFixo) #mostrando la comisión fija
    print("Tu salario en el mes sera R$",salFinal) #mostrando salario final
    
vendasTotalCarros(sal, carVend) #llamando la función para calcular comisón fija,
#comisión por las vendas, total de las vendas y salario final 








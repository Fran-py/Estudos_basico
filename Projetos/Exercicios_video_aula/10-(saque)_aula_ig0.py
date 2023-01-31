"""saque = int(input('Informe o valor do saque: '))

#notas de 1, 5, 10, 50 e 100

while  saque>10 and saque<600:

    nota_1 = saque // 1
    nota_5 = saque // 5
    nota_10 = saque // 10
    nota_50 = saque // 50
    nota_100 = saque // 100

    if 1 <= nota_100 < nota_50:
       print(f'Voce vai receber {nota_100} notas de 100 reais')
  
    elif nota_10 > nota_50 >=1:
       print(f'voce vai receber {nota_50} notas de 50 reais')

    else:
       print(f'voce vai receber {nota_10} notas de 10 reais')

    resto_100 = saque % 100
    resto_50 = saque % 50
    resto_10 = saque % 10
    
    notas10_do_resto100 = resto_100//10
    notas5_do_resto100 = resto_100%10 // 5
    notas1_do_resto100 = (resto_100%10) %5 
    notas1_do_resto100_menorque5 = resto_100%10

    if 5>resto_100:
       print('voce vai receber tambem',resto_100,'notas de 1 real')

    elif resto_100==5:
       print('Voce vai receber tambem 1 nota de',resto_100,'reais')
    
    elif 5<resto_100<10

    
   



       
       
    
       
       
       
       
    
       
       
    break









else:
   print('digite um valor valido')

"""

saque = int(input("Digite o valor do saque: "))

if 10 <= saque <= 600:
    notas_cem = saque // 100
    saque = saque % 100

    notas_cinquenta = saque // 50
    saque = saque % 50

    notas_dez = saque // 10
    saque = saque % 10

    notas_cinco = saque // 5
    saque = saque % 5

    notas_um = saque // 1

    if notas_cem > 0:
        print(notas_cem, "notas de R$ 100")
    if notas_cinquenta > 0:
        print(notas_cinquenta, "notas de R$ 50")
    if notas_dez > 0:
        print(notas_dez, "notas de R$ 10")
    if notas_cinco > 0:
        print(notas_cinco, "notas de R$ 5")
    if notas_um > 0:
        print(notas_um, "notas de R$ 1")
              
else:
    print("Nao é possivel fazer o saque")


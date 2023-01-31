valor = int ( input ("Introduza o valor que queres levantar: ") )

notasDeCem = valor // 100
notasDeCinquenta = ( valor % 100 ) // 50
notasDeDez = ( valor % 50 ) // 10
notasDeCinco = ( valor % 10 ) // 5
notasDeUm = ( valor % 5 ) // 1

print(valor%100)
#Verifica se o valor digitado é positivo
if ( valor < 1 ):
    print("Introduza valores válidos")
#Verifica se o valor digitado não é superior à 600
if valor <= 600:
    #Mostra as notas de cem
    if notasDeCem % 1 == 0:
        if notasDeCem != 0: 
            print( notasDeCem, "nota(s) de 100" )
        else:
            print( )
    #Mostra as notas de cinquenta
    if notasDeCinquenta % 1 == 0:
        if notasDeCinquenta != 0:
            print( notasDeCinquenta, "nota(s) de 50" )
        else:
            print( )   
    #Mostra as notas de dez
    if notasDeDez % 1 == 0:
        if notasDeDez != 0:
            print( notasDeDez, "nota(s) de 10" )
        else:
            print( )
    #Mostra as notasDeUms
    if notasDeCinco % 1 == 0:
        if notasDeCinco != 0:
            print( notasDeCinco, "nota(s) de 5" )
        else:
            print( )
    #Mostra as notasDeUms
    if notasDeUm % 1 == 0:
        if notasDeUm != 0:
            print( notasDeUm, "nota(s) de 1" )
        else:
            print( )
else:
    print( "Valor excedido" )






    









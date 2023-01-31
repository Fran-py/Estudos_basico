numero = int(input('Digite um numero: '))

if numero < 1000:

    numero_alterado = list(str(numero))
    print(len(numero_alterado))
    
    if len(numero_alterado) == 3:
        centena = numero_alterado[0]
        dezena = numero_alterado[1]
        unidade = numero_alterado[2]

        print(f'O numero possui {centena} centenas, {dezena} dezenas e {unidade} unidades')

    elif len(numero_alterado) == 2:
        dezena = numero_alterado[0]
        unidade = numero_alterado[1]

        print(f'O numero possui {dezena} dezenas e {unidade} unidades')

    else:
        unidade = numero_alterado[0]

        print (f'O numero possui {unidade} unidades')



    




    """centenas = numero // 100
    numero = numero % 100

    dezenas = numero // 10
    numero = numero % 10

    unidades = numero // 1

    if centenas > 0 and dezenas >0 and unidades > 0:
        print(f'{numero_alterado} possui {centenas} centenas, {dezenas} dezenas e {unidades} unidades')

    elif centenas > 0 and dezenas >0 and unidades == 0:
        print(f'{numero_alterado} possui {centenas} centenas, e {dezenas} dezenas')

    elif centenas > 0 and dezenas == 0 and unidades > 0:
        print(f'{numero_alterado} possui {centenas} centenas, e {unidades} unidades')

    elif centenas > 0 and dezenas == 0 and unidades == 0:
        print(f'{numero_alterado} possui {centenas} centenas')

    elif centenas == 0 and dezenas > 0 and unidades > 0:
        print(f'{numero_alterado} possui {dezenas} dezenas, e {unidades} unidades')

    elif centenas == 0 and dezenas > 0 and unidades == 0:
        print(f'{numero_alterado} possui {dezenas} dezenas')

    else:
        print (f'{numero_alterado} possui {unidades} unidades')"""
    
else:
    print ('Informe um numero válido')





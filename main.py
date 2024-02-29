while True:
    print()
    primeiro_numero_str = input('Digite o primeiro número: ')
    print()

    if primeiro_numero_str == '':
        print('Por favor, insira alguma infomação.')
        print()
        continue

    if not primeiro_numero_str.isdigit():
        print('Por favor, digite apenas números inteiros.')
        continue


    segundo_numero_str = input('Digite o segundo número: ')
   
    if segundo_numero_str == '':
        print('Por favor, insira alguma infomação.')
        print()
        continue

    if not segundo_numero_str.isdigit():
        print('Por favor, digite apenas números inteiros.')
        continue

    print()
    primeiro_numero = int(primeiro_numero_str)
    print()
    segundo_numero = int(segundo_numero_str)
    print()

    print('   +  ,  -  , *  ,  /  ')
    print()

    operadores = input('ESCOLHA UM OPERADOR ACIMA: ')

    if operadores == '+':
        calculo  = primeiro_numero + segundo_numero
        print('O resultado é: ', calculo)

    elif operadores == '-':
        calculo  = primeiro_numero - segundo_numero
        print('O resultado é: ', calculo)
    
    elif operadores == '*':
        calculo  = primeiro_numero * segundo_numero
        print('O resultado é: ', calculo)

    elif operadores == '/':
        if segundo_numero != 0:
            calculo  = primeiro_numero / segundo_numero
            print('O resultado é: ', calculo)
        
        else:
            print('ZERO NÃO É UM NÚMERO DIVISIVEL!!!')

    
    elif operadores != '+' and '-' and '*' and '/':
        print('Por favor, digite apenas operadores validos.')


    
    continuar = input('Deseja continuar o calculo? (s/n): ')

    if continuar.lower() != 's' and 'S':
        break

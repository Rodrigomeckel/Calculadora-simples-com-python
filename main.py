while True:

    print()

    primeiro_numero_str = input('Digite o primero número: ')
   
    if primeiro_numero_str == '':
        print('Por favor, insira alguma informação.')
        continue

    print()

    segundo_numero_str  = input('Digite o segundo número: ').strip()

    if segundo_numero_str == '':
        print('Por favor, insira alguma informação.')
        print()
        segundo_numero_str = input('Digite o Segundo número novamente: ').strip()
    print()

    try:
        print()
        primeiro_numero = int(primeiro_numero_str)
        print()
        segundo_numero  = int(segundo_numero_str)
        print()
    
    except ValueError:
        print('Apenas números inteiros são válidos!')
        continue

    print('   + , - , * , / ')
    print()

    operador  = input('ESCOLHA UM OPERADOR ACIMA: ')
    print()

    if operador == '+':
        calculo = primeiro_numero + segundo_numero
        print('O resutado é: ', calculo)
        print()
        
    elif operador == '-':
        calculo = primeiro_numero - segundo_numero
        print('O resutado é: ', calculo)
        print()

    elif operador == '*':
        calculo = primeiro_numero - segundo_numero
        print('O resutado é: ', calculo)
        print()

    elif operador == '/':

        if segundo_numero != 0:
            calculo = primeiro_numero / segundo_numero
            print('O resutado é: ', calculo)
            print()
        
        else:
            print('ZERO NÃO É UM NÚMERO DIVISIVEL!!')
            print()

    elif operador != '+' and '-' and '*' and '/':

        print('Escolha um operador válido!')
        print()
        operador = input('Digite o operador novamente: ')
        print()

        if operador == '+':
            calculo = primeiro_numero + segundo_numero
            print('O resutado é: ', calculo)
            print()
        
    elif operador == '-':
        calculo = primeiro_numero - segundo_numero
        print('O resutado é: ', calculo)
        print()

    elif operador == '*':
        calculo = primeiro_numero - segundo_numero
        print('O resutado é: ', calculo)
        print()

    elif operador == '/':

        if segundo_numero != 0:
            calculo = primeiro_numero / segundo_numero
            print('O resutado é: ', calculo)
            print()
        
        else:
            print('ZERO NÃO É UM NÚMERO DIVISIVEL!!')
            print()


    continuar = input('Deseja continuar o calculo? (s/n): ')
    print()

    if continuar.lower() != 's' and 'S':
        break

    




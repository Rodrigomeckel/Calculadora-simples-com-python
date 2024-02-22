while True:
    print()
    primero_numero_str = input('Digite o primero número: ')
    print()
    
    if primero_numero_str == '':
        print('O primero número esta vazio!!')
        print()
        continue
    
    segundo_numero_str = input('Digite o segundo número: ').strip()
    print()

    if segundo_numero_str == '':
        print('O segundo número esta vazio!!')
        print()
        segundo_numero_str = input('Digite novamente o segundo número: ').strip()
        

    try:
   
        print()
        primero_numero = int(primero_numero_str)
        print()
        segundo_numero = int(segundo_numero_str)
        print()
    
    except ValueError:
        print('Entrada inválida, Por favor, digite um número inteiro')
        continue
        
        

    print('        + , - , * , / ')
    print()

    operadores = input('ESCOLHA UM DOS OPERADORES ACIMA: ')
    print()

    if operadores == '+': 

        calculo = primero_numero + segundo_numero

        print('A resposta é: ', calculo)
        print()

    elif operadores == '-':

        calculo = primero_numero - segundo_numero

        print('A resposta é: ', calculo)
        print()

    elif operadores == '*':

        calculo = primero_numero * segundo_numero

        print('A resposta é: ', calculo)
        print()

    elif operadores == '/':

        if segundo_numero != 0:
            
            calculo = primero_numero / segundo_numero
            
            print('A resposta é: ', calculo)
            print()
        
        else:
            
            print('ZERO NÃO É UM NÚMERO DIVISIVEL!!')
            print()

    elif operadores != '+' and '-' and '*' and '/':
        
        print('ESCOLHA UM OPERADOR!!')
        print()

    else:
        print('ESCULHA UM OPERADOR!!!')
        print()

    
    continuar = input('Deseja continuar o calculo? (s/n): ')

    if continuar.lower() != 's' and 'S':
        break
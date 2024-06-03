menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

saldo = 0
LIMITE_VALOR_SAQUE = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input('Digite o valor que quer depositar: '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
        else:
            print('Depósito não concluído. Valor inválido!')
    
    elif opcao == 's':
        valor_saque = float(input('Digite o valor do saque: '))

        excedeu_saldo = valor_saque > saldo
        excedeu_valor_saque = valor_saque > LIMITE_VALOR_SAQUE
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação não concluída. Saldo insuficiente!')
        
        elif excedeu_valor_saque:
            print('Operação não concluída. Você excedeu o valor máximo para saque!')

        elif excedeu_saque:
            print('Operação não concluída. Você excedeu o número máximo de saque!')

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f'Saque: R$ {valor_saque:.2f}\n'
            numero_saques += 1

        else:
            print('Operação não concluída. Valor inválido!')

    elif opcao == 'e':
        texto_extrato = ' EXTRATO '
        print(texto_extrato.center(41, '='))
        print('Não foram realizadas movimentações!' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('================================')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida! Por favor, selecione novamente a operação desejada.')
#Funções
def cadastrar_peca(codigo):
    # Cadastra uma peça
        try:
            print('Bem Vindo à Área de Cadastro de Peças')
            nome= input('Insira o nome da peça: ')
            fabricante = input('Insira o fabricante da peça: ')
            valor = float(input('Informe o valor da peça: '))
            dic_peca = {'Nome': nome,
                        'Fabricante': fabricante,
                        'Valor': valor,
                        'Código': codigo}
            dic_peca['Código'] += 1
            lista_pecas.append(dic_peca.copy())
            return 'Cadastro Realizado com Sucesso'
        except ValueError:
            return 'Opção inválida, tente novamente'   

def consultar_peca():
    # consulta as peças cadastradas
    while True:
        try:
            print('Bem Vindo à Área de Consulta de Peças')
            op_consulta = int(input('\nEscolha sua opcao:'
                                    '\n1 - Consultar Todas as Peças'
                                    '\n2 - Consultar Peças por Código'
                                    '\n3 - Consultar Peças por Fabricante'
                                    '\n4 - Retornar'
                                    '\n>> '))
            print()                        
            if op_consulta == 1:
                for peca in lista_pecas:
                    for key, value in peca.items():
                        if key == 'Valor':
                            print('{}: R$ {:.2f} '.format(key, value))
                        else:
                            print('{}: {} '.format(key, value))
                    print()  
            elif op_consulta == 2:
                entrada = int(input('Insira o codigo da peça: '))
                if entrada <= codigo:
                    print()
                    for peca in lista_pecas:
                        if peca['Código'] == entrada:
                            for key,value in peca.items():
                                if key == 'Valor':
                                    print('{}: R$ {:.2f} '.format(key, value))
                                else:
                                    print('{}: {} '.format(key, value))
                            print()
                else:
                    print('Código inexistente, por favor, tente novamente\n')                           
            elif op_consulta == 3:
                entrada = (input('Insira o fabricante da peça: '))
                print()
                for peca in lista_pecas:
                    if peca['Fabricante'] == entrada:
                        for key, value in peca.items():
                                if key == 'Valor':
                                    print('{}: R$ {:.2f} '.format(key, value))  
                                else:
                                    print('{}: {} '.format(key, value))
                        print()     
            elif op_consulta == 4:
                break
            else:
                print('Opção inválida, tente novamente\n')
        except ValueError:
            print('Opção inválida, tente novamente\n')

def remover_peca():
    # Remove Peças do Cadastro
    print('Bem Vindo à Área de Remoção de Peças')
    entrada = int(input('Insira o codigo da peça: '))
    for peca in lista_pecas:
        if peca['Código'] == entrada:
            lista_pecas.remove(peca)
            print('Peça Removida com Sucesso\n')
        else: 
            print('Código inexistente, por favor, tente novamente\n')

#Menu Principal
codigo = 0
lista_pecas = []

while True:
    try:
        print('Bem Vindo ao Sistema de Controle de Estoque do Will')
        opcao = int(input('\nEscolha sua opcao:'
                        '\n1 - Cadastrar Peça'
                        '\n2 - Consultar Peça'
                        '\n3 - Remover Peça'
                        '\n4 - Sair'
                        '\n>> '))
        print()                
        if opcao == 1:
            cadastro = cadastrar_peca(codigo)
            if cadastro == 'Cadastro Realizado com Sucesso':
                codigo += 1
                print(cadastro)
            else:
                print('Opção inválida, tente novamente')
        elif opcao == 2:
            consultar_peca()
        elif opcao == 3:
            remover_peca()
        elif opcao == 4:
            print('Encerrando Programa...')
            break
        else:
            print('Opção inválida, tente novamente')
    except ValueError:
        print('Opção inválida, tente novamente')

        













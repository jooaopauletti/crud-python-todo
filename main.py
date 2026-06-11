import json

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    except:
        return []

def salvar_tarefas():
    with open('tarefas.json', 'w') as arquivo:
        json.dump(lista_tarefas, arquivo)

lista_tarefas = carregar_tarefas()

while True:
    print('==== TO DO LIST ====')
    print('1. Adicionar tarefas')
    print('2. Ver tarefas')
    print('3. Atualizar tarefas')
    print('4. Deletar tarefa')
    print('5. Sair')
    print('=' * 20)
    opcao_usuario = input('Escolha o número desejado: ')

    # CREATE
    if opcao_usuario == "1":
        print('Opção escolhida -> Adicionar tarefas')
        nova_tarefa = input('Qual tarefa você deseja acrescentar?: ')
        lista_tarefas.append(nova_tarefa)
        salvar_tarefas()
        print('Item adicionado na lista!')
        print(lista_tarefas)
        
    # READ
    elif opcao_usuario == "2":
        print('Opção escolhida -> Ver tarefas')
        print('==== SUAS TAREFAS ====')
        for numero, tarefa in enumerate(lista_tarefas, 1):
            print(numero, tarefa)
     
    # UPDATE  
    elif opcao_usuario == "3":
        print('Opção escolhida -> Atualizar tarefas')
        try:   
            for numero, tarefa in enumerate(lista_tarefas, 1):
                print(numero, tarefa)
            atualizar_tarefa = int(input('Qual tarefa você deseja atualizar? Selercionar apenas o NÚMERO: '))
            novo_item = input('Qual o novo item da lista de tarefas? ')
            lista_tarefas[atualizar_tarefa - 1] = novo_item
            salvar_tarefas()
            print(novo_item)
            print('Item atualizado com sucesso! ')
        except:
            print('Erro encontrado, digite apenas um número.')

    # DELETE
    elif opcao_usuario == "4":
        print('Opção escolhida -> Deletar tarefa')
        try:
            for numero, tarefa in enumerate(lista_tarefas, 1):
                print(numero, tarefa)
            remover_tarefa = int(input('Qual tarefa você deseja remover? Selecionar apenas o NÚMERO: '))
            lista_tarefas.pop(remover_tarefa - 1)
            salvar_tarefas()
            print('Tarefa removida!')
        except:
            print('Erro encontrado, digite apenas um número.')
        
    elif opcao_usuario == "5":
        print('Sair')
        break
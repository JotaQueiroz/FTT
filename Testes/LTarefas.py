import os, time

# Lista para inclusão de tarefas
Tarefas = []

# Função para adcionar tarefas a lista
def adicionar():
    os.system("cls")
    add = input("Qual tarefa deseja adicionar? ")
    os.system("cls")
    Tarefas.append(add)
    print(f"\033[32mTarefa:'{add}', adicionado com sucesso!\033[m")
    time.sleep(1.5)
    os.system("cls")


# Função para listar as tarefas   
def listar():
    os.system("cls")
    print("LISTA DE TAREFAS:")
    print("-"*17)
    if len(Tarefas) == 0:
        print("Você não possue nenhuma tarefa na sua lista.")
        print("Adicione tarefas à sua lista na opção '1'")

    else:
        for i, add in enumerate(Tarefas, start = 1):
            print(f"\033[33m{i} - {add}\033[m")
    print("-"*17)

# Função para excluir as tarefas        
def excluir():
    listar()
    select = int(input("Escolha o número de qual tarefa deseja excluir: ")) - 1
    
    if 0 <= select < len(Tarefas):
        remove = Tarefas.pop(select)
        os.system("cls")
        print("\033[31mTarefa removida com sucesso!\033[m")
        time.sleep(1.5)
        os.system("cls")
    else:
        print("Escolha inexistente!")

# Laço infinito para as opções com 'break' para sair        
while True:
    print("\nOpções:")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Excluir tarefa")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        excluir()
    elif opcao == '4':
        break
    else:
        print("Opção invalida!")
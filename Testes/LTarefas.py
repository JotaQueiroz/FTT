# Lista para inclusão de tarefas
Tarefas = []

# Função para adcionar tarefas a lista
def adicionar():
    add = input("Qual tarefa deseja adicionar? ")
    Tarefas.append(add)
    print(f"Tarefa:'{add}', adicionado com sucesso!")

# Função para listar as tarefas   
def listar():
    print("Lista de Tarefas:")
    print("-"*17)
    for i, add in enumerate(Tarefas, start = 1):
        print(f"{i} - {add}")
    print("-"*17)

# Função para excluir as tarefas        
def excluir():
    listar()
    select = int(input("Escolha o número de qual tarefa deseja excluir: ")) - 1
    
    if 0 <= select < len(Tarefas):
        remove = Tarefas.pop(select)
        print("Tarefa removida com sucesso!")
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
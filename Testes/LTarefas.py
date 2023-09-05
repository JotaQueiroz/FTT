Tarefas = []

def adicionar():
    add = input("Qual tarefa deseja adicionar?")
    Tarefas.append(add)
    print(f"Tarefa:'{add}' adicionado com sucesso!")
    
def listar():
    print("Lista de Tarefas:")
    print("-"*17)
    for i, add in enumerate(Tarefas):
        print(f"(i), {add}")
        
def excluir():
    listar()
    select = int(input("Escolha o número de qual tarefa deseja excluir: ")) - 1
    
    if 0 <= select < len(Tarefas):
        remove = Tarefas.pop(select)
        print("Tarefa removida com sucesso!")
    else:
        print("Escolha inexistente!")
        
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
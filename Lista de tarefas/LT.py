import sqlite3

# Função para criar a tabela de tarefas
def criar_tabela():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            concluida BOOLEAN
        )
    """)
    conexao.commit()
    conexao.close()

# Função para adicionar uma nova tarefa
def adicionar_tarefa(descricao):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tarefas (descricao, concluida) VALUES (?, ?)", (descricao, False))
    conexao.commit()
    conexao.close()

# Função para listar todas as tarefas
def listar_tarefas():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas

# Função para marcar uma tarefa como concluída
def marcar_tarefa_concluida(tarefa_id):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE tarefas SET concluida = ? WHERE id = ?", (True, tarefa_id))
    conexao.commit()
    conexao.close()

# Função principal
def main():
    criar_tabela()

    while True:
        print("\nLista de Tarefas:")
        tarefas = listar_tarefas()
        for tarefa in tarefas:
            tarefa_id, descricao, concluida = tarefa
            status = "Feita" if concluida else "Pendente"
            print(f"{tarefa_id}: {descricao} ({status})")

        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Marcar Tarefa como Concluída")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(descricao)
        elif opcao == "2":
            tarefa_id = int(input("Digite o ID da tarefa que deseja marcar como concluída: "))
            marcar_tarefa_concluida(tarefa_id)
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

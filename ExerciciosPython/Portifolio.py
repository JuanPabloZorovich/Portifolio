def adicionar_tarefa(lista, tarefa):
    lista.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa(lista, tarefa):
    if tarefa in lista:
        lista.remove(tarefa)
        print(f"Tarefa '{tarefa}' removida com sucesso!")
    else:
        print(f"Tarefa '{tarefa}' não encontrada na lista.")

def exibir_tarefas(lista):
    if not lista:
        print("A lista de tarefas está vazia.")
    else:
        print("\n--- Tarefas na Lista ---")
        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}. {tarefa}")

def main():
    lista_de_tarefas = []

    while True:
        print("\n=== Lista de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Exibir Tarefas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa a ser adicionada: ")
            adicionar_tarefa(lista_de_tarefas, tarefa)
        elif opcao == "2":
            tarefa = input("Digite a tarefa a ser removida: ")
            remover_tarefa(lista_de_tarefas, tarefa)
        elif opcao == "3":
            exibir_tarefas(lista_de_tarefas)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

import xlsxwriter
import os
def adicionar_lista():
    lista_junta = []
    lista_separada = []
    while True:
            item = input("Digite o item que você deseja adicionar ou aperte (4) para sair: ")
            if item == '4':
                break
            elif " " in item:
                lista_junta = list((item.split()))    
            else:
                lista_separada.append(item)
            lista = lista_separada + lista_junta
    return lista
def remover_lista(lista):
    while True:
            remover = input("Digite o item que você deseja remover ou aperte (4) para sair: ")
            while remover not in lista and remover != '4':
                print("\nParece que o item que você está tentando remover não está na lista, tente novamente: ")
                remover = input("Digite o item que você deseja remover ou aperte (4) para sair: ")
                if remover == '4':
                    break
            if remover == '4':
                break
            else:
               lista.remove(remover)
               print("\nItem removido com sucesso!")
    return lista
def mostrar_lista(lista):
    print(f"Aqui está sua lista: {lista}")
def menu():
    lista_backup = []
    while True:
        print("Bem-vindo ao Menu Lista de Compras!")
        print("\nAperte: (1) Para Adicionar um item à lista. (2) Para Remover um item da lista. (3) Para Mostrar a Lista e (4) Para Sair.")
        op = int(input("Digite a opção desejada: "))
        if op == 1:
            nova_lista = adicionar_lista()
            nova_lista.extend(lista_backup)
        elif op == 2:
            remover_lista(nova_lista)
        elif op == 3:
            mostrar_lista(nova_lista)
        elif op == 4:
            print("Encerrando...")
            break
        lista_backup = nova_lista
    return nova_lista
def salvar_lista():
    caminho = "" # Aqui você deve alterar o caminho do arquivo para o desejado
    criar_planilha = xlsxwriter.Workbook(caminho)
    sheet1 = criar_planilha.add_worksheet()
    minha_lista = menu()
    sheet1.write("A1", "Produto")
    for i in range(len(minha_lista)):
        sheet1.write(f"A{i+2}", minha_lista[i])
    criar_planilha.close()
    os.startfile(caminho)
    print("Lista salva com sucesso!")
salvar_lista()
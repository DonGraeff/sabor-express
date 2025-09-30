import os

restaurantes_cadastrados = []


def mostrar_subtitulo(texto):
    os.system("cls")
    print(f"\n{'=' * 20}")
    print(f"Sabor Express - {texto}")
    print(f"{'=' * 20}\n")


def limpar_tela():
    input("\nPressione Enter para continuar...")
    os.system("cls")


def cadastrar_restaurante():
    mostrar_subtitulo("Cadastrar Restaurante")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")

    for restaurante in restaurantes_cadastrados:
        if restaurante["nome"].lower() == nome_do_restaurante.lower():
            print(
                f"\nO restaurante '{nome_do_restaurante}' já está cadastrado. Tente outro nome."
            )
            limpar_tela()
            return

    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "categoria": categoria,
        "ativo": False,
    }
    restaurantes_cadastrados.append(dados_do_restaurante)
    print(f"\nO restaurante '{nome_do_restaurante}' foi cadastrado com sucesso!")
    limpar_tela()


def listar_restaurantes():
    mostrar_subtitulo("Listar Restaurantes")

    if not restaurantes_cadastrados:
        print("Nenhum restaurante cadastrado.")
    else:
        print(f"{'Nome'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
        print("-" * 65)
        for restaurante in restaurantes_cadastrados:
            nome_restaurante = restaurante["nome"]
            categoria_restaurante = restaurante["categoria"]
            if restaurante["ativo"]:
                status = "Ativado"
            else:
                status = "Desativado"
            print(
                f"{nome_restaurante.ljust(22)} | {categoria_restaurante.ljust(20)} | {status}"
            )
    limpar_tela()


def ativar_restaurante():
    mostrar_subtitulo("Ativar/Desativar Restaurante")
    nome_restaurante_input = input(
        "Digite o nome do restaurante para ativar/desativar: "
    )
    restaurante_encontrado = False

    for restaurante in restaurantes_cadastrados:
        if restaurante["nome"].lower() == nome_restaurante_input.lower():
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            if restaurante["ativo"]:
                status_novo = "ativado"
            else:
                status_novo = "desativado"
            print(
                f"\nO restaurante '{restaurante['nome']}' foi {status_novo} com sucesso!"
            )
            break

    if not restaurante_encontrado:
        print(f"\nO restaurante '{nome_restaurante_input}' não foi encontrado.")

    limpar_tela()


def menu_principal():
    while True:
        os.system("cls")
        print(
            """
                Sabor Express

                Selecione uma opção:
                1. Cadastrar restaurante
                2. Listar restaurantes
                3. Ativar restaurante
                4. Sair
            """
        )
        try:
            opcao_escolhida = int(input("Selecione uma opção: "))

            match opcao_escolhida:
                case 1:
                    cadastrar_restaurante()
                case 2:
                    listar_restaurantes()
                case 3:
                    ativar_restaurante()
                case 4:
                    os.system("cls")
                    print("Encerrando o programa...")
                    break
                case _:
                    print("\nOpção inválida. Tente novamente.")
                    limpar_tela()
        except ValueError:
            print("\nEntrada inválida. Digite um número de 1 a 4.")
            limpar_tela()


if __name__ == "__main__":
    menu_principal()

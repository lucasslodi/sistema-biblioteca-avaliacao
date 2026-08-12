import csv
import os

ARQUIVO_CSV = "livros.csv"
CAMPOS_CSV = ["titulo", "autor", "ano", "isbn", "status"]

def importar_livros(nome_arquivo): 
    biblioteca = [] #cria lista vazia 
    if not os.path.exists(nome_arquivo): 
        return biblioteca
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo: 
        leitor = csv.DictReader(arquivo) 
        for linha in leitor: 
            biblioteca.append(linha) 
    return biblioteca

def salvar_livros(nome_arquivo, biblioteca):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo: 
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_CSV)
        escritor.writeheader()
        escritor.writerows(biblioteca)

def cadastrar_livro(biblioteca):
    print("\n--- CADASTRO DE NOVO LIVRO ---") 
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    isbn = input("Código / ISBN: ")

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }

    biblioteca.append(novo_livro)
    print(f"\nLivro '{titulo}' cadastrado com sucesso!")

def listar_livros(biblioteca):
    print("\n--- CATÁLOGO DE LIVROS ---")
    if not biblioteca:
        print("Nenhum livro cadastrado no momento.")
        return 

    for i, livro in enumerate(biblioteca, start=1):
        print(f"{i}. [{livro['status'].upper()}] {livro['titulo']} - {livro['autor']} ({livro['ano']}) | ISBN: {livro['isbn']}")

def alterar_status(biblioteca, novo_status):
    acao = "empréstimo" if novo_status == "emprestado" else "devolução"
    print(f"\n--- REGISTRAR {acao.upper()} ---")
    isbn = input("Digite o ISBN do livro: ")

    for livro in biblioteca:
        if livro['isbn'] == isbn:
            if livro['status'] == novo_status:
                print(f"Aviso: O livro já está com o status '{novo_status}'.")
                return

            livro['status'] = novo_status
            print(f"Sucesso! {acao.capitalize()} registrado para o livro '{livro['titulo']}'.")
            return

    print("Erro: Nenhum livro encontrado com o ISBN informado.")

def exibir_menu():
    print("\n=================================")
    print("\n Programa feito por Lucas Emanuel")
    print("\n=================================")
    print("    SISTEMA DE BIBLIOTECA ")
    print("=================================")
    print("1. Cadastrar livro")
    print("2. Registrar empréstimo")
    print("3. Registrar devolução")
    print("4. Listar todos os livros")
    print("5. Buscar livro")
    print("6. Ordenar livros")
    print("0. Sair do programa")
    return input("Escolha uma opção: ")

def main():
    biblioteca = importar_livros(ARQUIVO_CSV)

    while True: 
        opcao = exibir_menu()

        if opcao == '1':
            cadastrar_livro(biblioteca)
        elif opcao == '2':
            alterar_status(biblioteca, "emprestado")
        elif opcao == '3':
            alterar_status(biblioteca, "disponível")
        elif opcao == '4':
            listar_livros(biblioteca)
        elif opcao == '0':
            salvar_livros(ARQUIVO_CSV, biblioteca)
            print("\nDados salvos em 'livros.csv'. Encerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Escolha um número entre 0 e 6.")

if __name__ == "__main__":
    main()
    
    
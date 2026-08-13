import csv
import os
 
ARQUIVO_CSV = "livros.csv"
CAMPOS_CSV = ["titulo", "autor", "ano", "isbn", "status"]
 
 
#  Criação da biblioteca de livros
# ==========================================
 
def importar_livros(nome_arquivo):
    biblioteca = [] #cria uma lista vazia
 
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo: #abre a lista no modo leitor. o encoding serve para ler as palavras do português de forma correta
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            biblioteca.append(linha)
           
    return biblioteca
 
 
def salvar_livros(nome_arquivo, biblioteca):
   
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo: #abre o arquivo csv no mode de escritor e reescreve as linhas do arquivo (para salvar os livros novos)
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_CSV)
        escritor.writeheader() # escreve o cabeçalho 
        escritor.writerows(biblioteca) # escreve todos os livros cadastrados de uma  vez
 
 
#
#REQUISITOS DE NEGÓCIO (FUNÇÕES DO SISTEMA)
# ==========================================
 
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
        "status": "disponível" # todo livro inicia obrigatoriamente disponível
    }
 
    biblioteca.append(novo_livro)
    print(f"\nLivro '{titulo}' cadastrado com sucesso!")
 
 
def listar_livros(biblioteca):
    """Exibe no terminal a listagem completa de livros."""
    print("\n--- CATÁLOGO DE LIVROS ---")
   
    if not biblioteca:
        print("Nenhum livro cadastrado no momento.")
        return # Encerra a execução da função aqui caso a biblioteca esteja vazia.
 
    for i, livro in enumerate(biblioteca, start=1):
        print(f"{i}. [{livro['status'].upper()}] {livro['titulo']} - {livro['autor']} ({livro['ano']}) | ISBN: {livro['isbn']}")
 
 
def buscar_livros(biblioteca):
    print("\n--- BUSCAR LIVRO ---")
    termo = input("Digite o título ou autor para buscar: ").lower()
   
    encontrados = []
    for livro in biblioteca:
        if termo in livro['titulo'].lower() or termo in livro['autor'].lower():
            encontrados.append(livro)
 
    if encontrados:
        print(f"\nResultados encontrados ({len(encontrados)}):")
        listar_livros(encontrados)
    else:
        print("\nNenhum livro encontrado com o termo informado.")
 
 
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
 
def pegar_titulo(livro):
    return livro['titulo'].lower()
 
def pegar_autor(livro):
    return livro['autor'].lower()
 
def pegar_ano(livro):
    return livro['ano']
 
 
def ordenar_livros(biblioteca):
    """Ordena a lista em memória por Título, Autor ou Ano."""
    print("\n--- ORDENAR LIVROS ---")
    print("1. Por Título")
    print("2. Por Autor")
    print("3. Por Ano de Publicação")
    opcao = input("Opção de ordenação: ")
 
    if opcao == '1':
        biblioteca.sort(key=pegar_titulo)
        print("Livros ordenados por TÍTULO!")
    elif opcao == '2':
        biblioteca.sort(key=pegar_autor)
        print("Livros ordenados por AUTOR!")
    elif opcao == '3':
        biblioteca.sort(key=pegar_ano)
        print("Livros ordenados por ANO!")
    else:
        print("Opção inválida de ordenação.")
 
 
# INTERFACE
# ==========================================
 
def exibir_menu():
    """Exibe o menu de opções no console."""
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
   
    while True:  # mantém o programa rodando até o usuário escolher a opção 0 (Sair).
        opcao = exibir_menu()
       
        if opcao == '1':
            cadastrar_livro(biblioteca)
        elif opcao == '2':
            alterar_status(biblioteca, "emprestado")
        elif opcao == '3':
            alterar_status(biblioteca, "disponível")
        elif opcao == '4':
            listar_livros(biblioteca)
        elif opcao == '5':
            buscar_livros(biblioteca)
        elif opcao == '6':
            ordenar_livros(biblioteca)
        elif opcao == '0':
            salvar_livros(ARQUIVO_CSV, biblioteca)
            print("\nDados salvos em 'livros.csv'. Encerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Escolha um número entre 0 e 6.")
 
if __name__ == "__main__":
    main()
 
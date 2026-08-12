import csv
import os

ARQUIVO_CSV = "livros.csv"
CAMPOS_CSV = ["titulo", "autor", "ano", "isbn", "status"]


# Criação da biblioteca de livros
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
        escritor.writeheader() # Escreve o cabeçalho (titulo, autor, ano, isbn, status)
        escritor.writerows(biblioteca) # Escreve todos os livros cadastrados de uma só vez


# 
# REQUISITOS DE NEGÓCIO (FUNÇÕES DO SISTEMA)
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
        "status": "disponível" # Todo livro inicia obrigatoriamente disponível
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


#INTERFACE 
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

    
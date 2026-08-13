#sistema de biblioteca

O sistema é desenvolvido na linguagem de Python e tem a funcionalidade para gerenciar o acervo de uma biblioteca. O código permite controlar o cadastro de livros, controlar empréstimos e devoluções, além de contar com funcionalidades de busca e ordenação de dados e manter tudo salvo de forma permanente em um arquivo csv.


#funcionalidades
1. **Cadastrar Livro**: Adiciona novas obras ao acervo informando Título, Autor, Ano de Publicação e Código/ISBN (iniciando automaticamente como "disponível").
2. **Registrar Empréstimo**: Altera o status de um livro disponível para "emprestado" com base no ISBN.
3. **Registrar Devolução**: Retorna o status de um livro emprestado para "disponível".
4. **Listar Livros**: Exibe todo o catálogo de forma organizada, detalhando o status atual de cada obra.
5. **Buscar Livro**: Permite localizar livros rapidamente pesquisando pelo título ou pelo nome do autor.
6. **Ordenar Livros**: Organiza a listagem em memória de acordo com a preferência do usuário (por Título, Autor ou Ano de Publicação).
7. **Persistência de Dados**: Todos os dados cadastrados são salvos automaticamente no arquivo `livros.csv` ao encerrar o programa.

#ferramentas utilizadas:
* **Python 3** (Linguagem principal)
* **Módulo `csv`** (Leitura e gravação de arquivos de dados)
* **Módulo `os`** (Verificação de existência de arquivos no diretório)
* **Git & GitHub** (Controle de versão e hospedagem do código)



#como executar o código:

1. Certifique-se ter o Python 3 instalado no computador;
2. abra o terminal e abra a pasta do projeto;
digitar o comando:
```bash
python main.py  ;



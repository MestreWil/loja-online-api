# Desenvolva uma API REST para uma loja online (SENAC RS)
==========================================================

A API deve permitir que os clientes façam o seu cadastro, consultem produtos disponíveis, 
realizem e listem seus pedidos. Além disso, os administrados devem ter acesso a recursos adicionais, 
como gerenciamento de produtos e pedidos.
A API deve ser desenvolvida utilizando JavaScrpt com Node.js
A API deve ser baseada nos princípios RESTful e utilizar os métodos HTTP corretos para cada operação (GET, POST, PUT, DELETE).
A API deve fornecer endpoints para as seguintes funcionalidades: Consulta de produtos disponíveis. Realização de um pedido. Consulta de 
pedidos realizados.
Os adminitsrradores devem ter acesso a endpoints adicionais para gerenciamento de produtos e pedidos, incluindo criação, atualização e exclusão de produtos.
A API deve retornar respostas apropriadas em caso de erros ou requisições inválidas.
Considere a utilização de bibliotecas ou frameworks adequados para o desenvolvimento da API (por exemplo, Express, Restify, Flask, Django...) Teste a API usando ferramentas como o Postman
ou Insomnia.

# Rodando a API do projeto

    # OBS: Ter versão do python acima da versão 3.10
    # OBS: Ter o modulo virtualenv instalado na maquina, caso não tenha:
    $pip install virtualenv
    
    # Clonar repositório
    $ git clone https://github.com/MestreWil/loja-online-api/
    # Iniciando setup do backend
    $ cd loja-online-api

    # Criar ambiente virtual específico para esse projeto
    $ python -m venv venv 
    
    # Ativar a venv
    $ ./venv/Scripts/activate

    # Instalar todas as dependências
    $ pip install -r requirements.txt

    # Rodar as migrations 
    $ python manage.py migrate

    # Criar um super user
    $ python manage.py createsuperuser

    # Rodar projeto
    $ python manage.py runserver
    

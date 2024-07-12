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

# Diagrama ER BASE
<br>
<p align="center">
  <a href="https://github.com/MestreWil/loja-online-api/blob/main/Captura%20de%20tela%202024-07-12%20130642.png">
    <img src="Captura%20de%20tela%202024-07-12%20130642.png" alt="Diagrama" width="180" height="180">
  </a>
# Rodando a API do projeto

    # OBS: Ter versão do python acima da versão 3.10
    # OBS: QUANDO RODAR A API, PARA VELA FUNCIONANDO BASTA ENTRA NO PAINEL ADMIN COLOCANDO /admin apos entrar na porta do api
    # USE O LOGIN QUE VOCÊ CRIOU NO createsuperuser para acessar o painel administrador
    # OBS: Ter o modulo virtualenv instalado na maquina, caso não tenha:
    $pip install virtualenv
    
    # Clonar repositório
    $ git clone https://github.com/MestreWil/loja-online-api/
    
    # Entrando na pasta do backend
    $ cd loja-online-api

    # Criar ambiente virtual específico para esse projeto
    $ python -m venv venv 
    
    # Ativar a venv
    $ ./venv/Scripts/activate

    # Instalar todas as dependências obs:tenha certeza de que você está na venv e com o interpretador na venv selecionado para instalar as dependencias
    $ pip install -r requirements.txt

    # Rodar as migrations 
    $ python manage.py migrate

    # Criar um super user
    $ python manage.py createsuperuser

    # Rodar projeto
    $ python manage.py runserver
    
    
    #ao entrar e der pagina not found, basta colocar /admin no endpoint para ser encaminhado para o painel administrador da API, loge com seu login e senha criados na etapa de criacao do super usuario e pronto
    
    # CASO ALGO NÃO TENHA FUNCIONADO OU SURGIU ALGUMA DÚVIDA, POR FAVOR ENTRAR EM CONTATO 
    # Email: williamtavaresdemoura@gmail.com
    # Instagram: @mestre_will
    

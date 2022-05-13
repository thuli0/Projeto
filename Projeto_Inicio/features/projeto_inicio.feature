# language: pt
@PROJETOINICIO
Funcionalidade: Cadastro Teste
    
    @001
    Cenário: 001 - Validar home do APP
        Quando Eu estou na tela home do APP sem clientes cadastrado
        Então Eu verifico que os textos da tela estão corretos
        E Eu verifico que o botão “+” Para Adicionar novos cadastro, e o campo pesquisa, são exibidos

    @002
    Cenário: 002 - Validar opções exibidas pelo botão “+”
        Quando Eu estou na tela home do APP
        E Clico no botão “+”
        Então Eu Verifico que as opções Cadastrar Novo, Exportar Dados, Sobre o App, São exibidas
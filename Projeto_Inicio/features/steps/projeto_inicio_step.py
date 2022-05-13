from pages.projeto_inicio_page import *
from behave import *


@when('Eu estou na tela home do APP sem clientes cadastrado')
def step_impl(context):
    context.page_object = ProjetoInicioPage(context.driver)


@then('Eu verifico que os textos da tela estão corretos')
def step_impl(context):
    context.page_object.validar_text_home()


@then('Eu verifico que o botão “+” Para Adicionar novos cadastro, e o campo pesquisa, são exibidos')
def step_impl(context):
    context.page_object.validar_bt_mais()


@when('Eu estou na tela home do APP')
def step_impl(context):
    context.page_object = ProjetoInicioPage(context.driver)


@when('Clico no botão “+”')
def step_impl(context):
    context.page_object.click_bt_mais()


@then('Eu Verifico que as opções Cadastrar Novo, Exportar Dados, Sobre o App, São exibidas')
def step_impl(context):
    context.page_object.validar_text_bt_mais()
from appium.webdriver.common.mobileby import MobileBy
from constants.projeto_constants import *
from common.base_page import BasePage
from common.utils import *


class ProjetoInicioPage(BasePage):
    
    BT_MAIS = (
        MobileBy.XPATH, '*//android.view.ViewGroup/android.widget.ImageButton')
    CAMPO_PESQUISAR = (
        MobileBy.ID, PACKAGE_APP+":id/editPesquisar")
    TEXT_NENHUM_CLIENT = (
        MobileBy.ID, PACKAGE_APP+":id/txtNenhumCliente")
    TEXT_NENHUM_CLIENTE = (
        MobileBy.XPATH, '//*[@text="Nenhum cliente cadastrado"]')
    
    TEXT_TITULO = (
        MobileBy.XPATH, '//*[@text="Cadastro de Clientes"]')
    
    TEXT_BT_MAIS1 = (
        MobileBy.XPATH, '//*[@text="Cadastrar Novo"]')
    
    TEXT_BT_MAIS2 = (
        MobileBy.XPATH, '//*[@text="Exportar Dados"]')

    TEXT_BT_MAIS3 = (
        MobileBy.XPATH, '//*[@text="Sobre o App"]')

    TEXT_BT_MAIS4 = (
        MobileBy.XPATH, '//*[@text="Opções"]')


    def click_bt_mais(self):
        super().custom_wait_implicit(self.BT_MAIS)
        super().click(self.BT_MAIS)
    
    
    def validar_text_home(self):
        super().custom_wait_implicit(self.TEXT_TITULO)
        super().validar_text_elemento(
            self.TEXT_TITULO, TEXTO_TITULO)
        super().validar_text_elemento(
            self.TEXT_NENHUM_CLIENT, TEXTO_NENHUM_CLIENTE)

    
    def validar_bt_mais(self):
        super().find_element_visibility(self.BT_MAIS)


    def validar_text_bt_mais(self):
        super().custom_wait_implicit(self.TEXT_TITULO)
        super().validar_text_elemento(
            self.TEXT_BT_MAIS1, TEXTO_BT_MAIS1)
        super().validar_text_elemento(
            self.TEXT_BT_MAIS2, TEXTO_BT_MAIS2)
        super().validar_text_elemento(
            self.TEXT_BT_MAIS3, TEXTO_BT_MAIS3)
        super().validar_text_elemento(
            self.TEXT_BT_MAIS4, TEXTO_BT_MAIS4)
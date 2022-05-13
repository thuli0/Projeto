import os
from appium import webdriver
from hamcrest import assert_that, is_

class Environment:

    def set_capabilities(context, scenario):
        if(context.config.userdata['type_execution'].upper() in 'LOCAL'):
            desired_caps = {}
            desired_caps['platformName']         = 'Android'
            desired_caps['deviceName']           = 'Android Emulator'
            desired_caps['app']                  = '/Users/bi003703/Documents/PROJETO/tests/cadastro_clientes_teste.apk'
            desired_caps['autoGrantPermissions'] = True
            desired_caps['autoAcceptAlerts']     = True
            desired_caps['automationName']       = 'UiAutomator2'
            context.driver                       = webdriver.Remote(
                context.config.userdata['appium_server_local'], desired_caps)
from common.environment_common import *


def before_scenario(context,scenario):
    Environment.set_capabilities(context,scenario)


def after_scenario(context, scenario):
    context.driver.close_app()
    context.driver.quit()
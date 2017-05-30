
import configparser #To get config from .ini

def get_config_gmail(conf_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(conf_file)

    returnval = dict()

    returnval['Gmail_User'] = config.get('Gmail','Email')
    returnval['Gmail_Pass'] = config.get('Gmail','Pass')

    return returnval

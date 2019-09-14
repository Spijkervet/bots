import configparser

config = configparser.ConfigParser()

config.read(r'/usr/local/lib/python3.6/site-packages/bots/config/bots.ini')
config.set('jobqueue', 'enabled', 'True')
config.set('dirmonitor1', 'path', '/dirmon')
config.remove_section('dirmonitor2')
with open(r'/usr/local/lib/python3.6/site-packages/bots/config/bots.ini', 'w') as configfile:
    config.write(configfile)
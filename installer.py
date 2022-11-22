import os
import configparser
import shutil

root = os.path.join(os.path.abspath(os.curdir), "TD5GLiveMonitor")
print(root)


def create_folders(root):
    try:
        os.mkdir(root)
    except FileExistsError:
        print(f"{os.path.join(root)} already exists...")


def create_config(root):
    config = configparser.ConfigParser()
    config.add_section('debugger')
    config.set('debugger', 'path', os.path.join(root, 'LOGGER'))
    config.set('debugger', 'logger', 'TD5GLog')
    config.set('debugger', 'level', 'DEBUG')

    config.add_section('techs')
    config.set('techs', 'Shawn Scoville', 'ShawnS@surveillance-247.com')
    config.set('techs', 'Ian Sutton', 'IanS@surveillance-247.com')
    config.set('techs', 'Anthony Marrongelli', 'AnthonyM@surveillance-247.com')
    config.set('techs', 'Mark Louprette Jr', 'MarkL@surveillance-247.com')

    config.add_section('server')
    config.set('server', 'IP ADDRESS', '127.0.0.1')
    config.set('server', 'PORT', '45826')
    config.set('server', 'user', 'Smartuser')
    config.set('server', 'pass', 'Smart247!')

    config.add_section('client')
    config.set('client', 'IP ADDRESS', '127.0.0.1')
    config.set('client', 'PORT', '45826')
    config.set('client', 'user', 'Smartuser')
    config.set('client', 'pass', 'Smart247!')
    config.set('client', 'client', 'TD5G Server')

    with open(os.path.join(root, 'config.ini'), 'w') as configfile:
        config.write(configfile)
    print(f"{configfile} created...")


if __name__ == '__main__':
    create_folders(root)
    create_config(root)


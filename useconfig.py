from configparser import ConfigParser
import os

config_file = r"C:\Users\steve\OneDrive\Projects-2025\Github\examples\pythonconfig.ini"
f = open(config_file, "r")
print(f)
config= ConfigParser()

config.read(config_file)

print(os.getcwd())

##server_alive_interval = config['DEFAULT']['ServerAliveInterval']

config_data=config['DEFAULT']

for key, value in config['DEFAULT'].items():
    print(f"{key}: {value}")

print(type(config_data))
print(config_data['number'])
print(config_data.getint('number'))
print(config_data)

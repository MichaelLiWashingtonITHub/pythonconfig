from configparser import ConfigParser
config = ConfigParser()

config["DEFAULT"] = {
    "number" : 5,
    "playername":"Michael Li",
    "ServerAliveInterval" : 45,
    "Compression" : "yes",
    "CompressionLevel" : 9,
    "ForwardX11": "yes"
}

config["bitbucket.org"] = {
    "User" : "hg"
}

config["topsecret.server.com"] ={
    "Port" : 50022,
    "ForwardX11" :  "no"

}


config["SUDO"] = {
    "number" : 5,
    "playername":"Steven Li"
}

config_file=r"C:\Users\steve\OneDrive\Projects-2025\Github\examples\pythonconfig.ini"
with open(config_file, "w") as f:
    config.write(f)


###



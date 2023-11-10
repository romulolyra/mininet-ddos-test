# Create json configuration file (conf.json) containing initial values of controller_ip, auth_port, shared_key, next_ctr
import json

conf_dict = {
    "controller_ip" : "127.0.0.1",
    "auth_port" : 6633,
    "master_key" : "abracadabra",
    "next_ctr" : 1
}
  
with open("conf.json", "w") as config_file:
    json.dump(conf_dict, config_file)
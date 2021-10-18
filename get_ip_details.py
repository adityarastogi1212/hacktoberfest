# Date: 12/05/2021

import sys
import json
from ipaddress import *
import requests
from prettytable import PrettyTable

def syntax():
    print("\nSyntax: For Own IP:    Python3 iptracer.py")
    print("\tFor Others IP: Python3 iptracer.py <other_IP_here>")

def results():
    x = PrettyTable()
    x.field_names = ["Key", "Value"]

    for key,value in req.items():
        x.add_row([key,value])

    print(x)

if len(sys.argv) < 2:
    own_ip = requests.get('https://api.ipify.org').text
    req = requests.get(f"http://ip-api.com/json/{own_ip}").json()
    print(f"\n#-----------IP details for [{own_ip}]------------#\n")
    results()
    print(f"\n#------------------------------------------------------#")

elif len(sys.argv) == 2:
    try:
        if ip_address(sys.argv[1]).is_loopback:
            print(f"'{sys.argv[1]}' is a loopback IP")

        elif ip_address(sys.argv[1]).is_private:
            print(f"'{sys.argv[1]}' is a private IP")
        
        else:
            others_ip = ip_address(sys.argv[1])
            req = requests.get(f"http://ip-api.com/json/{others_ip}").json()
            print(f"\n#--------------IP details for [{sys.argv[1]}]-------------#\n")
            results()
            print(f"\n#----------------------------------------------------------#")

    except ValueError:
        print(f"That's not an IP address: '{sys.argv[1]}'")

    except:
        syntax()

else:
    print("\nOops!! You have got a Syntax Error.")
    syntax()

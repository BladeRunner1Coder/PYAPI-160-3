import requests
import json
import sys
import os
from dotenv import load_dotenv
from time import sleep
from tqdm import tqdm


class GetIP:
    url_ip = 'https://api.ipify.org/?format=json'
    def __init__(self):
        self.ip = None

    def set_ip(self, bar):
        response = requests.get(self.url_ip)
        self.ip = response.json()['ip']
        sleep(1)
        bar.update(25)
        bar.set_postfix_str(f"Your IP was received successfully!")

    def get_ip(self):
        return self.ip


class GetAddress:
    url_address = 'https://ipinfo.io/'

    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.city = None

    def set_city(self, bar):
        response = requests.get(self.url_address + self.ip_address + '/geo')
        self.city = response.json()['city']
        sleep(1)
        bar.update(25)
        bar.set_postfix_str(f"Your City was detected successfully!")

    def get_city(self):
        return self.city

def create_folder(bar):
    sleep(1)
    bar.update(25)
    bar.set_postfix_str(f"Your Folder was created successfully!")

def upload_json_yd(ip, city, bar):
    info = dict()
    info[ip] = city
    info_json = json.dumps(info, ensure_ascii=False)
    pbar.write(info_json)
    sleep(1)
    bar.update(25)
    bar.set_postfix_str(f"Your File was uploaded successfully!")
    sleep(1)
    bar.set_postfix_str("Program closed!")
    return info_json

pbar = tqdm(total=100, desc=f"Program progress", file=sys.stdout)
getip = GetIP()
getip.set_ip(pbar)
address = GetAddress(getip.get_ip())
address.set_city(pbar)
load_dotenv()
token = os.getenv("TOKEN")
create_folder(pbar)
upload_json_yd(getip.get_ip(), address.get_city(), pbar)
pbar.close()

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
        bar.update(20)
        bar.set_postfix_str(f"Your IP was received successfully!")

    def get_ip(self):
        return self.ip


class GetAddress:
    url_address = 'https://ipinfo.io/'

    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.city = None

    def set_city(self, bar):
        response = requests.get(f"{self.url_address}{self.ip_address}/geo")
        self.city = response.json()['city']
        sleep(1)
        bar.update(20)
        bar.set_postfix_str(f"Your City was detected successfully!")

    def get_city(self):
        return self.city


class YandexDisk:
    urlYD = "https://cloud-api.yandex.net"

    def __init__(self, your_token):
        self.token = your_token
        self.headers = {"Authorization": f"OAuth {self.token}"}

    def create_folder(self, bar):
        params = {"path": "/Your IP city"}
        response = requests.put(f"{self.urlYD}/v1/disk/resources/", params=params, headers=self.headers)
        if response.status_code == 201:
            sleep(1)
            bar.update(20)
            bar.set_postfix_str(f"Folder 'Your IP city' was created successfully!")
        elif response.status_code == 409:
            sleep(1)
            bar.update(20)
            bar.set_postfix_str(f"Folder 'Your IP city' already exists!")
        else:
            sleep(1)
            bar.write(f"Folder 'Your IP city' was not created: {response.status_code}")
            bar.write(response.json()["message"])
            bar.close()
            sys.exit(0)

    def upload_file_to_folder(self, bar, ip, city):
        params = {
            "path": f"/Your IP city/{city}.json",
            "overwrite": "true"
        }
        response = requests.get(f"{self.urlYD}/v1/disk/resources/upload",
                                params=params, headers=self.headers)
        if response.status_code == 200:
            sleep(1)
            bar.update(20)
            bar.set_postfix_str(f"Link to upload file {city}.json received successfully!")
        elif response.status_code == 409:
            sleep(1)
            bar.update(20)
            bar.set_postfix_str(f"File {city}.json already exists!")
        else:
            bar.write(f"Error: {response.status_code}")
            bar.write(response.json()["message"])
            bar.close()
            sys.exit(0)
        path = response.json()["href"]
        info = {ip: city}
        info_json = json.dumps(info, ensure_ascii=False)
        response2 = requests.put(path, data=info_json.encode('utf-8'))
        if response2.status_code == 201:
            sleep(1)
            bar.update(20)
            bar.set_postfix_str(f"File {city}.json uploaded successfully!")
        else:
            bar.write(f"Loading error: {response2.status_code}")
            bar.write(response2.json()["message"])
            bar.close()
            sys.exit(0)


pbar = tqdm(total=100, desc=f"Program progress", file=sys.stdout)
getip = GetIP()
getip.set_ip(pbar)
address = GetAddress(getip.get_ip())
address.set_city(pbar)
load_dotenv()
token = os.getenv("TOKEN")
YD = YandexDisk(token)
YD.create_folder(pbar)
YD.upload_file_to_folder(pbar, getip.get_ip(), address.get_city())
sleep(1)
pbar.set_postfix_str("Program closed!")
pbar.close()

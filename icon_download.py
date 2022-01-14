import os
import sys

import requests
from bs4 import BeautifulSoup


def download_icon(pack):
    server_name = "cafe-bazaar"
    url = "https://cafebazaar.ir/app/" + str(pack)
    try:
        resp = requests.get(url.rstrip())
        soup = BeautifulSoup(resp.text, 'html.parser')
        if resp.status_code == 404:
            print(pack.strip() + " is not exists on " + server_name)
            return
        tag = soup.find("div", {"class": "CoverHeader__thumbnail"}).findChildren("img")
        link = tag[0]['src']
        file = requests.get(link.rstrip(), stream=True, allow_redirects=True)
        path = f"./repo/{pack}"
        os.popen(f"mkdir {path}")
        with open(f'{path}/icon.png', 'wb') as files:
            files.write(file.content)
            sys.stdout.flush()
        print(link)
    except Exception as ex:
        print(f"error occurred in downloading in {pack} :" + ex.__str__())
    print(pack)


def download_test(pack):
    serverName = "cafe-bazaar"
    url = "https://cafebazaar.ir/app/" + str(pack)
    try:
        resp = requests.get(url.rstrip())
        soup = BeautifulSoup(resp.text, 'html.parser')
        if resp.status_code == 404:
            print(pack.strip() + " is not exists on " + serverName)
            return
        tag = soup.find("div", {"class": "CoverHeader__thumbnail"}).findChildren("img")
        link = tag[0]['src']
        file = requests.get(link.rstrip(), stream=True, allow_redirects=True)
        with open('icon.png', 'wb') as files:
            files.write(file.content)
            sys.stdout.flush()
        print(link)
    except Exception as ex:
        print(f"error occurred in downloading in {pack} :" + ex.__str__())
    print(pack)


def get_list_apps(name):
    path = './repo/'
    apk_lists = list(filter(lambda file: file.split('.')[-1] == 'apk', os.listdir(path)))
    apk_hashmap = []
    try:
        for i in range(len(apk_lists)):
            package_name = os.popen(
                "aapt dump badging " + path + apk_lists[
                    i] + " | awk -v FS=\"\'\" \'/package: name=/{print $2}\'").read()
            new_package_name = str(package_name).rstrip()
            if new_package_name in apk_hashmap:
                print("next")
            else:
                apk_hashmap.append(new_package_name)
    except Exception as e:
        print("an error occurred in getting packageNames error is :\n\t+" + e.__str__())
    print(apk_hashmap)
    for pack in apk_hashmap:
        if pack is not None:
            download_icon(pack.rstrip())
    print("finished")


if __name__ == '__main__':
    get_list_apps("alireza")
    # download_test('org.mozilla.firefox')

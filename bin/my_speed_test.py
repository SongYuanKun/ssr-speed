import json
import os
import re
import socket
import subprocess

import requests
import socks
from prettytable import PrettyTable

from bin.curses_test import test_option


class DrawTable(object):
    def __init__(self):
        self.table = []
        header = [
            "name",
            "ip",
            "localPing",
            "ping",
            "upload",
            "download",
            "network"
        ]
        self.x = PrettyTable(header)
        self.x.reversesort = True
        self.x.sortby = "download"

    def append(self, **kwargs):
        if kwargs:
            content = [
                kwargs['name'],
                kwargs['ip'],
                kwargs['localPing'],
                kwargs['ping'],
                kwargs['upload'],
                kwargs['download'],
                kwargs['network'],
            ]
            self.x.add_row(content)

    def str(self):
        return str(self.x)


def connect_ssr(ssr):
    result = {
        'host': ssr['server'],
        'remarks': ssr['remarks'],
        'ip': '',
        'download': 0,
        'upload': 0,
        'ping': 0,
        'ping_pc': 0,
        'state': "Fail"
    }
    try:
        print(ssr['remarks'] + "/" + ssr['server'])
        if test_option['ping']:
            ret = subprocess.Popen("ping -n 3 %s" % result['host'], shell=True, stdout=subprocess.PIPE)
            out = ret.stdout.readlines()
            pattern = re.compile(r'\d+')
            ping_pc = pattern.findall(out[-1].decode('gbk'))
            print("ping_test,localPing:", ping_pc[-1])
            result['ping_pc'] = ping_pc[-1]

        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 6665)
        socket.socket = socks.socksocket
        if test_option['network']:
            ip = requests.get('http://api.ip.sb/ip', timeout=15).text.strip()
            result['ip'] = ip
            print("network_test,ip:", result['ip'])

        if test_option['speed']:
            from bin import speedtest
            s = speedtest.Speedtest()
            s.get_best_server()
            s.download()
            s.upload()
            s.results.share()
            results_dict = s.results.dict()
            result['ping'] = results_dict['ping']
            result['download'] = round(results_dict['download'] / 1000.0 / 1000.0, 2)
            result['upload'] = round(results_dict['upload'] / 1000.0 / 1000.0, 2)
            result['state'] = "Success"
            result['ip'] = results_dict['client']['ip']
            print("speed_test,ping:%s,download:%s,upload:%s" % (result['ping'], result['download'], result['upload']))

        result['state'] = "Success"
        return result

    except Exception as e:
        print(e)
        return result


def write_json(write_config):
    # 打开ssr config json
    json_path = "../win/gui-config.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        json_config = json.load(f)
    # 清空configs列表
    json_config['configs'] = []
    json_config['configs'].append(write_config)
    if 'protoparam' in json_config['configs'][0]:
        json_config['configs'][0]['protocolparam'] = json_config['configs'][0]['protoparam']
    if 'port' in json_config['configs'][0]:
        json_config['configs'][0]['server_port'] = json_config['configs'][0]['port']
    # 将订阅的数据写入的配置文件
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_config, f, indent=4)


# 运行 ssr
def run_ssr():
    ssr_path = "../win/ShadowsocksR-dotnet4.0-speedtest.exe"
    subprocess.Popen(ssr_path)


# 关闭ssr
def close_ssr():
    subprocess.call('taskkill /f /im ShadowsocksR-dotnet4.0-speedtest.exe', stdout=subprocess.PIPE)


table = DrawTable()


def test_ssr(config):
    run_ssr()
    write_json(config)
    speed_result = connect_ssr(config)
    os.system('cls')
    table.append(
        name=speed_result['remarks'],
        ip=speed_result['ip'],
        localPing=speed_result['ping_pc'],
        ping=speed_result['ping'],
        upload=speed_result['upload'],
        download=speed_result['download'],
        # youtube=speed_result['youtube'],
        network=speed_result['state']
    )
    print(table.str())
    close_ssr()
    return speed_result['state'] == 'Success'


if __name__ == '__main__':
    x = {
        "remarks": "@SSRTOOL_hkt2.puffvip.com",
        "id": "F47BE256D1E8ED50D02E9228AEB4DF05",
        "server": "hkt2.puffvip.com",
        "server_port": 443,
        "server_udp_port": 0,
        "password": "Paofu",
        "method": "chacha20",
        "protocol": "auth_aes128_md5",
        "protocolparam": "44479:nIiKIB",
        "obfs": "http_simple",
        "obfsparam": "3c2ad44479.microsoft.com",
        "remarks_base64": "QFNTUlRPT0xfaGt0Mi5wdWZmdmlwLmNvbQ",
        "group": "SSRTOOL.COM 推送"
    }
    test_ssr(x)

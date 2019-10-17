import json
import re
import socket
import subprocess

import requests
import socks
from prettytable import PrettyTable

from ParseSsr import ssr2json
from get_config import queryFrom_SSR_SHARE, queryFrom_youneed1, queryFrom_youneed2

default_socket = socket.socket


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

    def append(self, *args, **kwargs):
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
            import speedtest
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


# 运行 ssr
def run_ssr():
    ssr_path = "D:\SSR\ShadowsocksR-dotnet4.0.exe"
    subprocess.Popen(ssr_path)


# 关闭ssr
def close_ssr():
    subprocess.call('taskkill /f /im ShadowsocksR-dotnet4.0.exe', stdout=subprocess.PIPE)


test_option = {'ping': True, 'network': True, 'speed': True, 'youtube': True}
max_cols = 0
# 访问 youtube 网页加载时间大于设置时间直接退出不进行测速.解决高延迟的节点加载网页太慢问题
youtube_timeout = 10
# 使用 访问ip.sb获取外网ip的超时时间,判断节点是否能正常访问网页的依据
network_timeout = 15
# 测试所用端口
ssr_port = 6665

ssr_config = []
speed_result = []

to_test_list = queryFrom_SSR_SHARE()

to_test_list.extend(queryFrom_youneed1())
to_test_list.extend(queryFrom_youneed2())

print('to_test_urls=', to_test_list)

file_path = "D:\SSR\gui-config.json"
file_config = None
with open(file_path, 'r', encoding='utf-8') as f:
    file_config = json.load(f)
configs = file_config['configs']

for ssr_url in to_test_list:
    config = ssr2json(ssr_url)
    have_this = 0
    for x in configs:
        if x['server'] == config['server']:
            have_this = 1
    if have_this == 0:
        configs.append(config)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(file_config, f, indent=2)

for x in configs:
    ssr_config.append(x)
table = DrawTable()
run_ssr()

false_configs = []

# 测速感觉有点多余
# for x in ssr_config:
#     speed_result = connect_ssr(x)
#     if speed_result['state'] != 'Success':
#         false_configs.append(x)
#     os.system('cls')
#     table.append(
#         name=speed_result['remarks'],
#         ip=speed_result['ip'],
#         localPing=speed_result['ping_pc'],
#         ping=speed_result['ping'],
#         upload=speed_result['upload'],
#         download=speed_result['download'],
#         network=speed_result['state']
#     )
# print(table.str())

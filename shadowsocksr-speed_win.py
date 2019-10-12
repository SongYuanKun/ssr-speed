import base64
import json
import re
import socket
import subprocess

import requests
import socks
from prettytable import PrettyTable

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
            "youtube",
            "network"
        ]
        self.x = PrettyTable(header)
        self.x.reversesort = True
        self.x.sortby = "download"

    def append(self, *args, **kwargs):
        if (kwargs):
            content = [
                kwargs['name'],
                kwargs['ip'],
                kwargs['localPing'],
                kwargs['ping'],
                kwargs['upload'],
                kwargs['download'],
                kwargs['youtube'],
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
        'youtube': 0,
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


# 将订阅的数据写入到配置文件中
def write_json(write_config):
    # 打开ssr config json
    json_path = "win/gui-config.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        json_config = json.load(f)
    # 清空configs列表
    json_config['configs'] = []
    json_config['configs'].append(write_config)
    if 'protoparam' in json_config['configs'][0]:
        json_config['configs'][0]['protocolparam'] = json_config['configs'][0]['protoparam']
    if 'port' in json_config['configs'][0]:
        json_config['configs'][0]['server_port'] = json_config['configs'][0]['port']
    # ssr_port=json_config['configs'][0]['port']
    # 将订阅的数据写入的配置文件
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_config, f, indent=4)


# 运行 ssr
def run_ssr():
    ssr_path = "win/ShadowsocksR-dotnet4.0-speedtest.exe"
    subprocess.Popen(ssr_path)


# 关闭ssr
def close_ssr():
    subprocess.call('taskkill /f /im ShadowsocksR-dotnet4.0-speedtest.exe', stdout=subprocess.PIPE)


def ssr2json(text):
    if text.startswith('ssr://'):
        text = text[6:]
        print(ssrDecode(text))
    elif text.startswith('ss://'):
        text = text[5:]
        ssDecode(text)
    return


def ssrDecode(text):
    data = base64.b64decode(text.encode('utf-8'))
    arr = str(data, encoding="utf8").split(':')
    result1 = base64.b64decode(arr[5].split('/?')[0].encode('utf-8'))
    ip = arr[0]
    port = arr[1]
    password = result1
    group = ""
    obfs = arr[4]
    method = arr[3]
    protocol = arr[2]
    remarks = ""
    protoparam = ""
    obfsparam = ""
    group = ""
    udpport = ""
    uot = ""

    return {
        "server": ip,
        "server_port": port,
        "password": password,
        "obfs": obfs,
        "method": method,
        "protocol": protocol
    }


def ssDecode(text):
    return {
        "server": "${ip}",
        "server_port": "${port}",
        "password": "${password}",
        "method": "${method}"
    }


ssr2json(
    "ssr://c2hkZG5zLnhtdHByb3RvLmNsb3VkbnMuYXNpYToxMTAyMzpvcmlnaW46YWVzLTI1Ni1jdHI6cGxhaW46WVdSVVVVWlYvP3JlbWFya3M9UUZOVFVsUlBUMHhmYzJoa1pHNXpMbmh0ZEhCeWIzUnZMbU5zYjNWa2JuTXVZWE5wWVEmZ3JvdXA9VTFOU1ZFOVBUQzVEVDAwZzVvNm82WUNC")
test_option = {'ping': True, 'network': True, 'speed': True, 'youtube': True}
# max_cols = 0
# # 访问 youtube 网页加载时间大于设置时间直接退出不进行测速.解决高延迟的节点加载网页太慢问题
# youtube_timeout = 10
# # 使用 访问ip.sb获取外网ip的超时时间,判断节点是否能正常访问网页的依据
# network_timeout = 15
# # 测试所用端口
# ssr_port = 6665
#
# ssr_config = []
# speed_result = []
#
# if len(argv) > 1:
#     print(argv[1])
#     # file_path="win/gui-config.json"
#     file_path = argv[1]
#     file_config = None
#     with open(file_path, 'r', encoding='utf-8') as f:
#         file_config = json.load(f)
#     # print(file_config['configs'])
#     for x in file_config['configs']:
#         ssr_config.append(x)
#     # print(x)
#     # print(x)
# else:
#     url = input("url:")
#     headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
#     f = urllib.request.Request(url, headers=headers)
#     ssr_subscribe = urllib.request.urlopen(f).read().decode('utf-8')  # 获取ssr订阅链接中数据
#     ssr_subscribe_decode = ParseSsr.base64_decode(ssr_subscribe)
#     ssr_subscribe_decode = ssr_subscribe_decode.replace('\r', '')
#     ssr_subscribe_decode = ssr_subscribe_decode.split('\n')
#     for i in ssr_subscribe_decode:
#         if (i):
#             decdata = str(i[6:])  # 去掉"SSR://"K
#             ssr_config.append(ParseSsr.parse(decdata))  # 解析"SSR://" 后边的base64的配置信息返回一个字典
# table = DrawTable()
# for x in ssr_config:
#     # print(x)
#     run_ssr()
# write_json(x)
# speed_result = connect_ssr(x)
# os.system('cls')
# table.append(
#     name=speed_result['remarks'],
#     ip=speed_result['ip'],
#     localPing=speed_result['ping_pc'],
#     ping=speed_result['ping'],
#     upload=speed_result['upload'],
#     download=speed_result['download'],
#     youtube=speed_result['youtube'],
#     network=speed_result['state']
# )
# print(table.str())
# close_ssr()

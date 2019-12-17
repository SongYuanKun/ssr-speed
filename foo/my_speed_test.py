import os
import re
import socket
import subprocess

import requests
import socks

from foo import ssr_properties
from foo.curses_test import test_option


def connect_ssr(ssr, port):
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
        my_socket = socks.socksocket()
        my_socket.setproxy(socks.SOCKS5, "127.0.0.1", port)

        if test_option['network']:
            ip = requests.get('http://103.88.45.51/ip', headers={'host': 'api.ip.sb'}, timeout=15).text.strip()
            result['ip'] = ip
            print("network_test,ip:", result['ip'])

        if test_option['speed']:
            from foo import speedtest
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
    ssr_path = r"D:\PycharmProjects\ssr-speed\bin\ShadowsocksR-dotnet4.0-speedtest.exe"
    subprocess.Popen(ssr_path)


# 关闭ssr
def close_ssr():
    subprocess.call('taskkill /f /im ShadowsocksR-dotnet4.0-speedtest.exe', stdout=subprocess.PIPE)


def run_ssr2():
    ssr_path = r"D:\PycharmProjects\ssr-speed\bin\temp2\ShadowsocksR-dotnet4.0-speedtest2.exe"
    subprocess.Popen(ssr_path)


def close_ssr2():
    subprocess.call('taskkill /f /im ShadowsocksR-dotnet4.0-speedtest2.exe', stdout=subprocess.PIPE)


def run_ssr3():
    ssr_path = r"D:\PycharmProjects\ssr-speed\bin\temp3\ShadowsocksR-dotnet4.0-speedtest3.exe"
    subprocess.Popen(ssr_path)


def close_ssr3():
    subprocess.call('taskkill /f /im ShadowsocksR-dotnet4.0-speedtest3.exe', stdout=subprocess.PIPE)
    # 运行 ssr


def run_ssr4():
    ssr_path = r"D:\PycharmProjects\ssr-speed\bin\temp4\ShadowsocksR-dotnet4.0-speedtest4.exe"
    subprocess.Popen(ssr_path)


# 关闭ssr
def close_ssr4():
    subprocess.call('taskkill /f /im ShadowsocksR-dotnet4.0-speedtest4.exe', stdout=subprocess.PIPE)


def test_ssr(config, num):
    speed_result = {}
    if num == 1:
        run_ssr()
        ssr_properties.write_test_json(config)
        speed_result = connect_ssr(config, 6665)
        close_ssr()
    elif num == 2:
        run_ssr2()
        ssr_properties.write_test_json2(config)
        speed_result = connect_ssr(config, 6666)
        close_ssr2()
    elif num == 3:
        run_ssr3()
        ssr_properties.write_test_json3(config)
        speed_result = connect_ssr(config, 6667)
        close_ssr3()
    elif num == 4:
        run_ssr4()
        ssr_properties.write_test_json4(config)
        speed_result = connect_ssr(config, 6668)
        close_ssr4()

    return speed_result['state'] == 'Success'

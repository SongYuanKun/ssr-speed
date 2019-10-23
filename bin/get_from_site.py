import socket
import subprocess

from bin import get_ssr_properties, get_from_subscribe
from bin.ParseSsr import ssr2json
from bin.my_speed_test import test_ssr, table

default_socket = socket.socket


# 运行 ssr
def run_ssr():
    ssr_path = r"D:\SSR\ShadowsocksR-dotnet4.0.exe"
    subprocess.Popen(ssr_path)


# 关闭ssr
def close_ssr():
    subprocess.call('taskkill /f /im ShadowsocksR-dotnet4.0.exe', stdout=subprocess.PIPE)


def get_from_site():
    to_test_list = get_from_subscribe.get_from_subscribe()
    # to_test_list.extend(get_ssr_config.get_from_ssrjiedian())
    # to_test_list.extend(get_ssr_config.get_from_youneed1())
    # to_test_list.extend(get_ssr_config.get_from_youneed2())
    print('to_test_urls=', to_test_list)

    properties = get_ssr_properties.get_properties()
    configs = properties['configs']
    for ssr_url in to_test_list:
        config = ssr2json(ssr_url)
        have_this = 0
        for x in configs:
            if x['server'] == config['server']:
                have_this = 1
        if have_this == 0 and test_ssr(config):
            configs.append(config)
    print(table.str())
    get_ssr_properties.save_properties(properties)

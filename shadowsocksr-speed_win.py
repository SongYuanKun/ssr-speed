import json
import socket
import subprocess

from ParseSsr import ssr2json
from get_config import queryFrom_SSR_SHARE, queryFrom_youneed1, queryFrom_youneed2
from my_speed_test import test_ssr

default_socket = socket.socket


# 运行 ssr
def run_ssr():
    ssr_path = "D:\SSR\ShadowsocksR-dotnet4.0.exe"
    subprocess.Popen(ssr_path)


# 关闭ssr
def close_ssr():
    subprocess.call('taskkill /f /im ShadowsocksR-dotnet4.0.exe', stdout=subprocess.PIPE)


if __name__ == '__main__':

    test_option = {'ping': True, 'network': True, 'speed': True, 'youtube': True}
    max_cols = 0
    # 访问 youtube 网页加载时间大于设置时间直接退出不进行测速.解决高延迟的节点加载网页太慢问题
    youtube_timeout = 10
    # 使用 访问ip.sb获取外网ip的超时时间,判断节点是否能正常访问网页的依据
    network_timeout = 15

    ssr_config = []
    speed_result = []

    to_test_list = queryFrom_SSR_SHARE()

    to_test_list.extend(queryFrom_youneed1())
    to_test_list.extend(queryFrom_youneed2())

    print('to_test_urls=', to_test_list)

    file_path = "D:\SSR\gui-config.json"
    with open(file_path, 'r', encoding='utf-8') as f:
        file_config = json.load(f)
    configs = file_config['configs']

    for ssr_url in to_test_list:
        config = ssr2json(ssr_url)
        have_this = 0
        for x in configs:
            if x['server'] == config['server']:
                have_this = 1
        if have_this == 0 and test_ssr(config):
            configs.append(config)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(file_config, f, indent=2)
    run_ssr()

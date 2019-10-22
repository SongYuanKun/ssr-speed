import urllib


def get_from_subscribe():
    url = input("url:")
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    f = urllib.request.Request(url, headers=headers)
    ssr_subscribe = urllib.request.urlopen(f).read().decode('utf-8')  # 获取ssr订阅链接中数据
    print(ssr_subscribe)

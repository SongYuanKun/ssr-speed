import base64
import hashlib


def ssr2json(text):
    if text.startswith('ssr://'):
        text = text[6:]
        return ssrDecode(text)
    elif text.startswith('ss://'):
        text = text[5:]
        return ssDecode(text)
    return


def trim(s):
    if len(s) == 0:
        return ''
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == '':
        return trim(s[:-1])
    else:
        return s


def cleanupBase64(dirty):
    if trim(dirty):
        dirty = trim(dirty)
    else:
        dirty = dirty.replace('/^\s+|\s+$/g', '')
    dirty = dirty.replace('/[^+\/0-9A-Za-z-_]/g', '')
    if len(dirty) < 2:
        return ''
    while len(dirty) % 4 != 0:
        dirty = dirty + '='
    return dirty


def ssrDecode(text):
    md5 = hashlib.md5(text.encode('utf-8')).hexdigest().upper()
    data = base64.urlsafe_b64decode(cleanupBase64(text)).decode('utf-8')
    arr = data.split('/?')[0].split(':')
    arr2 = data.split('/?')[1].split('&')
    password = base64.urlsafe_b64decode(cleanupBase64(arr[5].split('/?')[0])).decode('utf-8')
    ip = arr[0]
    port = arr[1]
    obfs = arr[4]
    method = arr[3]
    protocol = arr[2]
    obfsparam = ""
    protoparam = ""
    remarks = ""
    remarks_base64 = ""
    group = ""

    for f in arr2:  # 第二个实例
        kv = f.split('=')
        try:
            v = base64.urlsafe_b64decode(cleanupBase64(kv[1])).decode('utf-8')
            if kv[0] == 'obfsparam':
                obfsparam = v
            elif kv[0] == 'protoparam':
                protoparam = v
            elif kv[0] == 'remarks':
                remarks = v
                remarks_base64 = kv[1]
            elif kv[0] == 'group':
                group = v
        except Exception as e:
            print(e)
            continue
    res = {
        "remarks": remarks,
        "id": md5,
        "server": ip,
        "server_port": int(port),
        "server_udp_port": 0,
        "password": password,
        "method": method,
        "protocol": protocol,
        "protocolparam": protoparam,
        "obfs": obfs,
        "obfsparam": obfsparam,
        "remarks_base64": remarks_base64,
        "group": group,
        "enable": True,
        "udp_over_tcp": False
    }
    return res


def ssDecode(text):
    data = base64.b64decode(text.encode('utf-8'))
    arr = str(data, encoding="utf8").split(':')
    method = arr[0]
    ip = arr[1].split('@')[1]
    password = arr[1].split('@')[0]
    port = arr[2]
    return {
        "server": ip,
        "server_port": port,
        "password": password,
        "method": method
    }


if __name__ == '__main__':
    result = ssr2json(
        "ss://eGNoYWNoYTIwLWlldGYtcG9seTEzMDU6dC5tZS9TU1JTVUI=@v9.ssrsub.xyz:8080/?plugin=obfs-local%3Bobfs%3Dhttp%3Bobfs-host%3Ddata.video.qiyi.com#@SSRSUB-%E5%8A%A0%E6%8B%BF%E5%A4%A79-%E4%BB%98%E8%B4%B9SSR%E6%8E%A8%E8%8D%90:t.cn/EGJIyrl")
    print(result)

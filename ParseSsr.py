import base64


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
    text = cleanupBase64(text)
    data = base64.b64decode(text.encode('utf-8'))
    arr = str(data, encoding="utf8").split('/?')[0].split(':')
    arr2 = str(data, encoding="utf8").split('/?')[1].split('&')
    result1 = str(base64.b64decode(cleanupBase64(arr[5].split('/?')[0]).encode('utf-8')), encoding="utf8")
    ip = arr[0]
    port = arr[1]
    password = result1
    obfs = arr[4]
    method = arr[3]
    protocol = arr[2]
    obfsparam = ""
    protoparam = ""
    remarks = ""
    group = ""

    for fruit in arr2:  # 第二个实例
        ls = fruit.split('=')
        if ls[0] == 'obfsparam':
            obfsparam = str(base64.b64decode(cleanupBase64(ls[1])), encoding="utf8")
        elif ls[0] == 'protoparam':
            protoparam = str(base64.b64decode(cleanupBase64(ls[1])), encoding="utf8")
        elif ls[0] == 'remarks':
            remarks = str(base64.b64decode(cleanupBase64(ls[1])), encoding="utf8")
        elif ls[0] == 'group':
            group = str(base64.b64decode(cleanupBase64(ls[1])), encoding="utf8")

    res = {
        "server": ip,
        "port": port,
        "protocol": protocol,
        "method": method,
        "password": password,
        "obfs": obfs,
        "obfsparam": obfsparam,
        "remarks": remarks,
        "group": group,
        "protoparam": protoparam,
        "protocolparam": "",
        "server_port": port
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

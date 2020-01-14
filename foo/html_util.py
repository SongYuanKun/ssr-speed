from bs4 import BeautifulSoup

proxy_handler = {
    'http': '127.0.0.1:1081',
    'https': '127.0.0.1:1081'
}


def format_response(response):
    html = response.content.decode('utf-8') \
        .replace("\\\"", "\"").replace("\\r", "\r") \
        .replace("\\n", "\n").replace("\\t", "\t") \
        .replace("\\/", "/").replace("/\"", "\"") \
        .replace("<br/>", ",")
    return BeautifulSoup(html, 'html5lib')

import json

file_path = r"D:\SSR\gui-config.json"
test_file_path = r"D:\SSR\gui-config.json"


def get_properties():
    with open(file_path, 'r', encoding='utf-8') as f:
        file_config = json.load(f)
    return file_config


def save_properties(file_config):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(file_config, f, indent=2)


def write_test_json(write_config):
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

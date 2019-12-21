import json

file_path = r"D:\SSR\gui-config.json"


def get_properties():
    with open(file_path, 'r', encoding='utf-8') as f:
        file_config = json.load(f)
    return file_config


def save_properties(file_config):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(file_config, f, indent=4)


def write_test_json(write_config):
    # 打开ssr config json
    json_path = r"..\bin\gui-config.json"
    write_configs(json_path, write_config)


def write_test_json2(write_config):
    # 打开ssr config json
    json_path = r"..\bin\temp2\gui-config.json"
    write_configs(json_path, write_config)


def write_test_json3(write_config):
    # 打开ssr config json
    json_path = r"..\bin\temp3\gui-config.json"
    write_configs(json_path, write_config)


def write_test_json4(write_config):
    # 打开ssr config json
    json_path = r"..\bin\temp4\gui-config.json"
    write_configs(json_path, write_config)


def write_configs(json_path, write_config):
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

import os
import yaml
from yaml import Loader
import sys
from setting.common import get_host_ip
from setting.config.merge_config import merge_config
from setting.config.setting_default import CONFIG


def get_addr():
    path = sys.argv[1]
    yaml_config: dict = yaml.load(open(os.path.join(path, "application.yaml")), Loader)
    config = merge_config(CONFIG, yaml_config)

    KUI_HOST = str(get_host_ip())
    KUI_PORT = str(config["PROJECT"]["PORT"])

    os.environ["KUI_PORT"] = str(config["PROJECT"]["PORT"])
    os.environ["KUI_HOST"] = str(get_host_ip())
    print(f"{KUI_HOST}:{KUI_PORT}")

    return KUI_HOST, KUI_PORT


result = get_addr()

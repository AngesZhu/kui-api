import os

import yaml
from yaml import CLoader as Loader
from setting.logger_config import logger
from setting.config.merge_config import merge_config
from setting.config.setting_default import CONFIG
from setting.config.setting_entity import SettingModel


__all__ = ["settings"]

# 获取环境变量
logger.info("""
 _                 _ _                                __ _       
| | ___   __ _  __| (_)_ __   __ _    ___ ___  _ __  / _(_) __ _ 
| |/ _ \ / _` |/ _` | | '_ \ / _` |  / __/ _ \| '_ \| |_| |/ _` |
| | (_) | (_| | (_| | | | | | (_| | | (_| (_) | | | |  _| | (_| |
|_|\___/ \__,_|\__,_|_|_| |_|\__, |  \___\___/|_| |_|_| |_|\__, |
                             |___/                         |___/ """)
logger.info("start the Kui Api application")

logger.info("loading environment configuration file")
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
yaml_config: dict = yaml.load(open(os.path.join(project_path, "application.yaml")), Loader)
config = merge_config(CONFIG, yaml_config)
settings = SettingModel(**config)
logger.info("loading environment configuration file end")

import os

PROJECT = {
    "BASE_PATH": os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
}

SWAGGER = {
    "SHOW": True,
    "TITLE": "Kui API 应用接口文档",
    "VERSION": "0.0.1",
    "DESCRIPTION": "Kui API 后端服务应用",
    "DOCS_URL": "/api/docs",
    "REDOC_URL": "/api/redoc",
}
ACCESS = {
    "ACCESS_TOKEN_EXPIRE_MINUTES": 1350000,      # 60*60*24*15
    "ALGORITHM": "HS256",
    "SECRET_KEY": "aeq)s(*&(&)()WEQasd8**&^9asda_asdasd*&*&^+_sda_dev"
}

RPC = {
    "TITLE": "Kui RPC 应用接口文档",
    "VERSION": "0.0.1",
    "DESCRIPTION": "Kui RPC 后端服务应用",
}

CONFIG = {
    "PROJECT": PROJECT,
    "SWAGGER": SWAGGER,
    "ACCESS": ACCESS,
    "RPC": RPC,
    # token过期时间 15天
    "ACCESS_TOKEN_EXPIRE_MINUTES": 60 * 60 * 24 * 15,
    # 生成token的加密算法
    "ALGORITHM": "HS256",
    # 生产环境保管好 SECRET_KEY
    "SECRET_KEY": 'aeq)s(*&(&)()WEQasd8**&^9asda_asdasd*&*&^+_sda_dev',

    # 项目根路径
    "BASE_PATH": os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__))))),
}
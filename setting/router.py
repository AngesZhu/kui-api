from kui.wsgi import Routes, allow_cors
from kui.wsgi.openapi import OpenAPI

from setting import logger, settings
from setting.common.routes_utils import loading_routes

__all__ = ["router"]

router = Routes(http_middlewares=[allow_cors()])

"""
根据配置加载路由，不需要自己一个一个添加，只需要在对应的app内编写完路由对象
"""
applications = {
    # "default": {
    #     "describe": "默认路由",
    #     "path": "api", # 路由分组
    #     "modules": ("Apps.xxx", "Apps.xxx"),  # 路由导入路径
    #     "routes_method": "routers", # 路由对象名称
    #     "middlewares": ("middleware.operation_middleware") # 导入中间件
    # },
    # "admin": {
    #     "describe": "admin相关接口",
    #     "path": "admin",
    #     "modules": ("Apps.xxx"),
    #     "routes_method": "routers",
    #     "middlewares": ("middleware.mark_middleware")
    # },
}

logger.info("loading routes from config")
router << loading_routes(applications)
logger.info("loading routes from config complete")

if settings.SWAGGER.SHOW:
    logger.info("allow loading swagger routes")
    _swagger_info = {
        "title": settings.SWAGGER.TITLE,
        "version": settings.SWAGGER.VERSION,
        "description": settings.SWAGGER.DESCRIPTION
    }
    swagger = OpenAPI(info=_swagger_info, template_name="swagger")
    redoc = OpenAPI(info=_swagger_info, template_name="redoc",)

    router << settings.SWAGGER.DOCS_URL // Routes(swagger.routes, namespace="swagger")
    router << settings.SWAGGER.REDOC_URL // Routes(redoc.routes, namespace="apidoc")
    logger.info("loading swagger routes complete")

from kui.wsgi import Header, Depends
from typing import Any, Union, Optional
from middleware.utils.jwt_token import check_token
from setting.register import response_code


def check_jwt_token(
        token: Optional[str] = Header(None, alias="X-Token", description="登录token")
) -> Union[str, Any]:
    """
    解析验证token  默认验证headers里面为token字段的数据
    可以给 headers 里面token替换别名, 以下示例为 X-Token
    token: Optional[str] = Header(None, alias="X-Token")
    :param token:
    :return:
    """
    res, msg = check_token(token)
    if res:
        return msg
    else:
        return response_code.error_400(message=msg)


def admin_middleware(endpoint):
    """
    ops操作权限-；临时版，只判断是否是活跃用户和管理员用户
    :param :
    :return:
    """
    # @functools.wraps(endpoint)
    def wrapper(user_info: Optional[dict] = Depends(check_jwt_token)):
        if user_info["admin"] and user_info["active"]:
            return endpoint()
        return response_code.error_400(message="No operation permission")
    return wrapper


def mark_middleware(endpoint):
    """
    验证请求是否符合合法要求
    :param endpoint:
    :param mark: 请求标记
    :return:
    """
    def wrapper(mark: Optional[str | None] = Header(None, alias="X-Mark")):
        if mark in ("web", "ops"):
            return endpoint()
        return response_code.error_400(message="Illegal Request")
    return wrapper

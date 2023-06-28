from typing import Optional
from kui.parameters.field_functions import Depends
from middleware import check_jwt_token

__all__ = ["token_middleware"]


def token_middleware(endpoint):
    def wrapper(user_info: Optional[dict] = Depends(check_jwt_token)):
        return endpoint()
    return wrapper


"""
    # def wrapper(token: Optional[str] = Header(None, alias='X-Token', description='登录token')):
    #     res, msg = check_token(token)
    #     if res:
    #         return endpoint()
    #     else:
    #         return response_code.error_400(message=msg)
    # return wrapper
"""

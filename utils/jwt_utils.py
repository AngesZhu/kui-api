import time
import jwt
from setting.config import settings


class JwtUtils:
    """
    模块使用PyJwt实现
    更多功能与用法，详见PyJwt文档：https://pyjwt.readthedocs.io/en/stable/
    """

    @staticmethod
    def create_token(user_info: dict) -> str:
        time_int = time.time()
        data = {
            "iat": int(time_int),
            "exp": int(time_int)+settings.ACCESS_TOKEN_EXPIRE_MINUTES,
            # "exp": int(time_int)-86400*15,
            "userId": int(user_info["userId"]),
            "userName": user_info["userName"],
            "active": user_info["active"],
            "admin": user_info["admin"],
        }
        # headers
        headers = {
            'alg': "HS256",  # 声明所使用的算法
            "typ": "JWT"
        }
        # 调用jwt库,生成json web token
        jwt_token = jwt.encode(data,
                               settings.SECRET_KEY,
                               algorithm=settings.ALGORITHM,
                               headers=headers)
        return jwt_token

    @staticmethod
    def verify_token(token: str) -> tuple:
        try:
            res_data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            return True, res_data
        except:
            return False, token


if __name__ == '__main__':
    token = JwtUtils.create_token({
        "userId": 1,
        "userName": "test",
        "active": 1,
        "admin": 0,
    })
    print(token)
    data = JwtUtils.verify_token(token)
    print(data)


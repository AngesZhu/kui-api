from typing import Optional

from setting.database import redis_client
from utils.jwt_utils import JwtUtils


def check_token(token: Optional[str]):
    if token:
        check_res = JwtUtils.verify_token(token)
        if check_res[0]:
            redis_token = redis_client.get("user_token:{}".format(check_res[1]["userId"]))
            if redis_token == token:
                return True, check_res[1]
            return False, "The token is expiration"
        return False, "The token is expiration"
    else:
        return False, "Please enter your user token"

import hashlib


def create_MD5(data):
    zt_pwd = hashlib.md5()
    zt_pwd.update(data.encode(encoding='utf-8'))
    return zt_pwd.hexdigest()



# if __name__ == '__main__':
#     print(MD5_login("aaa"))

<div align="center">
<h1>Kui Api</h1>

<p>
<img src="https://img.shields.io/pypi/pyversions/index.py" alt="PyPI - Python Version" />
</p>
Kui 服务端 Api 模版项目<br>
</div>

---

**Kui Api** 基于 [Kui](https://github.com/abersheeran/kui) 与 [PyRpc](https://github.com/abersheeran/rpc.py) 框架搭建，实现 HTTP 与 RPC 协议整合，
可采用多应用插拔模式实现的微服务架构，[Kui 使用文档](https://kui.aber.sh/) 。

整体分为以下几个模块

- 【基础模块】utils
- 【中间件】middleware
- 【项目配置】setting
  - common 基础方法封装
  - config 项目配置类以及默认配置
  - database 数据库相关封装（sqlalchemy）
  - register 应用内封装
  - schedule 任务封装
  - logger_config 日志封装
  - router 路由加载
  - server 应用封装


## 项目启动
> Python环境：3.7 及以上版本

### 环境依赖

**安装 Poetry**
```
pip install poetry
```

**进入项目后执行**
```
poetry install
```

### 项目启动

**文件直接启动**

- 直接执行 main.py 文件

**gunicorn直接启动**


- 执行
```
gunicorn main:app
```

**脚本启动（runweb）**
```shell
执行文件 start.sh
```
> 关于runweb，详情见：https://github.com/abersheeran/runweb


## 项目配置
> 使用中，若需添加新配置，除了在配置文件中添加外，还需在setting_entity.py文件中维护相对应的配置对象
```
# 默认配置
*/setting/config/setting_deafult.py

# 其他配置
*application.yaml
```




* 2019-06-22, 配置Web服务器(IIS)上线
* 2019-06-15, 增加：随机数应用
* 2019-06-13, 增加专业资讯采集


### 运行提示

```

    命令行-运行参数
    pynews.py <city|id> <link|cont|0|auto> [test]
        argv[0] : 运行文件
        argv[1] : 城市(eg.dg)或规则id(eg.1024)或数据id(eg.5678)或不限(eg.0)
        argv[2] : link:采集网址, cont:采集详情, 0:link+cont, auto:备用
        argv[3] : 可选, 不为空即当成`test`模式,测试规则不保存到数据库
    eg: 
        - pynews.py 1025 link test --- 测试-规则id=1025 的列表规则
        - pynews.py dg   link      --- 采集-所有dg规则 的网址
        - pynews.py 1024 link      --- 采集-规则id=1024 的网址
        - pynews.py 5678 cont test --- 测试-数据id=5678 的详情规则
        - pynews.py dg   cont      --- 采集-所有dg规则 的详情
        - pynews.py 5678 cont      --- 采集-数据id=5678 的详情
        - pynews.py 0    0         --- 采集所有 - 网址和详情
```

### 重要文件

* /trunk/app/
  - web.py    # Py-Web服务器/调试规则
  - pynews.py # 新闻采集-命令行执行
  - pynm.py   # 新闻采集-多进程执行(执行所有规则,手动设置分组)

* /trunk/app/libs/
  - cjnews.py # 新闻采集类
  - cjtool.py # 采集工具函数
  - mpnews.py # 多进程新闻采集类

* /trunk/views/front/npa/
  - Py-Web端 - 调试规则 - 模板

--- --- --- --- --- --- --- --- --- --- --- 
--- --- --- --- --- --- --- --- --- --- --- 

* 2018-03-25, (v1.1) 继续爬：完善多进程采集

--- --- --- --- --- --- --- --- --- --- --- 
--- --- --- --- --- --- --- --- --- --- --- 

### 微爬(Wepy) - /trunk/app

生活是艰难的：甚至需要爬……  
Weipa, Weipy, Wepy, 微爬 …… 又是失眠中名字出来了！ 但是：微爬(Wepy)，尽量让您轻松愉快的爬知识，爬价值，爬乐趣！

微爬(Wepy,Wepthon)：是一款轻量、免费、共享的通用Python微框架；适用于CMS开发,爬虫开发！  
基于 Python, Flask/Blueprint/jinja, Mysql/Sqlite, PyQuery 等开源模块开发  
基于Blueprint分组扩展，基于MKV的控制器/方法扩展  
环境需求：Python3+, Flask(Jinja2,Werkzeug), Mysql/Sqlite, PyQuery  


### 微爬(Wepy) - 安装配置

* 环境安装
  - Python环境：Python3.5+, 
  - 第三方模块：sqlite3, flask, pymysql, requests, pyquery

* 安装Mysql数据库（爬虫要用）
  - 安装Mysql数据库
  - 导入表数据：/trunk/app/data/wepy.sql

* 配置应用
  - 文件：appcfg.ini
  - 特别提示：配置链接Mysql数据库 `[cdb]` 相关参数

* 运行应用
  - 直接运行：/trunk/app/web.py
  - win模式下，可点 /trunk/run.cmd，直接进入命令行
  - 访问：http://127.0.0.1:5000/ (端口可在`appcfg.ini`配置中修改)


### 微爬(Wepy) - 目录结构

* 如下。
  标记有：Porsonal Test Code! 的，可直接删除！

```
    /branches/                 --- Porsonal Test Code!
      - /ex100/          
      - /ex200/          
      - /hipy/      
    /trunk/_cache/             --- 缓存目录           
    /trunk/app/                --- 微爬(Wepy)
      - /ctrls/        - 控制器
      - /data/         - db, config
      - /static/       - js,css 资源
      - /views/        - 模板
      - /web.py       - 运行入口
      - /mpa.py       - 命令行-多进程运行入口(有点鸡肋味道)
    /trunk/blog/               --- 单独blog演示 (v1)
    /trunk/core/               --- 核心库包
    /trunk/import/             --- 导入库包
    /trunk/impui/              --- 外部UI库
    /trunk/test/               --- Porsonal Test Code!
```


### 微爬(Wepy) - 问题遗留

* 多进程 目前只能在命令行运行；
* Blueprint下 session/cookie 的问题；



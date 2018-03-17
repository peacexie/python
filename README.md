

生活是艰难的：甚至需要爬……
Weipa, Weipy, Wepy, 微爬 …… 又是失眠中名字出来了！ 但是：微爬(Wepy)，尽量让您轻松愉快的爬知识，爬价值，爬乐趣！


### 微爬(Wepy) - /trunk/app

微爬(Wepy,Wepthon)：是一款轻量、免费、共享的通用Python微框架；适用于CMS开发,爬虫开发！
基于 Python, Flask/Blueprint/jinja, Mysql/Sqlite, PyQuery 等开源模块开发
基于Blueprint分组扩展，基于MKV的控制器/方法扩展
环境需求：Python3+, Flask(Jinja2,Werkzeug), Mysql/Sqlite, PyQuery


### 微爬(Wepy) - 目录结构

* app-目录结构

```
    /branches/           --- Porsonal Test Code!
      - /ex100/    
      - /ex200/    
      - /hipy/     
    /trunk/app/          --- 微爬(Wepy)
      - /_cache/  - 缓存目录
      - /data/    - db, config
      - /static/  - js,css 资源
      - /views/   - 模板
      - /webc.py  - 运行入口
    /blog/               --- 单独blog演示
    /core/               --- 核心库包
    /import/             --- 导入库包
    /impui/              --- 外部UI库
    /test/               --- Porsonal Test Code!
```


### 微爬(Wepy) - 问题遗留

* 多进程在 Flask-Request 下运行问题
* 命令行模式下 无上下文 使用 Flask-g 问题
* Blueprint下 session/cookie 使用



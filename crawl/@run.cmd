
@echo off

goto main
:: Readme

    > web.py # web服务器/调试规则
    > run.py # 命令行执行

    命令行-运行参数
    run.py <city|id> <link|cont|0|auto> [test]
    argv[0] : 运行文件
    argv[1] : 城市(eg.dg)或规则id(eg.1024)或数据id(eg.5678)或不限(eg.0)
    argv[2] : link:采集网址, cont:采集详情, 0:link+cont, auto:备用
    argv[3] : 可选, 不为空即当成`test`模式,测试规则不保存到数据库
    eg: 
        - run.py 1025 link test --- 测试-规则id=1025 的列表规则
        - run.py dg   link      --- 采集-所有dg规则 的网址
        - run.py 1024 link      --- 采集-规则id=1024 的网址
        - run.py 5678 cont test --- 测试-数据id=5678 的详情规则
        - run.py dg   cont      --- 采集-所有dg规则 的详情
        - run.py 5678 cont      --- 采集-数据id=5678 的详情
        - run.py 0    0         --- 采集所有 - 网址和详情

:: Read-end
:main

cmd
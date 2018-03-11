#coding=UTF-8

import os, sys, time
from flask import Flask, Blueprint, redirect, g, render_template, abort
from core import config, dbop, jef, vext

def web():
    cfgs = config.init()
    timer = time.time()
    root = os.getcwd()
    web = Flask(__name__, template_folder=root+cfgs['dir']['views'], 
                          static_folder=root+cfgs['dir']['static'])
    cfgs = config.init()
    for key in cfgs['sys']:
        web.config[key.upper()] = cfgs['sys'][key]
    cfgs['sys']['timer'] = timer
    cfgs['sys']['root'] = root
    rfiles = cfgs['sys']['rfiles'].split(',')
    for file in rfiles:
        breg(web, cfgs, file, 1) 
    groups = cfgs['sys']['groups'].split(',')
    for group in groups:
        breg(web, cfgs, group)
    areg(web, cfgs) #print(web.url_map)
    return web

# 注册web/g扩展
def areg(web, cfgs):
    # reg-filters 
    web.jinja_env.filters['url'] = jef.url
    web.jinja_env.filters['info'] = jef.info
    web.jinja_env.filters['get'] = jef.get
    web.jinja_env.filters['exe'] = jef.exe
    # reg-funcs 
    @web.before_request
    def before_request():
        cfgs['run']['timer'] = time.time()
        g.db = dbop.dbm(cfgs['cdb'])
    def teardown_request(exception):
        if hasattr(g, 'db'):
            g.db.close()
    ''' 
    @web.errorhandler(404)  
    def not_found(e):      
        return render_template("root/home/error.htm")
    @web.teardown_request

    '''

# 注册Blueprint
def breg(web, cfgs, group, file=0):
    sview = Blueprint(group, '_'+group.replace('.','_'))
    gfix = ''
    if file==0:
        @sview.route('/')
        @sview.route('/<mkv>')
        def svmkv(mkv=''):
            return view(web, group, cfgs, mkv)
        if len(group)>0:
            gfix = '/' + group
    else: # robots.txt
        exts = os.path.splitext(group)
        gfix = '/' + exts[0]
        @sview.route(exts[1])
        def svfile(mkv=''):
            return vext.vrfp(group);
    web.register_blueprint(sview, url_prefix=gfix)

# 一个分组的view显示
def view(web, group, cfgs, mkv):
    g.run = {} #; print(g.db); print(g);  
    cfgs['mkvs'] = mkvs(group, mkv)
    for key in cfgs:
        setattr(g, key, cfgs[key])
    tpath = g.dir['views'] + '/' + g.mkvs['group']
    d = tpname(tpath) # 模板和基本数据
    data = cdata(web, tpath)
    if 'd' in data: # 返回res覆盖原有属性
        d = dict(d, **data['d'])
        del data['d']
    d['data'] = data
    vext.verr(d)
    if d['tpname']=='dir':
        return redirect(d['message'], code=301)
    elif '(,json,xml,jsonp,)'.find(','+d['tpname']+',')>0:
        return vext.vmft(d)
    else:
        return render_template(d['full'], d=d), d['code']

# 一个`Ctrl`控制器的数据 
def cdata(web, tpath):
    
    file = g.mkvs['group'] +'_'+ g.mkvs['mod'] + 'Ctrl'
    flag = os.path.exists(g.dir['views']+'/_ctrls/'+file+'.py') # v2
    if not flag:
        return {'__msg': 'None ['+file+'] Class'}
    g.run['Ctrl'] = file
    items = __import__('_ctrls.'+file) # v1/v2
    ctrl = getattr(items, file)
    cobj = ctrl.main(web)
    tabs = g.mkvs['key'] +','+ '_'+g.mkvs['type'] + ',_def'
    taba = tabs.split(',')
    for fid in taba:
        func = fid + 'Act'
        if func in dir(cobj):
            g.run['Act'] = func
            method = getattr(cobj, func) 
            return method()
    return {'__msg': 'None ['+tabs+'] Action'}

# 分析模板和基本数据
def tpname(tpath):
    tpnow = g.mkvs['tpname']
    tpdef = g.mkvs['tpdef']
    tpext = g.dir['tpext']
    flag = os.path.exists(tpath + '/' + tpnow + tpext)
    d = {'group':g.mkvs['group'], 'tpath':tpath, 'tpname':tpnow, 'code':200, 'message':''}
    if not flag: 
        if os.path.exists(tpath + '/' + tpdef + tpext):
            d['tpname'] = tpdef
        else:
            d['tpdef'] = tpnow
            d['tpname'] = ''
    return d

# 分析mkv
def mkvs(group, mkv):
    vtype = 'mhome'
    if len(group)==0:     # </root>/info
        group = 'root'
        hmod = mkv.find('.')>0 or mkv.find('-')>0
        mkv = mkv if hmod else 'home-' + ('index' if len(mkv)==0 else mkv)
    elif len(mkv)==0:     # /front/
        mkv = 'home-index'
    elif mkv.find('.')>0: # /front/news.nid
        vtype = 'detail'
    elif mkv.find('-')>0: # /front/news-cid
        vtype = 'mtype'
    else:                 # /front/news
        mkv = mkv + '-index'
    tmp = mkv.split('.') if mkv.find('.')>0 else mkv.split('-')
    view = tmp[2] if len(tmp)>=3 else ''
    mkva = {'type':vtype, 'mod':tmp[0], 'key':tmp[1], 'view':view}
    tpnow = tmp[0] +'/'+ ('detail' if mkv.find('.')>0 else tmp[1])
    tpdef = tmp[0] +'/'+ vtype
    exts = {'group':group, 'mkv':mkv, 'tpname':tpnow, 'tpdef':tpdef}
    res = dict(mkva, **exts)
    return res

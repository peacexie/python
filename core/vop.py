#coding=UTF-8

import os, sys, time
from flask import Flask, Blueprint, redirect, g, render_template, abort
from core import config, dbop, jef, vext

def app():
    cfgs = config.init()
    timer = time.time()
    root = os.getcwd()
    app = Flask(__name__, template_folder=root+cfgs['dir']['views'], 
                          static_folder=root+cfgs['dir']['static'])
    cfgs = config.init()
    for key in cfgs['sys']:
        app.config[key.upper()] = cfgs['sys'][key]
    cfgs['sys']['timer'] = timer
    cfgs['sys']['root'] = root
    rfiles = cfgs['sys']['rfiles'].split(',')
    for file in rfiles:
        breg(app, cfgs, file, 1) 
    groups = cfgs['sys']['groups'].split(',')
    for group in groups:
        breg(app, cfgs, group)
    areg(app, cfgs) #print(app.url_map)
    return app

# 注册app/g扩展
def areg(app, cfgs):
    # reg-filters 
    app.jinja_env.filters['url'] = jef.url
    app.jinja_env.filters['info'] = jef.info
    app.jinja_env.filters['get'] = jef.get
    app.jinja_env.filters['exe'] = jef.exe
    # reg-funcs 
    @app.before_request
    def before_request():
        cfgs['run']['timer'] = time.time()
        g.db = dbop.dbm(cfgs['cdb'])
    def teardown_request(exception):
        if hasattr(g, 'db'):
            g.db.close()
    ''' 
    @app.errorhandler(404)  
    def not_found(e):      
        return render_template("root/home/error.htm")
    @app.teardown_request

    '''

# 注册Blueprint
def breg(app, cfgs, group, file=0):
    sview = Blueprint(group, '_'+group.replace('.','_'))
    gfix = ''
    if file==0:
        @sview.route('/')
        @sview.route('/<mkv>')
        def svmkv(mkv=''):
            return view(app, group, cfgs, mkv)
        if len(group)>0:
            gfix = '/' + group
    else: # robots.txt
        exts = os.path.splitext(group)
        gfix = '/' + exts[0]
        @sview.route(exts[1])
        def svfile(mkv=''):
            return vext.vrfp(group);
    app.register_blueprint(sview, url_prefix=gfix)

# 一个分组的view显示
def view(app, group, cfgs, mkv):
    g.run = {} #; print(g.db); print(g);  
    cfgs['mkvs'] = mkvs(group, mkv)
    for key in cfgs:
        setattr(g, key, cfgs[key])
    tpath = g.dir['views'] + '/' + g.mkvs['group']
    d = tpname(tpath) # 模板和基本数据
    data = cdata(app, tpath)
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
def cdata(app, tpath):
    
    file = g.mkvs['mod'] + 'Ctrl' # v1
    file = g.mkvs['group'] +'_'+ g.mkvs['mod'] + 'Ctrl' # v2 # /veiws/_ctrls/root_homeCtrl.py
    #flag = os.path.exists('.'+tpath+'/_ctrls/'+file+'.py') # v1
    flag = os.path.exists(g.dir['views']+'/_ctrls/'+file+'.py') # v2
    if not flag:
        return {'__msg': 'None ['+file+'] Class'}
    #sys.path.append('.'+tpath) # v1
    #sys.path.append(g.dir['views']) # v2
    g.run['Ctrl'] = file
    # ('archives.user',fromlist = ('user',))
    items = __import__('_ctrls.'+file) # v1/v2
    #items = __import__(g.mkvs['group']+'._ctrls', fromlist=(file,)) # v3
    ctrl = getattr(items, file)
    cobj = ctrl.main(app)
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

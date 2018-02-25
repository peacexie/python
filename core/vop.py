
import os, sys, json
from flask import Blueprint, request, g, render_template, abort
from core import config

# 按分组运行
def vrun(app):
    cfgs = config.init()
    for key in cfgs['sys']:
        app.config[key.upper()] = cfgs['sys'][key]
    groups = cfgs['sys']['groups'].split(',')
    for group in groups:
        vreg(app, group, cfgs)

# 注册分组
def vreg(app, group, cfgs):
    sview = Blueprint(group, '_'+group)
    @sview.route('/')
    @sview.route('/<mkv>')
    def svmkv(mkv=''):
        return view(app, group, cfgs, mkv)
    gfix = '' if len(group)==0 else '/'+group
    app.register_blueprint(sview, url_prefix=gfix)
    app.jinja_env.filters['url'] = jef_url

# 一个分组的view显示
def view(app, group, cfgs, mkv):
    g.run = {} #; print(request); print(g);  
    cfgs['mkvs'] = mkvs(group, mkv)
    for key in cfgs:
        setattr(g, key, cfgs[key])
    tpath = g.dir['tpls'] + '/' + g.mkvs['group']
    d = tpname(g, tpath) # 模板和基本数据
    data = cdata(app, request, g, tpath)
    if 'd' in data: # 返回res覆盖原有属性
        d = dict(d, **data['d'])
        del data['d']
    d['data'] = data
    verr(g, d)
    if '(,json,xml,jsonp,)'.find(','+d['tpname']+',')>0:
        return vfmt(d, d['tpname']) # head怎么改变?
    else:
        return render_template(d['full'], d=d)

def vfmt(d, fmt):
    if fmt=='xml':
        s = 'Coming Soon!'
    else: # json/jsonp(有callback)
        s = json.dumps(d, ensure_ascii=False)
        cb = request.args.get('callback')
        if cb:
            s = cb + '(' + s + ');'
    return s

# 错误处理
def verr(g, d):
    if len(d['tpname'])==0:
        d['code'] = 404
        d['message'] = '[' + d['tpath'] + '/' + d['tpdef'] + '] Template NOT Found!'
    if d['group']=='root' and g.mkvs['mkv']=='home-error':
        d['code'] = 403
        d['message'] = '[/error] HTTP 403 Forbidden!'
    if d['code']>=400:
        if g.sys['debug']=='False':
            abort(d['code'], d['message'])
        tpnow = 'home/error'
    elif d['code']>=300:
        tpnow = 'home/info'
    if d['code']<300:
        d['full'] = d['group'] + '/' + d['tpname'] + g.dir['tpext']
    else:
        d['full'] = 'root' + '/' + tpnow + g.dir['tpext']
    #return d 

# 一个`Ctrl`控制器的数据 
def cdata(app, request, g, tpath):
    sys.path.append(tpath)
    file = g.mkvs['mod'] + 'Ctrl'
    flag = os.path.exists(tpath+'/_ctrls/'+file+'.py')
    if not flag:
        return {'__msg': 'None ['+file+'] Class'}
    g.run['Ctrl'] = file
    items = __import__('_ctrls.' + file)
    ctrl = getattr(items, file)
    cobj = ctrl.main(app, request, g)
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
def tpname(g, tpath):
    tpnow = g.mkvs['tpname']
    tpdef = g.mkvs['tpdef']
    tpext = g.dir['tpext']
    flag = os.path.exists(tpath + '/' + tpnow + tpext)
    d = {'group':g.mkvs['group'], 'tpath':tpath, 'tpname':tpnow, 'code':0, 'message':''}
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

# jinja_env.filters
# 暂无意义, 直接这样写: mod-key?parms 或 ../group/mod-key?parms
def jef_url(mkv, p=''):
    if mkv=='/':
        mkv = '/root/'
    elif mkv=='./':
        mkv = '/' + g.mkvs['group'] + '/'
    elif mkv.find('/')<0: # mkv
        mkv = '/' + g.mkvs['group'] + '/' + mkv
    #else: # /gid/mkv 
    #    mkv = mkv
    mkv = mkv.replace('/root/', '/')
    return mkv + ('?'+p  if len(p)>0 else '')

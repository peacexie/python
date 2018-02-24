
import os, sys
from flask import Blueprint, request, g, render_template, abort
from core import config

# 按分组运行
def vrun(app):
    cfgs = config.init()
    for key in cfgs['sys']:
        app.config[key.upper()] = cfgs['sys'][key]
    groups = cfgs['sys']['groups'].split(',')
    for group in groups:
        # 去掉内置group?
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

# 一个分组的view显示
def view(app, group, cfgs, mkv):
    g.run = {}
    cfgs['mkvs'] = mkvs(group, mkv)
    for key in cfgs:
        setattr(g, key, cfgs[key])
    tpath = g.dir['tpls'] + '/' + g.mkvs['group']
    d = tpname(g, tpath) # 数据结果
    data = cdata(app, request, g, tpath)
    if 'd' in data: # 返回res覆盖原有属性
        del data['d']
        d = dict(d, **data)
    d['data'] = data
    if d['code']>0:
        verr(g, d)
    #print(app); print(request); print(g);   
    tpfull = d['group'] + '/' + d['tpname'] + g.dir['tpext']
    return render_template(tpfull, d=d)

# 错误处理
def verr(g, d):
    if g.sys['debug']=='False':
        abort(404, d['message'])
    d['tpname'] = 'home/error'

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
    tabs = g.mkvs['key'] +','+ g.mkvs['type'] + ',_def'
    taba = tabs.split(',')
    for fid in taba:
        func = fid + 'Act'
        if func in dir(cobj):
            g.run['Act'] = func
            method = getattr(cobj, func) 
            return method()
    return {'__msg': 'None ['+tabs+'] Action'}

# 分析模板
def tpname(g, tpath):
    tpdef = g.mkvs['tpdef']
    tpext = g.dir['tpext']
    flag = os.path.exists(tpath + '/' + g.mkvs['tpname'] + tpext)
    res = {'group':g.mkvs['group'], 'tpath':tpath, 'tpname':g.mkvs['tpname'], 'code':0, 'message':''}
    if not flag: 
        if os.path.exists(tpath + '/' + tpdef + tpext):
            res['tpname'] = tpdef
        else:
            res['code'] = 404
            res['message'] = '[' + tpath + '/' + tpdef + '] Template NOT Found!'
    return res

# 分析mkv
def mkvs(group, mkv):
    vtype = 'index'
    if len(group)==0:     # </root>/info
        group = 'root'
        mkv = 'home-' + ('index' if len(mkv)==0 else mkv)
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
    tpname = tmp[0] +'/'+ ('detail' if mkv.find('.')>0 else tmp[1])
    tpdef = tmp[0] +'/'+ vtype
    exts = {'group':group, 'mkv':mkv, 'tpname':tpname, 'tpdef':tpdef}
    res = dict(mkva, **exts)
    return res

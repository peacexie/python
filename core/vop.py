
import os, sys
from flask import Blueprint, request, g, render_template, abort
from core import config

def run(app):
    cfgs = config.init()
    for key in cfgs['sys']:
        app.config[key.upper()] = cfgs['sys'][key]
    groups = cfgs['sys']['groups'].split(',')
    for group in groups:
        reg(app, group, cfgs)

def reg(app, group, cfgs):
    sview = Blueprint(group, '_'+group)
    @sview.route('/')
    @sview.route('/<mkv>')
    def svmkv(mkv=''):
        return view(app, group, cfgs, mkv)
    gfix = '' if len(group)==0 else '/'+group
    app.register_blueprint(sview, url_prefix=gfix)

def view(app, group, cfgs, mkv):
    cfgs['mkvs'] = mkvs(group, mkv)
    for key in cfgs:
        setattr(g, key, cfgs[key])
    d = vres(app, request, g) # setattr(g, 'd', d)
    #print(app); print(request); print(g);    
    tpfull = d['group']+'/'+d['tpname']+g.dir['tpext']
    return render_template(tpfull, d=d)

# res : group, tpath, tpname, code, message, data
def vres(app, request, g):
    g.run = {}
    tpath = g.dir['tpls'] + '/' + g.mkvs['group']
    ctrl = load(g, tpath)
    tpnow = tpname(g, tpath)
    res = {'group':g.mkvs['group'], 'tpath':tpath, 'tpname':tpnow, 'code':0, 'message':''}
    if(tpnow==''):
        res['tpname'] = 'home/error'
        res['code'] = 404
        res['message'] = '[' + tpath + '/' + g.run['tpbak'] + '] Template NOT Found!'
        #abort(404, 'Template NOT Found!') 
    if ctrl:
        cobj = ctrl.main(app, request, g)
        data = cdata(cobj, g.mkvs)
    else:
        data = {'__msg':'None Ctrl-Data'}
    res['data'] = data
    return res 

def cdata(cobj, mkvs):
    tabs = (mkvs['key'] +','+ mkvs['type'] + ',_def').split(',')
    for fid in tabs:
        func = fid + 'Act'
        if(func in dir(cobj)): #'testvar'   in   dir()
            method = getattr(cobj, func) 
            return method()
        #print(func+',,,,, ')
    return {'__msg':'None Ctrl-Data'}

def load(g, tpath):
    sys.path.append(tpath)
    file = g.mkvs['mod'] + 'Ctrl'
    flag = os.path.exists(tpath+'/_ctrls/'+file+'.py')
    if not flag:
        return False
    items = __import__('_ctrls.' + file)
    item = getattr(items, file)
    return item

def tpname(g, tpath):
    tpnow = g.mkvs['tpname']
    tpdef = g.mkvs['tpdef']
    tpext = g.dir['tpext'] 
    flag = os.path.exists(tpath + '/' + tpnow + tpext)
    if not flag: 
        if os.path.exists(tpath + '/' + tpdef + tpext):
            tpnow = tpdef
        else:
            g.run['tpbak'] = tpdef
            tpnow = ''
    return tpnow

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

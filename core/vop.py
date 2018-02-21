
import os, sys
from flask import Blueprint, request, g, render_template
from core import config
#from _ctrls import blogCtrl
#ctrl = blogCtrl.main(request, g, _cfgs)

def run(app):
    _cfgs = config.init()
    for key in _cfgs['sys']:
        app.config[key.upper()] = _cfgs['sys'][key]
    groups = _cfgs['sys']['groups'].split(',')
    for group in groups:
        views(app, group, _cfgs)

def views(app, group, _cfgs):
    sview = Blueprint(group, '__name_'+group)
    @sview.route('/')
    @sview.route('/<mkv>')
    def smkv(mkv=''):
        print(app); print(request); print(g); 
        gdir = 'root' if len(group)==0 else group
        return render_template(gdir + '/home/index.htm')
    gfix = '' if len(group)==0 else '/'+group
    app.register_blueprint(sview, url_prefix=gfix)

# res : data, state, tpname, code, message
# mkvs, http(code,message), data:list,detail,ext/side*
def vres(app, request, g, _cfgs):
    tpath = _cfgs['dir']['tpls'] + '/' + _cfgs['mkvs']['vgp']
    ctrl = load(_cfgs, tpath)
    tpdef = tpname(_cfgs, tpath)
    res = {'tpath':tpath, 'tpname':tpdef}
    if ctrl:
        cobj = ctrl.main(app, request, g, _cfgs)
        print(cobj)
    else:
        print(' xxxx2!!! ')
    #sys.exit()
    res['data'] = {}
    return res 

def load(_cfgs, tpath):
    sys.path.append(tpath)
    file = _cfgs['mkvs']['mod'] + 'Ctrl'
    flag = os.path.exists(tpath+'/_ctrls/'+file+'.py')
    if not flag:
        return False
    items = __import__('_ctrls.' + file)
    item = getattr(items, file)
    return item

def tpname(_cfgs, tpath):
    tpname = _cfgs['mkvs']['tpname']
    tpdef = _cfgs['mkvs']['tpname']
    flag = os.path.exists(tpath + tpname + _cfgs['dir']['tpext'])
    if not flag:
        tmp = tpath + tpdef + _cfgs['dir']['tpext']
        tpname = tpdef if(os.path.exists(tmp)) else 'root/home/error'
    return tpname

def mkvs(vgp, mkv):
    vgp = 'root' if len(vgp)==0 else vgp
    if len(mkv)==0:
        type = 'mhome'
        mkv = 'home-index'
    elif mkv.find('.')>0:
        type = 'detail'
    elif mkv.find('-')>0:
        type = 'mtype'
    else:
        type = 'mhome'
        mkv = mkv + '-index'
    tmp = mkv.split('.') if mkv.find('.')>0 else mkv.split('-')
    view = tmp[2] if len(tmp)>=3 else ''
    mkvs = {'type':type, 'mod':tmp[0], 'key':tmp[1], 'view':view}
    tpname = vgp +'/'+ tmp[0] +'/'+ ('detail' if mkv.find('.')>0 else tmp[1])
    tpdef = vgp +'/'+ tmp[0] +'/'+ type
    exts = {'vgp':vgp, mkv:mkv, 'tpname':tpname, 'tpdef':tpdef}
    res = dict(mkvs, **exts)
    #print(request); 
    #print(g)
    return res

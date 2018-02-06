
import os, sys
#from _ctrls import blogCtrl
#ctrl = blogCtrl.main(request, g, _cfgs)

# res : data, state, tpname, code, message
def vres(app, request, g, _cfgs):
    ctrl = load(_cfgs)
    if ctrl:
        cobj = ctrl.main(app, request, g, _cfgs)
        print(cobj)
    else:
        print(' xxxx!!! ')
    #sys.exit()
    res = {}
    return res

def load(_cfgs):
    gpath = _cfgs['envs']['rapp'] + "/templates/" + _cfgs['mkvs']['vgp']
    sys.path.append(gpath)
    file = _cfgs['mkvs']['mod'] + 'Ctrl'
    flag = os.path.exists(gpath+'/_ctrls/'+file+'.py')
    if not flag:
        return False
    items = __import__('_ctrls.' + file)
    item = getattr(items, file)
    return item

def tpname(mkvs):
    #
    return mkvs

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
    exts = {'vgp':vgp, mkv:mkv, 'tpname':tpname}
    res = dict(mkvs, **exts)
    return res

import sys, os
from flask import Blueprint, render_template
sview = Blueprint('admin', __name__)

os.path.basename(__file__)

@sview.route('/')
@sview.route('/<mkv>')
def smkv(mkv=''):
    return render_template('admin/home/index.htm')


"""
@app.route('/')
@app.route('/<mkv>')
def route(vgp='', mkv=''):
    #print(app.config['PORT'])
    _cfgs['mkvs'] = vop.mkvs(vgp, mkv)
    _vres = {'data':{}, 'vgp':vgp} # data, state, tpname, tpath
    #print(app); print(request); print(g); print(_cfgs)
    _vres = vop.vres(app, request, g, _cfgs)
    return render_template('root/index.htm', _cfgs=_cfgs, _vres=_vres)
"""
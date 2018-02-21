from flask import Blueprint, render_template
admin = Blueprint('admin', __name__)

@admin.route('/')
@admin.route('/<mkv>')
def index(mkv=''):
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

import os, sys, platform
import configparser

def app(app, _cfgs):
    for key in _cfgs['app']:
        app.config[key.upper()] = _cfgs['app'][key]
'''
    app.config['SECRET_KEY'] = '123456'  
    app.secret_key = '123456' 
'''

def init():
    _cfgs = {}
    _cfgs['envs'] = envs()
    bcfg = base(_cfgs['envs'])
    for key in bcfg: # app, path, db, blog ... 
        _cfgs[key] = bcfg[key]
    _cfgs['db']['path'] = _cfgs['envs']['root'] + _cfgs['db']['file']
    return _cfgs

def envs():
    envs = {}
    envs['root'] = os.path.dirname(os.path.dirname(__file__))
    envs['rapp'] = '.'
    sys.path.append(envs['root'] + "/import")
    envs['arc'] = platform.architecture()
    envs['sys'] = platform.system()
    envs['ver'] = platform.version()
    return envs

def base(envs):
    conf = configparser.ConfigParser()
    conf.read(envs['root']+"/data/config.ini", encoding="utf-8-sig")
    secs = conf.sections()
    base = {}
    for key in secs:
        base[key] = dict(conf.items(key))
    return base


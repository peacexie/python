
import os, sys, platform
import configparser

def init():
    _cfgs = {}
    _cfgs['envs'] = envs()
    bcfg = base(_cfgs['envs'])
    _cfgs['app'] = bcfg['app']
    _cfgs['path'] = bcfg['path']
    _cfgs['db'] = bcfg['db']
    _cfgs['db']['path'] = _cfgs['envs']['root'] + _cfgs['db']['file']
    return _cfgs

def envs():
    envs = {}
    envs['root'] = os.path.dirname(os.path.dirname(__file__)) # `..`
    sys.path.append(envs['root'] + "/import")
    envs['arc'] = platform.architecture()
    envs['sys'] = platform.system()
    envs['ver'] = platform.version()
    return envs

def base(envs):
    conf = configparser.ConfigParser()
    conf.read(envs['root'] + "/data/config.ini")
    secs = conf.sections()
    base = {}
    for key in secs:
        base[key] = dict(conf.items(key))
    return base


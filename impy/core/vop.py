
#import os, sys, platform
#import configparser

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

def tpname(mkvs):
    #
    return mkvs

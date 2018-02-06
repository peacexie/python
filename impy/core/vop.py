
#import os, sys, platform
#import configparser

def mkvs(vgp, mkv):
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
    mkvs = {'vgp':vgp, 'mkv':mkv, 'type':type, 'mod':tmp[0], 'key':tmp[1], 'view':view}
    return mkvs

def tpname(mkvs):
    #
    return mkvs

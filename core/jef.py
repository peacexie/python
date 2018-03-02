
import time
from flask import g

# jinja_env.filters
# 暂无意义, 直接这样写: mod-key?parms 或 ../group/mod-key?parms
def url(mkv, p=''):
    if mkv=='/':
        mkv = '/root/'
    elif mkv=='./':
        mkv = '/' + g.mkvs['group'] + '/'
    elif mkv.find('/')<0: # mkv
        mkv = '/' + g.mkvs['group'] + '/' + mkv
    #else: # /gid/mkv 
    #    mkv = mkv
    mkv = mkv.replace('/root/', '/')
    return mkv + ('?'+p  if len(p)>0 else '')

def info(p=''):
    timer = time.time()-g.run['timer']
    return round(timer, 2)
    # run:00.2(s), tpl:/views/tests/home/index, upd:2014-1234-34
    # Done:37.102/149.760(ms); 13(queries)/1.178(MB); Tpl:c_page/_home; Upd:2018-03-02 17:59:30

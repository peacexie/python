
import os,sys,platform
from core import config as _cfg

_cfg.path['root'] = os.path.dirname(os.path.dirname(__file__))
#sys.path.append(path['root'] + )
sys.path.append(_cfg.path['root'] + "/import")

_cfg.env['arc'] = platform.architecture()
_cfg.env['sys'] = platform.system()
_cfg.env['ver'] = platform.version()

#return _cfg
#print(_cfg)

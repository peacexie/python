#coding=UTF-8

import sys
sys.path.append(sys.path[0])
sys.path.append(sys.path[0] + "/../")

from core import vop
app = vop.web()

if __name__ == '__main__':
    app.run()

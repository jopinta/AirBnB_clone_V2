#!/usr/bin/python3
'''Fabric script that generates a .tgz archive'''

from fabric.api import run, local
from datetime import datetime


def do_pack():
    '''for the tgz'''
    try:
        local('mkdir -p versions')
        d_t = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_" + d_t + ".tgz"
        local("tar -cvzf" + filename + " web_static")
        return filename
    except:
        return None

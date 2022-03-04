#!/usr/bin/env python3
#a simple CLI interface for the auto physics experiment tool kits
#by regymm

import sys
import os
import getopt
from ftplib import FTP
import getpass


HomeDir = 'C:/Users/Admin/MyHome/PhysicsExp'


def usage():
    print('read the source code yourself to get help')


def wrong():
    print('something went wrong...')


def initnew(exptype):
    fn = ''
    if exptype == 'analyse':
        os.system('cp -vn ' + HomeDir + '/physicsexp/Template/analyse_template.py ./analyse.py')
        os.system('touch data.txt')
        # os.system('ln -sv /home/user/PhysicsExp/Core .')
    elif exptype == 'plot':
        os.system('cp -vn ' + HomeDir + '/physicsexp/Template/plot_template.py ./plot.py')
        # os.system('ln -sv /home/user/PhysicsExp/Core .')
        os.system('touch data.txt')
    else:
        print('wrong type!')
    print('init done.')


def upload(filename):
    # upload to qingmiyunyin print system, TODO
    pass


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:u:", ["help", "init=", "upload="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    if args:
        print('unhandled argument detected.')
        sys.exit(3)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--init"):
            initnew(a)
            sys.exit()
        elif o in ("-u", "--upload"):
            upload(a)
            sys.exit()
        else:
            wrong()
            sys.exit(2)


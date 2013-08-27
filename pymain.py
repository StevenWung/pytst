# -*- coding: utf-8 -*-


#from parsertest import parsetest
from optparse import OptionParser
import os

def parsetest():
    
    opt = OptionParser(version='0.1')
    opt.add_option('-x', '--xxx', help='this is a test', dest = 'xvalue', default='1')
    (options, args) = opt.parse_args()
    if options.xvalue == None:
        opt.print_help()
    else:
        print(os.path.abspath())


if __name__ == '__main__':
    parsetest()
    
    
    
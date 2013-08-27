#!/usr/bin/python
from optparse import OptionParser

def parsetest():
    
    opt = OptionParser(version='0.1')
    opt.add_option('-x', '--xxx', help='this is a test', dest = 'xvalue', default='1')
    (options, args) = opt.parse_args()
    #opt.print_help()
    if options.xvalue == None:
        opt.print_help()
    else:
        print(options.xvalue)
import os
import json
import ftplib
import logging

logging.debug("this test")
HOST = "****"
NAME = "***"
PASS = "***"
FILE = "test.txt"

OK = 0
ERROR_DIR_NOT_EXIST = 100
ERROR_DIR_DO_EXIST  = 101

class FtpUploader(object):
    def __init__(self, host, username, password, base_dir='/'):
        self.bdir = base_dir
        self.rdirs = []
        try:
            self.ftp = ftplib.FTP(host, username, password)
        except Exception,e:
            if 'cannot log in' in e.message:
                print "Login Error"
            else:
                raise e
        pass
    def _mkdir(self, dir):
        ddir = self.bdir
        dirs = dir.split('/')
        for d in dirs[:-1]:
            ddir = ddir + '/' + d
            if ddir not in self.rdirs:
                self.rdirs.append( ddir )
            try:
                self.ftp.mkd( ddir )
            except Exception, e:
                pass
    def _dir_exist(self,dir):
        pass
    def _cd_dir(self,dir):
        dir = self.bdir + '/' + dir
        try:
            self.ftp.cwd( dir )
        except Exception,e:
            if  'The system cannot find the file specified' in e.message or \
                'The directory name is invalid' in e.message or \
                'The system cannot find the path specified' in e.message:
                return ERROR_DIR_NOT_EXIST
            print e
        return OK
    def upload_file(self,file_path, dest_path):

        self._mkdir( dest_path )

        #filename
        if dest_path.endswith('/'):
            #/a/b/c/
            file_name = os.path.basename( file_path )
            rfile_path = self.bdir + '/' + dest_path + '/' + file_name
        else:
            #/a/b/c
            file_name = os.path.basename( dest_path )
            rfile_path = self.bdir + '/' + dest_path
        remote_file_path = dest_path
        file = open( file_path , 'rb' )
        self.ftp.storbinary( "STOR " + rfile_path, file )
        file.close()
    def tree(self, dir):
        list = []
        if 0:#self._dir_exist( dir ):
            print "{0} does not exist".format(dir)
            return
        self._cd_dir( dir )
        print dir
        for name in self.ftp.nlst(  ):
            print name
            continue
            try_dir = dir + '/' + name
            try_dir = try_dir.replace('//', '/')
            rt = self._cd_dir( try_dir )
            if rt == ERROR_DIR_NOT_EXIST:
                #is a file
                #print "f "+try_dir
                item = {
                    'type':'file',
                    'path':try_dir
                }
                list.append( item )
            else:
                #print "d "+try_dir
                sublst = self.tree( try_dir )
                if len( sublst ) == 0:
                    item = {
                        'type':'dir',
                        'path' : try_dir,
                    }
                else:
                    item = {
                        'type':'dir',
                        'path' : try_dir,
                        'sub_dir' : sublst
                    }
                list.append( item )
        return list
        pass
    def upload_dir(self, src_dir, dst_dir):
        pass
    def close(self):
        self.ftp.close()

if __name__ == "__main__":
    cfg = json.load(open("py.conf", 'rb'))
    ftp = FtpUploader( cfg['host'], cfg['username'], cfg['password'] , '/ftp123898/Web')
    ftp.upload_file('test.txt', '2/3/4/6/index.html')
    lst = ftp.tree( '/static/2014/1024/steven/upload/' )
    print json.dumps(lst,  indent=4, separators=(',', ': ') )
    #ftp._cd_dir('2/3/4/6/index.html')
    ftp.close()


'''
conn = ftplib.FTP( HOST, NAME, PASS )
dir = '/ftp123898/Web/static/pictures/'
conn.mkd( dir )
conn.cwd( dir )
file = open( FILE, "rb" )
#conn.storbinary("STOR " + FILE, file)
conn.close()
file.close()
'''

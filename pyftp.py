import os
import json
import ftplib
import logging

logging.debug("this test")
HOST = "****"
NAME = "***"
PASS = "***"
FILE = "test.txt"

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
        for d in self.rdirs:
            if dir in d:
                return True
        return False
    def _cd_dir(self,dir):
        dir = self.bdir + '/' + dir
        self.ftp.cwd( dir )
    def upload_file(self,file_path, dest_path):
        if not self._dir_exist( dest_path ):
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
        self._cd_dir( dir )
        for name in self.ftp.nlst(  ):
            pass
            print name
        pass
    def upload_dir(self, src_dir, dst_dir):
        pass
    def close(self):
        self.ftp.close()

if __name__ == "__main__":
    cfg = json.load(open("py.conf", 'rb'))
    ftp = FtpUploader( cfg['host'], cfg['username'], cfg['password'] , '/ftp123898/Web')
    ftp.upload_file('test.txt', '2/3/4/6/index.html')
    ftp.tree( '/' )
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

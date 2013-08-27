import os
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
        #cd
        self._cd_dir( dest_path )
        #filename
        if dest_path.endswith('/'):
            file_name = os.path.basename( file_path )
        else:
            file_name = os.path.basename( dest_path )
        file = open( file_path , 'rb' )
        self.ftp.storbinary( "STOR " + file_name, file )
        file.close()


ftp = FtpUploader( HOST, NAME, PASS , '/ftp123898/Web/static/')
ftp.upload_file('test.txt', '2014/1024/steven/upload/')
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

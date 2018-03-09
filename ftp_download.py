#-*- coding: UTF-8 -*-
####################################################################
# python 查看FTP是否能连接成功
####################################################################
import os
from ftplib import FTP_TLS

USERNAME = 'eweitia'
PASSWORD = 'Tw201803'
FTP_SERVER_HOST = '153.88.99.232'
FTP_SERVER_PORT = 22
FILE_REMOTE = r'otpo.csv'
FILE_LOCAL = r'C:\users\eweitia\desktop\otpo.csv'
BUFSIZE = 1024  # 设置缓冲器大小

def main():
    ftp = FTP_TLS()
    ftp.connect(host = FTP_SERVER_HOST)
    ftp.login(user=USERNAME, passwd=PASSWORD)
    ftp.dir()
    ftp.cwd('/ebipmft-concurintelligenceextract-vd')
    ftp.dir()
    print(ftp.getwelcome())
    fp = open(FILE_LOCAL, 'wb')
    ftp.retrbinary('RETR %s' % FILE_REMOTE, fp.write, BUFSIZE)
    ftp.quit()
    ftp.close()
    
    
if __name__ == '__main__':
    main()

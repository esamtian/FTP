#-*- coding: UTF-8 -*-
####################################################################
# python 查看FTP是否能连接成功
####################################################################

USERNAME = 'eweitia'
PASSWORD = 'Tw201803'

FTP_SERVER_HOST = '153.88.99.232'
FTP_SERVER_PORT = 22
import os
from ftplib import FTP_TLS
def main():
    ftp = FTP_TLS()
    ftp.connect(host = FTP_SERVER_HOST)
    ftp.login(user=USERNAME, passwd=PASSWORD)
    ftp.dir()
    ftp.cwd('/ebipmft-concurintelligenceextract-vd')
    ftp.dir()
    print(ftp.getwelcome())

    file_remote = r'otpo.csv'
    file_local = r'C:\users\eweitia\desktop\otpo.csv'
    bufsize = 1024  # 设置缓冲器大小
    fp = open(file_local, 'wb')
    ftp.retrbinary('RETR %s' % file_remote, fp.write, bufsize)

    ftp.quit()
    ftp.close()
if __name__ == '__main__':
    main()
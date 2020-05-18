# _*_coding:utf8_*_
import paramiko
import sys, os, time
private_key = paramiko.RSAKey.from_private_key_file(r'D:/SecureCRT/cx/id_rsa')
t = paramiko.Transport(('192.168.226.128', 22))
t.connect(username='root', pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('ssh.txt', '/tmp/ssh.txt')
sftp.get('/tmp/ssh.txt','ssh_bak.txt')
t.close()

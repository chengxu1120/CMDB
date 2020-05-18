#!_*_ coding:utf8 _*_
import sys, os, time
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa.pub')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.226.128', port=22, username='root', pkey=private_key)
stdin, stdout, stderr = ssh.exec_command('df')
res, err = stdout.read(), stderr.read()
res = res if res else err
with open('ssh.txt','w') as f:
    f.write(res.decode("utf8"))
print(res.decode("utf8"))

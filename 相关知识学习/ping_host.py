import sys, os, time
import threading
import subprocess


IPList = []


def ping_ip(ip):
    output = os.popen('ping -n 1 %s'%ip)
    for w in output:
        if str(w).upper().find('TTL') >= 0:
            IPList.append(w)


def ping_net(ip):
    pre_ip = (ip.split('.')[0:-1])
    for i in range(1, 256):
        add = (".".join(pre_ip) + '.' + str(i))
        threading._start_new_thread(ping_ip, (add,))
        time.sleep(0.1)
        # print(add)


if __name__ == '__main__':
    # ping_net(socket.gethostbyname(socket.gethostname()))
    ping_net('192.168.6.110')
    for ip in IPList:
        print(ip)

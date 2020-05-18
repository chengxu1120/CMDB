from lib.plugins import get_server_info
import settings
import paramiko
from concurrent.futures import ThreadPoolExecutor
from lib.plugins.basic import BasicPlugin


def ssh(hostname, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, password=settings.SSH_PWD)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    res, err = stdout.read(), stderr.read()
    res = res if res else err
    ssh.close()
    return res


def task(host):
    server_info = get_server_info(ssh, host)
    print(server_info)


def run():
    # basic = BasicPlugin(ssh,'192.168.226.128')

    pool = ThreadPoolExecutor(10)
    hosts = [
        '192.168.226.128',
        '192.168.226.129',
    ]
    for host in hosts:
        pool.submit(task, host)


if __name__ == '__main__':
    run()

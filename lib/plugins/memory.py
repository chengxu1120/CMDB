import sys, os, time
from .base import BasePlugin


class MemoryPlugin(BasePlugin):
    '''
    采集内存信息
    '''

    def process(self, ssh, hostname):
        return ssh(hostname, 'free -h').decode("utf-8")

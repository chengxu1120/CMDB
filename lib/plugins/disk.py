import sys, os, time
from .base import BasePlugin

class DiskPlugin(BasePlugin):
    '''
    采集硬盘信息
    '''

    def process(self, ssh, hostname):
        result = ssh(hostname,'df')
        return result.decode("utf-8")

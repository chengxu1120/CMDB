import sys, os, time
from .base import BasePlugin


class BasicPlugin(BasePlugin):
    def process(self, ssh, hostname):
        result = ssh(hostname, 'uname -a')
        return result.decode("utf8")

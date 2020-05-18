import sys, os, time
from .base import BasePlugin


class NetworkPlugin(BasePlugin):
    def process(self, ssh, hostname):
        return ssh(hostname,'ifconfig').decode("utf-8")

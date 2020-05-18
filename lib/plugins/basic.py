import sys, os, time
from .base import BasePlugin
import traceback
from lib.utils.log import logger


class BasicPlugin(BasePlugin):
    # def process(self, ssh, hostname):
    #     result = ssh(hostname, 'uname -a')
    #     return result.decode("utf8")

    def process(self, ssh, hostname):
        result = None
        try:
            result = int('sdfsf')
        except Exception as e:
            logger.error(traceback.format_exc())
        return result

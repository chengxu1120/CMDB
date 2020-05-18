import sys, os, time
from .base import BasePlugin
import traceback
from lib.utils.log import logger
from lib.plugins.response import BaseResponse

class BasicPlugin(BasePlugin):
    # def process(self, ssh, hostname):
    #     result = ssh(hostname, 'uname -a')
    #     return result.decode("utf8")

    def process(self, ssh, hostname):
        result = BaseResponse()
        try:
            result.data = ssh(hostname, 'uname -a').decode("utf8")
        except Exception as e:
            logger.error(traceback.format_exc())
            result.error = traceback.format_exc()
            result.status = False
        return result.dict

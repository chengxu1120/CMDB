import sys, os, time


class BasePlugin(object):
    def process(self, ssh, hostname):
        raise NotImplementedError("%s必须实现process方法。" % self.__class__.__name__)

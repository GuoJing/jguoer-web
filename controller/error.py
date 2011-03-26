# -*- coding: utf-8 -*-

from lib.template import st

class Error:
    def GET(self):
        return st("404.mako", **locals())


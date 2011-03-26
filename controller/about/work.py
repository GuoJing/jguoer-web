# -*- coding: utf-8 -*-

from lib.template import st

class Work:
    def GET(self):
        return st("about/work.mako", **locals())

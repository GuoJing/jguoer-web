# -*- coding: utf-8 -*-

from lib.template import st

class About:
    def GET(self):
        return st("about/about.mako", **locals())

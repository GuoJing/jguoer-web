# -*- coding: utf-8 -*-

from lib.template import st

class Home:
    def GET(self):
        content = 'Hello world page with mako'
        return st("main.mako", **locals())

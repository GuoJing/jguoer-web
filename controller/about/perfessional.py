# -*- coding: utf-8 -*-

from lib.template import st

class Perfessional:
    def GET(self):
        return st("about/perfessional.mako", **locals())


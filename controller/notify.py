# -*- coding: utf-8 -*-

from lib.template import st

class Notify:
    def GET(self):
        content = '操作执行成功'
        return st("notify.mako", **locals())

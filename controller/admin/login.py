# -*- coding: utf-8 -*-

from lib.template import st
from lib.utils import js, gd, sc, gc
from model.user import authen_user, get_user

class Login:
    def GET(self):
        name = gc('name')
        if name:
            #return 'test'
            user = get_user(name)
            return st("admin/main.mako", **locals())
        return st("admin/login.mako", **locals())

    def POST(self):
        req = gd()
        authen = authen_user(req.name, req.pwd)
        if authen:
            sc('name', req.name)
        return js(dict(r=True, authen=authen))

# -*- coding: utf-8 -*-

from lib.template import st
from lib.utils import js, gd, sc, gc
from model.user import authen_user, get_user
from model.article import add

class AdminAdd:
    def GET(self):
        name = gc('name')
        if name:
            user = get_user(name)
            return st("admin/add.mako", **locals())
        return st("admin/login.mako", **locals())

    def POST(self):
        req = gd()
        name = gc('name')
        if name:
            user = get_user(name)
            ok = add(req.cate, req.title, req.url, req.content, user.name)
            return js(dict(r = True, ok = ok))
        else:
            return js(dict(r = False))

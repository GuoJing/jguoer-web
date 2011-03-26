# -*- coding: utf-8 -*-

from lib.template import st
from lib.utils import js, gd, sc, gc
from model.user import authen_user, get_user

class AdminLogout:
    def GET(self):
        name = gc('name')
        sc('name','',-2)
        return st("admin/login.mako", **locals())

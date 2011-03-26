# -*- coding: utf-8 -*-

from lib.template import st
from lib.utils import js, gd, sc, gc
from model.article import get_user_articles
from model.user import authen_user, get_user

class AdminManage:
    def GET(self):
        name = gc('name')
        if name:
            #return 'test'
            user = get_user(name)
            articles = get_user_articles(user.name)
            return st("admin/manage.mako", **locals())
        return st("admin/login.mako", **locals())

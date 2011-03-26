# -*- coding: utf-8 -*-

from lib.template import st
from lib.utils import js, gd, sc, gc
from model.article import Article
from model.user import authen_user, get_user

class AdminDelete:
    def POST(self, name):
        authen = gc('name')
        if authen:
            article = Article.get(name)
            article.delete()
            return js(dict(r=True, id=name))
        return js(dict(r=False))


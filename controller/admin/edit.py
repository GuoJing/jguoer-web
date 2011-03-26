# -*- coding: utf-8 -*-

from lib.template import st
from lib.utils import js, gd, sc, gc
from model.user import authen_user, get_user
from model.article import Article

class AdminEdit:
    def GET(self, id):
        name = gc('name')
        article = Article.get(id)
        if article and name:
            user = get_user(name)
            return st("admin/edit.mako", **locals())
        return st("404.mako", **locals())

    def POST(self, id):
        article = Article.get(id)
        cate = article.cate
        req = gd()
        article.title = req.title
        article.cate = req.cate
        article.url = req.url
        article.content = req.content
        article.update(cate)
        return js(dict(r=True, ok=True, id=id))

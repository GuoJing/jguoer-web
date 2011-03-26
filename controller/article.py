# -*- coding: utf-8 -*-

from lib.template import st
from model.article import Article

class Articles:
    def GET(self, name):
        article = Article.get(name)
        if article:
            return st("article.mako", **locals())
        return st("404.mako", **locals())

# -*- coding: utf-8 -*-

from lib.template import st
from model.article import get_cate_articles

class News:
    def GET(self):
        articles = get_cate_articles(0)
        return st("news.mako", **locals())

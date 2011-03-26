# -*- coding: utf-8 -*-

from lib.template import st
from model.article import get_cate_articles

class Design:
    def GET(self):
        articles = get_cate_articles(1)
        return st("news.mako", **locals())

#!/usr/bin/env python

import web
from controller.home import Home
from controller.error import Error
from controller.news import News
from controller.blog import Blog
from controller.design import Design
from controller.product import Product
from controller.notify import Notify
from controller.article import Articles
from controller.admin.login import Login
from controller.admin.main import AdminMain
from controller.admin.add import AdminAdd
from controller.admin.edit import AdminEdit
from controller.admin.manage import AdminManage
from controller.admin.delete import AdminDelete
from controller.admin.logout import AdminLogout
from controller.about.about import About
from controller.about.work import Work
from controller.about.perfessional import Perfessional

urls = (
    '/', 'Home',
    '/index', 'Home',
    '/home', 'Home',
    '/about', 'About',
    '/about/perfessional', 'Perfessional',
    '/about/work', 'Work',
    '/news', 'News',
    '/blog', 'Blog',
    '/article/(.+)', 'Articles',
    '/design', 'Design',
    '/product', 'Product',
    '/admin/success', 'Notify',
    '/admin/login', 'Login',
    '/admin/main', 'AdminMain',
    '/admin/add', 'AdminAdd',
    '/admin/edit/(.+)', 'AdminEdit',
    '/admin/manage', 'AdminManage',
    '/admin/delete/(.+)', 'AdminDelete',
    '/admin/logout', 'AdminLogout',
    '/.*', 'Error',
)

app = web.application(urls, globals())

ENABLE_NGINX = False

if __name__ == "__main__":
    if ENABLE_NGINX:
        web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()

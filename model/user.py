# encoding: UTF-8
from lib.consts import *

class User(object):
    name = ''
    nickname = ''
    pic_url = ''
    rss_url = ''
    blog_url = ''
    rss = None
    pwd = ''

def get_user(name):
    if name in user_info.keys() and name in active_users:
        user = User()
        user.name = name
        info = user_info[name].split(',')
        user.nickname = info[0]
        user.pic_url = info[1]
        user.rss_url = blog_rss_urls[name]
        user.blog_url = blog_url[name]
        user.pwd = user_pwd[name]
        return user

def get_users(names):
    users = []
    for name in names:
        user = get_user(name)
        users.append(user)
    return users

def authen_user(name, pwd):
    if name in active_users and pwd == user_pwd[name]:
        return True
    return False

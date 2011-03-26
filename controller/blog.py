# -*- coding: utf-8 -*-

import urllib
from xml.dom import minidom
from lib.template import st
from lib.utils import get_xml_text
from lib.mc import mc
from lib.consts import *
from model.rss import Rss
from model.user import get_users

class Blog:
    def GET(self):
        mc_user = mc.get('users')
        if mc_user:
            users = mc_user
        else:
            users = get_users(active_users)
            has_error = False
            allrss = []
            for user in users:
                try:
                    rss = []
                    rss_url = user.rss_url
                    data = urllib.urlopen(rss_url)
                    data = data.read()
                    xml = minidom.parseString(data)
                    items = xml.getElementsByTagName('item')[:4]
                    for item in items:
                        rss_item = Rss()
                        title = get_xml_text(item.getElementsByTagName('title')[0].childNodes)
                        date = get_xml_text(item.getElementsByTagName('pubDate')[0].childNodes)
                        link = get_xml_text(item.getElementsByTagName('link')[0].childNodes)
                        rss_item.title = title.encode('utf-8')
                        rss_item.date = date.split('+')[0].encode('utf-8')
                        rss_item.link = link.encode('utf-8')
                        rss.append(rss_item)
                        allrss.append(rss_item)
                    user.rss = rss
                except:
                    has_error = True
                    user.rss = None
            if not has_error:
                mc.set('users', users, 3600 * 12)
        return st('blog.mako', **locals())

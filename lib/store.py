# -*- coding: utf-8 -*-

import MySQLdb

def get_cursor():
    try:
        store = MySQLdb.connect(host='127.0.0.1', user='s184', passwd='a2vfkhzq', db='s184_app')
        cursor = store.cursor()
        return cursor
    except:
        return None

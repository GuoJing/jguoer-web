# encoding: UTF-8
import urllib
from lib.store import get_cursor
from lib.mc import mc

class Article(object):
    cate = 0
    title = ''
    url = ''
    content = ''
    id = ''
    author = ''
    time = None

    def __init__(self, id, cate, title, author, time, url=None, content=None):
       self.cate = cate
       self.title = urllib.unquote(title)
       self.url = url
       self.content = urllib.unquote(content)
       self.id = id
       self.author = author
       self.time = time

    @classmethod
    def get(cls, id):
        mc_article = mc.get('a:%s'%id)
        if mc_article:
            return mc_article
        cursor = get_cursor()
        sql = 'select cate, title, author, time, url, content from article ' \
            'where id=%s'
        params = (id)
        if cursor:
            cursor.execute(sql, params)
            r = cursor.fetchone()
            if r:
                article = cls(id, r[0], r[1], r[2], r[3], r[4], r[5])
                mc.set('a:%s'%id, article)
                return article
            return None
        return None
    
    @classmethod
    def gets(cls, ids):
        return [mc.get('a:%s'%id) or Article.get(id) for id in ids]

    def delete(self):
        cursor = get_cursor()
        sql = 'delete from article where id = %s'
        params = (self.id)
        cursor.execute(sql, params)
        cursor.connection.commit()
        mc.delete('a:%s'%self.id)
        mc.delete('as:%s'%self.author)
        mc.delete('ac:%s'%self.cate)

    def update(self, old_cate):
        cursor = get_cursor()
        sql = 'update article set title=%s, cate=%s, url=%s, content=%s, author=%s ' \
            'where id=%s'
        params = (self.title, self.cate, self.url, self.content, self.author, self.id)
        cursor.execute(sql, params)
        cursor.connection.commit()
        mc.delete('a:%s'%self.id)
        if self.cate != old_cate:
            mc.delete('ac:%s'%self.cate)
            mc.delete('ac:%s'%old_cate)

def add(cate, title, url, content, author):
    mc.delete('as:%s'%author)
    mc.delete('ac:%s'%cate)
    cursor = get_cursor()
    sql = 'insert into article (cate, title, url, content, author) values ' \
        '(%s, %s, %s, %s, %s)'
    params = (cate, title, url, content, author)
    try:
        cursor.execute(sql, params)
        cursor.connection.commit()
        return True
    except:
        cursor.connection.rollback()
        return False

def get_ids_of_user(name):
    ids = mc.get('as:%s'%name)
    if not ids:
        cursor = get_cursor()
        sql = 'select id from article '\
            'where author=%s order by id desc'
        params = (name)
        cursor.execute(sql, params)
        ids = [str(id) for (id, ) in cursor]
        mc.set('as:%s'%name, ids)
    return ids

def get_ids_of_cate(cate):
    ids = mc.get('ac:%s'%cate)
    if not ids:
        cursor = get_cursor()
        sql = 'select id from article '\
            'where cate=%s order by id desc'
        params = (cate)
        cursor.execute(sql, params)
        ids = [str(id) for (id, ) in cursor]
        mc.set('ac:%s'%cate, ids)
    return ids

def get_user_articles(name):
    ids = get_ids_of_user(name)
    return Article.gets(ids)

def get_cate_articles(cate):
    ids = get_ids_of_cate(cate)
    return Article.gets(ids)

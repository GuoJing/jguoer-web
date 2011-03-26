# encoding: UTF-8
import web

def get_xml_text(nodelist):
    rc = ""
    if not nodelist:
        return ''
    for node in nodelist:
        rc = rc + node.data
        return rc

def replace_html(str):
    str = str.replace("&lt;","a")
    str = str.replace("&gt;","b")
    return str

def parse_list_para(value):
    if not value:
        return '[]'
    json_str = ''
    if type(value) is list:
        for item in value:
            json_str = json_str + parse_dict_para(item) + ','
        json_str = json_str[:-1]
    return '[' + json_str + ']'

def parse_normal_type(value):
    bvalue = value
    if value is True and type(value) is bool:
        value = 'true'
    elif value is False and type(value) is bool:
        value = 'false'
    value = value.replace('"','\"')
    return value, type(bvalue)

def parse_dict_para(data):
    if not data:
        return '{}'
    json_str = ''
    if type(data) is dict:
        for key in data.keys():
            value, btype = parse_normal_type(data[key])
            if btype is bool:
                json_str = json_str + '"%s":%s,'%(key, value)
            else:
                json_str = json_str + '"%s":"%s",'%(key, value)
        json_str = json_str[:-1]
        return '{' + json_str + '}'
    else:
        return '{}'

class RequestObject(object):
    def __init__(self, data):
        if data:
            for key in data:
                value = data[key]
                self.__dict__[key] = value

def get_data():
    data = web.data()
    paras = str(data).split('&')
    req = dict()
    for para in paras:
        t = para.split('=')
        req[t[0]] = t[1]
    return RequestObject(req)

def set_cookie(key, value, time=None):
    time = time or 3600 * 10
    web.setcookie(key, value, time)

def get_cookie(key):
    return web.cookies().get(key)

js = parse_dict_para
gd = get_data
sc = set_cookie
gc = get_cookie

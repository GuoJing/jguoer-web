# -*- coding: utf-8 -*-

import cmemcached

servers = ["127.0.0.1:11508"]

mc = cmemcached.Client(servers)

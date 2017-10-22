#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web

from server.controller.base import BaseHandler
from schema.tables.income import Income


class BlistHandler(BaseHandler):

    def get(self):
        return self.ok(Income.getAll(self.db, toStr=True))
#! /usr/bin/env python
# -*- coding:utf-8 -*-

import feedparser
from datetime import datetime

class Inputter(object):
    def __init__(self, conf, name):
        self.conf = conf
        self.name = name

    def get(self):
        raise NotImplemented

    def history_item(self, title, tag):
        return {'title': title,
                'input_from': self.name,
                'input_date': datetime.now().isoformat(),
                'tag': tag}

class FeedInputter(Inputter):
    def __init__(self, conf, name):
        super(FeedInputter, self).__init__(conf, name)

    def get(self):
        input_dict = {}
        try:
            fdp = feedparser.parse(self.conf['url'])
        except Exception as e:
            print e
            print "(Error) can not get the RSS..."
            raise

        if 'keyword' in self.conf:
            keyword = self.conf['keyword']
        else:
            keyword = None

        for entry in fdp['entries']:
            title = entry.get('title', "")

            if keyword and keyword not in title:
                continue

            link  = entry.get('link', "")
            if not link in input_dict: # if the link is not in the dict yet
                input_dict[link] = self.history_item(title, '')

        return input_dict

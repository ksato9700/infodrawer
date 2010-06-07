#! /usr/bin/env python
# -*- coding:utf-8 -*-

import inputter

class Twitter(inputter.FeedInputter):
  '''
  Retrieve entries in Twitter's TimeLine matching the specified keyword
  
  Format of config.yaml
      twitter:
          url: http://twitter.com/statuses/user_timeline/XXXXX.rss
          keyword: "メモ"

  >>> conf = {}
  >>> conf['url'] = "http://twitter.com/statuses/user_timeline/7080152.rss"
  >>> conf['keyword'] = u"こんにちは"

  >>> from twitter import Twitter
  >>> t = Twitter(conf)
  >>> result = t.get()
  >>> print len(result)
  3

  '''
  def __init__(self, conf):
    super(Twitter, self).__init__(conf, 'Twitter Memo')

def _test():
  import doctest
  doctest.testfile('twitter.py', encoding='utf-8')

if __name__ == '__main__':
  _test()

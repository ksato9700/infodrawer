#! /usr/bin/env python
# -*- coding:utf-8 -*-

import inputter

class TwitterFav(inputter.FeedInputter):
  '''
  Retrieve favarites from Twitter
  
  Format of config.yaml
      twitterfav:
          url: http://twitter.com/favorites/XXXXX.rss

  >>> conf = {}
  >>> conf['url'] = "http://twitter.com/favorites/7080152.rss"

  >>> t = TwitterFav(conf)
  >>> result = t.get()
  >>> print len(result)
  1

  '''
  def __init__(self, conf):
    super(TwitterFav, self).__init__(conf, 'Twitter Favorite')

def _test():
  import doctest
  doctest.testmod()

if __name__ == '__main__':
  _test()

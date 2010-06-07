#! /usr/bin/env python
# -*- coding:utf-8 -*-

import inputter

class GoogleReader(inputter.FeedInputter):
  '''
  Retrieve starred entries from GoogleReader

  Use only 'url' in config.yaml

  >>> conf = {}
  >>> conf['url'] = "http://feeds.feedburner.com/blogspot/dtKx"
  ... # this is just for doctest. The actual Google Reader starred URLs will be the following format.
  ... # http://www.google.com/reader/public/atom/user/XXXXX/state/com.google/starred

  >>> g = GoogleReader(conf)

  Returns a dictionary of url: (title, input_from, input_date, tag)
  
  >>> result = g.get()
  >>> print len(result)
  25
  '''
  def __init__(self, conf):
    super(GoogleReader, self).__init__(conf, 'Google Reader')
        
def _test():
  import doctest
  doctest.testmod()

if __name__ == '__main__':
  _test()

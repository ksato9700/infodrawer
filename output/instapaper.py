#! /usr/bin/env python
# -*- coding:utf-8 -*-

import outputter
import urllib

class InstaPaper(outputter.Outputter):
    def __init__(self, conf):
      super(InstaPaper, self).__init__(conf)


    def output(self, output_dict):
      INSTAPAPER_API_URL = 'https://www.instapaper.com/api/add'

      pd = {'username':self.conf['username'], 'password':self.conf['password']}
    
      result_list = []
      for url,entry in output_dict.iteritems():
        result = {}
        pd['url'] = url
        pd['title'] = entry['title'].encode('UTF-8')
        params = urllib.urlencode(pd)
        response = urllib.urlopen(INSTAPAPER_API_URL, params)
        if (response.code != 200):
          continue
        result['code'] = response.code
        result['link'] = pd['url'] 
        result['title'] = pd['title']
        result_list.append(result)
      return result_list

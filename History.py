#! /usr/bin/env python
# coding: utf-8

import os,yaml

HIST_FILENAME="input_hist.yaml"

class History():
  def __init__(self):
    '''
    hist_map �ϡ�url�򥭡��Ȥ��ơ�{title,date}��ޤ༭�����ġ�
    date�η����ϡ�ISO 8601 (YYYY-MM-DD)�ǡ�
    entry�����դǤϤʤ�����Ͽ���줿����

    hist_dict = {'http://...': {'title':'...', 'date': '...'},
                'http://...': {'title':'...', 'date': '...'}, ... }
    
    '''
    f = os.path.abspath(os.path.dirname(__file__)) + "/" + HIST_FILENAME

    self.hist_dict = {}
    
    if os.path.exists(f):
      self.hist_dict =  yaml.load(open(f))

  def get_hist(self):
    return self.hist_dict

  def append_file(self):
    f = os.path.abspath(os.path.dirname(__file__)) + "/" + HIST_FILENAME
    fp = open(f,"a")
    output = yaml.dump(self.hist_dict)
    fp.write(output)
    fp.close()

  def merge(self, input_dict):
    return_dict = {}
    for url,value in input_dict.iteritems():
      if (url not in self.hist_dict):
	self.hist_dict[url] = value
	return_dict[url] = value

    return return_dict

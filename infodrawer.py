#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys, os
import types
import yaml

import urllib
import urllib2

import History

CONF_FILENAME="conf.yaml"

def encoding_detect(orig_str):
  for coding in ('iso-2022-jp', 'euc-jp', 'cp932', 'utf-8'):
    try:
      return (coding, orig_str.decode(coding))
    except UnicodeDecodeError:
      pass
    return (None, None)
  
def create_contents(url, value, insta=True):
  if (insta):
    url = "http://www.instapaper.com/text?u=" + urllib.quote_plus(url)
  req = urllib2.Request(url)
  response = None
  try:
    response = urllib2.urlopen(req)
  except URLError, e:
    print e.code
    print e.read()
    return ""

  msg = response.read()
  (value['encoding'], value['contents']) = encoding_detect(msg)
  
  return value

def find_putters(conf, dirname, base_modname, base_classname):
  putter_module = __import__(dirname, fromlist=conf[dirname].keys())
  putter_class = getattr(getattr(putter_module, base_modname), base_classname)

  putters = []
  for n in conf[dirname]:
    mod = getattr(putter_module,n) 
    putters.append(*map(lambda c: (n,c), 
                        filter(lambda attr: isinstance(attr, type) and issubclass(attr, putter_class), 
                               map(lambda name: getattr(mod,name), dir(mod)))))
  return putters

def main():
  f = os.path.abspath(os.path.dirname(__file__)) + "/" + CONF_FILENAME
  conf = yaml.load(open(f).read().decode('utf8'))

  # hist = History.History()

  new_dict = {}
  # for i, inputter in find_putters(conf, 'input', 'inputter', 'Inputter'):
  #   new_dict.update(hist.merge(inputter(conf['input'][i]).get()))
  
  # for url, value in  new_dict.iteritems():
  #   new_dict[url] = create_contents(url, value)

  # if len(new_dict) < 1:
  #    print 'nothing to output'
  #    sys.exit(0)
    
  for o, outputter in find_putters(conf, 'output', 'outputter', 'Outputter'):
    outputter(conf['output'][o]).output(new_dict)

if __name__ == '__main__':
  main()

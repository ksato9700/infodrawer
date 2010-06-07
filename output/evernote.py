#! /usr/bin/env python
# -*- coding:utf-8 -*-

import outputter

class Evernote(outputter.MailOutputter):
  def __init__(self, conf):
    super(Evernote, self).__init__(conf)

    if ('note' in conf):
      self.note      = conf['note']
    else:
      self.note      = None
    if ('tag' in conf):
      self.tag       = conf['tag']
    else:
      self.tag       = None


  def create_HTML_message(self, from_addr, to_addr, subject, html_body, encoding):
    if 'note' in self.conf:
      subject += " @" + self.conf['note']
    if 'tag' in self.conf:
      subject += " #" + self.conf['tag']
    return super(Evernote, self).create_HTML_message(from_addr, to_addr, subject, html_body, encoding)

if __name__ == '__main__':
  import sys,os
  import yaml
  
  sys.path.append("..")
  import History

  CONF_FILENAME="conf.yaml"

  hist = History.History()
  
  f = os.path.abspath(os.path.dirname(__file__)) + "/../" + CONF_FILENAME
  conf = yaml.load(open(f).read().decode('utf8'))

  output_m = Evernote(conf['output']['evernote'])
  output_m.output(hist.get_hist())
  

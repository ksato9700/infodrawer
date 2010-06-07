#! /usr/bin/env python
# -*- coding:utf-8 -*-

import outputter

class Mail(outputter.MailOutputter):
  def __init__(self, conf):
    super(Mail, self).__init__(conf)

def main():
  import sys,os
  import yaml
  
  sys.path.append("..")
  import History

  CONF_FILENAME="conf.yaml"

  hist = History.History()

  f = os.path.abspath(os.path.dirname(__file__)) + "/../" + CONF_FILENAME
  conf = yaml.load(open(f))

if __name__ == '__main__':
  main()

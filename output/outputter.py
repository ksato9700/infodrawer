#! /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import urllib

import re

import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart 
from email.Header import Header
from email.Utils import formatdate

class Outputter(object):
    def __init__(self, conf):
        self.conf = conf

    def output(self):
        raise NotImplemented

class MailOutputter(Outputter):
    def __init__(self, conf):
        super(MailOutputter, self).__init__(conf)

    def create_HTML_message(self, from_addr, to_addr, subject, html_body, encoding):
        msg = MIMEText(html_body.encode('utf-8'), 'html', 'utf-8')

        subject_prefix = self.conf['subject']
        # insta = conf['insta']

        subject = subject.ljust(30) # title becomes max 30 length
        if subject_prefix:
            subject = subject_prefix + " " + subject
    
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Date'] = formatdate()
        
        return msg

    def send_mail(self, from_addr, to_addr, msg, smtp = None):
        # SMTPの引数を省略した場合はlocalhost:25
        if smtp == None:
            s = smtplib.SMTP()
        else:
            s = smtplib.SMTP(smtp)
        s.sendmail(from_addr, [to_addr], msg.as_string())
        s.close()

    def send_via_gmail(self, from_addr, to_addr, msg, gaddr, password):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(gaddr, password)
        s.sendmail(from_addr, [to_addr], msg.as_string())
        s.close()

    def output(self, output_dict):
        from_addr  = self.conf['from_addr']
        to_addr    = self.conf['mail_addr']
        smtp       = self.conf['smtp']

        use_gmail  = self.conf['use_gmail'] == True
        gmail_addr = self.conf['gmail_addr']
        gmail_pass = self.conf['gmail_pass']
        if not gmail_pass:
            import getpass
            gmail_pass = getpass.getpass('GMail password:')

        for url, value in  output_dict.iteritems():
            contents = None
            encoding = ""
            if 'Twitter' in value['input_from']:
                encoding = 'utf-8'
                contents = value['title']
            else:
                encoding = value[encoding]
                contents = value[contents]

            if contents == None:
                continue # XXX 

            msg = self.create_HTML_message(from_addr,to_addr,
                                           value['title'],
                                           contents, encoding)
            if use_gmail:
                self.send_via_gmail(from_addr, to_addr, msg, 
                                    gmail_addr, gmail_pass)
            else:
                self.send_mail(from_addr, to_addr, msg, smtp)


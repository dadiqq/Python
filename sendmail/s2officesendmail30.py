#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from mconfig import META_MAILS
from email.header import Header
class MailError(Exception):
    pass

class Mailer(object):
    def __init__(self, maildict, datenow):
        self.mail_list = maildict.get('to', [])
        self.mail_subject = maildict.get('subject', '')
        self.mail_content = maildict.get('content', '')
        self.attach_names = maildict.get('attach_names', [])
        self.datenow = datenow

        self.mail_host = ("email.foundersc.com")
        self.mail_user = "limq"
        self.mail_port = 587
        self.mail_pass = "l"
        self.mail_postfix = "chinans.com.cn" 
    
    def check_mconfig(self):
        if not self.mail_list or not self.mail_subject:
            raise MailError('param error, please check mconfig.py and confirm all dict have "to" and "subject" key')
               

    def sendMail(self):
        self.check_mconfig()
    
        me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        
        msg = MIMEMultipart()
        msg["Accept-Language"]="zh-CN"
        msg["Accept-Charset"]="ISO-8859-1,utf-8"

        msg['Subject'] = self.mail_subject.replace('YYYYMMDD', str(self.datenow))
        msg['From'] = me
        msg['To'] = ";".join(self.mail_list)
        
        puretext = MIMEText('<h1>你好，<br/>'+self.mail_content+'</h1>','html','utf-8')
        # puretext = MIMEText('自动邮件测试'+self.mail_content)
        msg.attach(puretext)
        
        for attach_name in self.attach_names:
            attach_name = attach_name.replace('YYYYMMDD', str(self.datenow))
            #attach_name = attach_name.decode("utf-8") #python3.x 没有decode方法
            rarpart = MIMEApplication(open(attach_name, 'rb').read())
            fname = attach_name.split('/')[-1]
            rarpart.add_header('Content-Disposition', 'attachment', filename=('gbk','',fname))

            msg.attach(rarpart)
        
        
        try:
          s = smtplib.SMTP() #创建邮件服务器对象
          s.connect(self.mail_host,self.mail_port) #连接到指定的smtp服务器。参数分别表示smpt主机和端口
          s.starttls()
          s.ehlo()
          s.login(self.mail_user, self.mail_pass) #登录到你邮箱
          s.sendmail(me, self.mail_list, msg.as_string()) #发送内容
          print (self.mail_content + '发送成功!\n')
          s.close()

          return True
        except Exception as e:
          print (e)
          return False

def send_batch_mail(datenow):
    for meta_mail in META_MAILS:
        print(meta_mail['content'] + "发送中...")
        ss = Mailer(meta_mail, datenow)

        ss.sendMail()
    


if __name__ == '__main__':
    datenow = input('please input current date, format as YYYYMMDD:  ')
    print ('you input is %s, please input "yes" conginue' % datenow)
    isok = input()
    if str(isok).lower() == 'yes':
       send_batch_mail(datenow)

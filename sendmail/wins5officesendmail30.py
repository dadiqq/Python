#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
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

        self.mail_host = ("smtp.126.com")#发送服务器
        self.mail_user = "gylimingqi" #邮箱用户名
        self.mail_port = 25 #端口
        self.mail_pass = "p@ssw0rd" #邮箱密码
        self.mail_postfix = "126.com"  #邮箱后缀 
    
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
        message1 = 'Hi,' + self.mail_content + ' <br/>'
        file_object=open(htmlfilename)
        mess=file_object.readline()
        file_object.close()
        mess=str(mess)
        #message2='    This email is auto-generated by the monitor tool. <br/>'
        #message3='    Thanks <br/>'
        #message4='Mingq Li  <br/><br/>__________________________________________________<br/>'
        #message5='中国民族证券有限责任公司<br/>'
        #message6='客户资产存管中心<br/>'
        #message7='地址:北京市西城区阜外大街甲34号方正证券大厦<br/>'
        #message8='联系电话:01068575099<br/>'
        #message9='<address>Written by <a href="mailto:limq@chinans.com.cn">李名琪</a>.<br> 北京 at:<br>Example.com<br>7F, 方正证券大厦<br>北京市</address>'
        #messagetotal=message1+message2+message3+message4+message5+message6+message7+message8+message9
        html_start = '<font face="Courier New, Courier, monospace"><pre>'  
        html_end = '</pre></font>'  
 
        puretext = MIMEText(html_start+message1+mess+html_end,_subtype='html',_charset='utf-8')
        #puretext = MIMEText('<h1>你好，<br/>'+self.mail_content+'</h1>','html','utf-8')
        # puretext = MIMEText('自动邮件测试'+self.mail_content)
        msg.attach(puretext)
        
        for attach_name in self.attach_names:
            attach_name = attach_name.replace('YYYYMMDD', str(self.datenow))
            #attach_name = attach_name.decode("utf-8") #python3.x 没有decode方法
            rarpart = MIMEApplication(open(attach_name, 'rb').read())
            fname = attach_name.split('\\')[-1]
            rarpart.add_header('Content-Disposition', 'attachment', filename=('gbk','',fname))

            msg.attach(rarpart)
        
        
        try:
          starttime=datetime.datetime.now()#统计发送开始时间
          s = smtplib.SMTP() #创建邮件服务器对象
          s.connect(self.mail_host,self.mail_port) #连接到指定的smtp服务器。参数分别表示smpt主机和端口
          s.starttls()
          s.ehlo()
          s.login(self.mail_user, self.mail_pass) #登录到你邮箱
          s.sendmail(me, self.mail_list, msg.as_string()) #发送内容
          endtime=datetime.datetime.now()#统计结束时间
          total=endtime-starttime
          print ('耗时',total,'s ' + self.mail_content + '发送成功!\n')
          s.close()
          zz= '耗时 ' + str(total) + 's '
          z=(self.mail_content + "发送成功!\n\n")
          with open(logfilename,'a') as file_object:  #写日志文件
              file_object.write(zz)
              file_object.write(z)
          return True
        except Exception as e:
          print (e)

def send_batch_mail(datenow):
    for meta_mail in META_MAILS:
        time=datetime.datetime.now()
        time2= time.strftime('%Y%m%d %H:%M:%S')
        print('开始 ' + time2 + meta_mail['content'] + "发送中...")
        s = '开始 ' + time2 + meta_mail['content'] + '发送中...\n'
        with open(logfilename,'a') as file_object: #写日志文件

            file_object.write(s)
        ss = Mailer(meta_mail, datenow)
        ss.sendMail()
    

if __name__ == '__main__':
    datenow = input('please input current date, format as YYYYMMDD:  ')
    print ('you input is %s, please input "yes" conginue' % datenow)
    logfilename='sendmail' + datenow + '.log'
    htmlfilename='htmlsendmail.html'
    isok = input()
    if str(isok).lower() == 'yes':
       send_batch_mail(datenow)

#!/usr/bin/env python
# -*- coding:utf-8 -*-

META_MAILS = [
		  {
          'to':[
                'zhaoqizhen@foundersc.com',
                'limq@foundersc.com',
                'gylimingqi@126.com',
                '78235621@qq.com'
                ],  #必填
          'attach_names':[
                          r'/home/limq/Python/sendmail/YYYYMMDD/锝金投资1号YYYYMMDD.rar'
                          ],
          'content': '锝金投资一号,这是一封测试邮件,当您收到这封邮件是我们测试程序发送的', #必填
          'subject': '锝金投资一号YYYYMMDD', 
          },
		  {
          'to':[
                'gylimingqi@126.com',
                'limq@foundersc.com',
                'zhaoqizhen@foundersc.com',
                '78235621@qq.com'
                ],  #必填
          'attach_names':[
                          r'/home/limq/Python/sendmail/YYYYMMDD/五矿信托伞形宝YYYYMMDD.rar'
                          ],
          'content': '五矿信托,这是一封测试系统邮件,您收到这封邮件是我们测试程序发送的', #必填
          'subject': '五矿信托YYYYMMDD', 
          },
		  
]
dict=META_MAILS[0]
print (dict.get('to',[]))


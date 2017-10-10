#!/usr/bin/env python
# -*- coding:utf-8 -*-

META_MAILS = [
		  {
          'to':[
                'gylimingqi@126.com',
                '78235621@qq.com'
                ],  #必填
          'attach_names':[
                          r'/home/limq/Python/sendmail/YYYYMMDD/锝金投资壹号YYYYMMDD.rar'
                          ],
          'content': '锝金投资一号', #必填
          'subject': '锝金投资一号YYYYMMDD', 
          },
		  {
          'to':[
                'gylimingqi@126.com',
                '78235621@qq.com'
                ],  #必填
          'attach_names':[
                          r'/home/limq/Python/sendmail/YYYYMMDD/五矿信托伞形宝YYYYMMDD.rar'
                          ],
          'content': '五矿信托', #必填
          'subject': '五矿信托YYYYMMDD', 
          },
		  
]
dict=META_MAILS[0]
print (dict.get('to',[]))


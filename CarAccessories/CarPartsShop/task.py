from __future__ import absolute_import
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from CarAccessories.celery import app


# @app.task
def send_email(code):

    sender = 'xxm13504577723@163.com'
    password = 'xxm123456'
    revicers = [
        '921774254@qq.com'
    ]
    content = '''尊敬的用户%s:

        欢迎注册passeur.cn摆渡账户，

        你的验证码是%s

        如果你有任何的不满和建议可以在该网站的博客中在线和我聊天passeur.com/chat/
        或者给我发送邮件xxm13504577723@163.com
    ''' % (''.join(revicers), code)

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("摆渡人", 'utf-8')  # 发送者
    message['To'] = ''.join(revicers)

    subject = '摆渡账号注册码验证'
    message['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
    smtp.login(sender, password)
    smtp.sendmail(sender, revicers, message.as_string())

    smtp.close()

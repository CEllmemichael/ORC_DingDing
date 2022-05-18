import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '@qq.com'  # 填写发信人的邮箱账号
my_pass = ''  # 发件人邮箱授权码
my_user = '@qq.com'  # 收件人邮箱账号


def mail(my_user,wern):
    ret = True
    if wern == 1:
        txt1 = '现在签到'
        # pass
    elif wern == 2:
        txt1 = '有可能在提问'
        # pass
    try:
        msg = MIMEText(txt1, 'plain', 'utf-8')  # 填写邮件内容
        msg['From'] = formataddr(["魏树鸿的程序提醒:", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["魏树鸿的程序提醒:", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "程序提醒"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

def loop(wern):
    mail_daress= ["1834719615@qq.com","1263795805@qq.com","1055308565@qq.com"]#,"1204191514@qq.com","1055308565@qq.com","2294825149@qq.com","2810051559@qq.com"]
    for my_user in mail_daress:
        n = mail(my_user,wern)
    return n

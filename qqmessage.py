# -*- coding:utf-8 -*-
"""
Author：G3
Time: 2021/7/13
Software: PyCharm
"""
# 该例程仅供学习使用

# 使用psutil来判断QQ是否登录
import psutil,time,os
import pyperclip
import pyautogui as gui

people = '小号'	# 好友全称
message = '***'	# 发送的消息
msg = message
QQ_dir = r'E:\Tencent\QQ\Bin\QQ.exe'	# QQ路径

# 判断QQ是否登录
def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:  # 通过PID判断
        if psutil.Process(pid).name() == process_name:
            print(1)
            return isinstance(pid,int)

# 发送消息
def send_msg(people, msg):
    if proc_exist('QQ.exe'):
        # 打开QQ主界面
        gui.moveTo(1694, 1058, duration=0.2)
        gui.moveTo(1694, 1058, duration=0.2)
        gui.click()
        time.sleep(0.5)

    else:
        # 登录QQ
        QQ_login()

    # 搜索好友并打开聊天窗口
    gui.moveTo(1569, 263, duration=0.2)
    gui.click()
    time.sleep(0.5)
    pyperclip.copy(people)
    gui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    gui.hotkey('Enter')
    time.sleep(1)

    # 输入需要发送的信息
    gui.moveTo(700, 850, duration=0.2)
    gui.click()
    pyperclip.copy(msg)
    gui.hotkey('ctrl', 'v')
    gui.hotkey('Enter')

    # 隐藏主界面并退出聊天界面
    gui.moveTo(1795, 127, duration=0.5)
    gui.click()
    time.sleep(0.5)
    gui.hotkey('ctrl', 'w')

# 登录QQ
def QQ_login():
    os.startfile(QQ_dir)
    print('正在打开QQ')
    time.sleep(3)
    gui.moveTo(960, 695, duration=0.5)
    gui.click()
    time.sleep(10)

if __name__ == "__main__":

    send_msg(people,message)

# 查看鼠标位置
while True:
    last_position=gui.position()
    if last_position!=gui.position():
        print(gui.position())

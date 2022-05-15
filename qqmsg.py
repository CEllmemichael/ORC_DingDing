import psutil,time,os
import pyperclip
import pyautogui as gui
def sendqqmasg(message):
    # peoples = ['政治觉悟提高群','小垃纪大聪明（小熊）']
    if message == 1:
        autoclick()
        peoples = ['政治觉悟提高群', '小垃纪大聪明（小熊）']
        msg = '魏树鸿的程序提示：现在签到'
    else:
        peoples = ['政治觉悟提高群',]
        msg = '魏树鸿的程序提示：有可能提问'
     # 好友全称
    # msg = message
    time.sleep(1)
    for people in peoples:
        gui.moveTo(1694, 1058, duration=0.2)
        gui.moveTo(1694, 1058, duration=0.2)
        gui.click()
        time.sleep(0.5)
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
        gui.moveTo(700, 900, duration=0.2)
        gui.click()
        pyperclip.copy(msg)
        gui.hotkey('ctrl', 'v')
        gui.hotkey('Enter')

        # 隐藏主界面并退出聊天界面
        gui.moveTo(1795, 127, duration=0.5)
        gui.click()
        time.sleep(0.5)
        gui.hotkey('ctrl', 'w')
        time.sleep(5)
def autoclick():
    for i in range(550,900):
        if i%30==0:
            print(i)
            gui.moveTo(600, i, duration=0.2)
            gui.click()
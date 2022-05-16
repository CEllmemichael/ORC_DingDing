from aip import AipOcr
from mails import mail
from mails import loop
from qqmsg import sendqqmasg,autoclick
APP_ID = "c"
API_KEY = "c"
SECRET_KEY = "c"
import pyautogui
import cv2
import numpy as np
import time
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def scrope(pic_path):
    image = get_file_content(pic_path)
    """ 如果有可选参数 """
    options = {}
    nn = 0
    wern = 0
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    print("正在识别图片信息......")
    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    result=client.basicGeneral(image, options)
    src=result['words_result']
    #print(len(src))
    dicfile=open('file.txt','a+',encoding='utf-8')
    for key in range(len(src)):
        if src[key]['words'] in ["我发起了课程签到，请及时处理","课程签到提醒",]:#and src[key]['words']not in ["签到结束","已签到"] :
            wern = 1
        if src[key]['words'] in ["在","在的"]:
            wern = 2
    if wern == 1:
        for key in range(len(src)):
            if wern == 1 and src[key]['words'] in ["签到结束","已签到","田恬老师老师发起的课程签到：签到结束"]:
                wern = 0
        # else:
        #     for x in src[key]['words']:
        #         if x in "签到结束时间":
        #             nn = nn + 1
        #     if nn>6:
        #         wern = 2

        dicfile.write(src[key]['words'])
        dicfile.write('\n')
        # print(src[key]['words'])
    dicfile.close()
    return wern


if __name__ == '__main__':
    times = 2
    num = 1
    while 1:
        time.sleep(times)
        img = pyautogui.screenshot(region=[370,300, 800, 570])  # 分别代表：左上角坐标，宽高
        # 对获取的图片转换成二维矩阵形式，后再将RGB转成BGR
        # 因为imshow,默认通道顺序是BGR，而pyautogui默认是RGB所以要转换一下，不然会有点问题
        img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("截屏", gray)
        if num == 1:
            cv2.imwrite('dashen_compressed.png', gray, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        gray2 = cv2.cvtColor(cv2.imread('dashen_compressed.png'), cv2.COLOR_BGR2GRAY)
        # print(np.mean(gray-gray2))
        # print(np.mean(gray - gray2))
        print(np.mean(gray - gray2))
        if np.mean(gray-gray2) >2:
            cv2.imwrite('dashen_compressed.png', gray, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            pic_path = r"dashen_compressed.png"
            # pic_path=r'111.png'
            wern = scrope(pic_path)
            print(wern)
            if wern!=0:
                # autoclick()
                sendqqmasg(wern)
                ret = loop(wern)
                times = 1000
                num = 0
            else:
                times = 2
        num = num + 1

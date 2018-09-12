#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Cavin Cao'

'''
	功能：利用百度官方api，读取图片中的文字，同时将文字转换成语音
    官方地址：http://ai.baidu.com/docs#/OCR-Python-SDK/top
    demo对应博文：
'''

import config
from aip import AipOcr,AipSpeech


""" 你的 APPID AK SK """
APP_ID = config.baidu_app_id
API_KEY = config.baidu_api_key
SECRET_KEY = config.baidu_secret_key

clientAipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
clientAipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

picture_url="http://image.bug2048.com/mongo20180906.jpg"


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

"""
    1.调用文字识别API识别图片上的文字
    2.拼接文字后调用语音合成API转换成语音
"""

def convert_picture_words():
    words=''
    wordsResult=clientAipOcr.basicGeneralUrl(picture_url)
    for item in wordsResult['words_result']:
        words+=item['words']+','
    if words=='':
        return
    words=words[:-1]
    print(words)
    speechResult=clientAipSpeech.synthesis(words, 'zh', 1, {
        'vol': 5,
        'per': 3
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(speechResult, dict):
        with open('result.mp3', 'wb') as f:
            f.write(speechResult)


if __name__ == '__main__':
    convert_picture_words()
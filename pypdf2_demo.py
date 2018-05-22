#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Cavin Cao'

'''
	功能：pypdf2类库基本操作demo
    官方地址：http://mstamy2.github.io/PyPDF2/
    这篇博文介绍的比较全面：https://blog.csdn.net/xingxtao/article/details/79056341
'''

import sys
import os
import os.path
from PyPDF2.pdf import PdfFileReader,PdfFileWriter
import time
time1=time.time()

def split_pdf(inFile, outFile): 
    '''
    拆分文档
    :param inFile:     输入文件
    :param outFile:    输出文件
    :return:
    '''
    pdfFileWriter = PdfFileWriter() 
    pdfFileReader = PdfFileReader(open(inFile, 'rb')) 
    page_count = pdfFileReader.getNumPages() 
    print(page_count) 
    # 将 pdf 第2页之后的页面，输出到一个新的文件 
    for i in range(2, page_count): 
        pdfFileWriter.addPage(pdfFileReader.getPage(i)) 
    pdfFileWriter.write(open(outFile, 'wb')) 

def mergePdf(inFileList, outFile):
    '''
    合并文档
    :param inFileList: 要合并的文档的 list
    :param outFile:    合并后的输出文件
    :return:
    '''
    pdfFileWriter = PdfFileWriter()
    #排序一下，不然合并序号不对
    inFileList=sorted(inFileList)
    for inFile in inFileList:
        # 依次循环打开要合并文件
        pdfReader = PdfFileReader(open(inFile, 'rb'))
        numPages = pdfReader.getNumPages()
        for index in range(0, numPages):
            pageObj = pdfReader.getPage(index)
            pdfFileWriter.addPage(pageObj)

        # 最后,统一写入到输出文件中
        pdfFileWriter.write(open(outFile, 'wb'))

def addBlankpage(inFile, outFile):
    '''
    pdf读取写入操作
    '''
    pdfFileWriter = PdfFileWriter()

    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(inFile)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    numPages = pdfFileReader.getNumPages()

    for index in range(0, numPages):
        pageObj = pdfFileReader.getPage(index)
        pdfFileWriter.addPage(pageObj)  # 根据每页返回的 PageObject,写入到文件
        pdfFileWriter.write(open(outFile, 'wb'))

    pdfFileWriter.addBlankPage()   # 在文件的最后一页写入一个空白页,保存至文件中
    pdfFileWriter.write(open(outFile,'wb'))


def getFileName(filepath):
    '''
    获取某个文件夹下文件
    '''
    file_list = []
    for root,dirs,files in os.walk(filepath):
        for filespath in files:
            file_list.append(os.path.join(root,filespath))
    return file_list



if __name__ == '__main__':
    file_path = r'/Users/cavin/Desktop/asd'
    fileNameList=getFileName(file_path)
    outFile=u"target.pdf"
    mergePdf(fileNameList,file_path+'/'+outFile)
    print('finished')

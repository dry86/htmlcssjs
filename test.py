import docx
from docx.api import Document
from bs4 import BeautifulSoup
from docx import Document
from zipfile import ZipFile






# file_dir_zip_raw = 'SE101-专题1作业：计算机硬件工作原理（2019-01-18前提交）-673.zip'


# print(file_dir_zip_raw[0:file_dir_zip_raw.rfind('.',1)])


# print(file_dir_zip_raw[::-1].split('.', 1)[-1][::-1])



# document=ZipFile(r'D:\\Graduation_Thesis\\vue-app\\flask\\upload\\智能硬件设备.docx')
# xml_content=document.read("word/document.xml")
# wordObj=BeautifulSoup(xml_content.decode("utf-8"),"xml")
# texts=wordObj.findAll("w:t")
# # print(texts)
# for text in texts:
#     print(text.text)



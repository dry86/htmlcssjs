from ltp import LTP
import os

#分句
ltp = LTP()


all_the_text = open('test-qust.txt',encoding='utf-8',errors='ignore')  #获取文件迭代器，而非一次性读入内存

paragraphs = []
for line in all_the_text:
    line=line.strip('\n')
    paragraphs.append(line)

print(paragraphs)

sents = ltp.sent_split(paragraphs)

for i in sents:
    print(i)
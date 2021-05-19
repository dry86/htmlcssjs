import gensim
from gensim.models.doc2vec import Doc2Vec, LabeledSentence
import os 
import jieba
import pandas as pd

TaggededDocument = gensim.models.doc2vec.TaggedDocument

#corpus文件夹 只需更改此处
CORPUS_FOLDER = r"upload\\SE101-专题2作业：关于Python语言(2019-01-18前提交）-685\\"

#input corpus seg
train_corpus = CORPUS_FOLDER+"a_zh_corpus_seg.txt"

#output model
saved_model = CORPUS_FOLDER+"a_model_doc2vec"

#停用词txt
stop_words_dir = "stop_list.txt"


#去掉回车换行
def delete_r_n(line):
    return line.replace("\r","").replace("\n","").strip()
 
#读取停用词
def get_stop_words(stop_words_dir):
    stop_words = []
 
    with open(stop_words_dir, "r", encoding='utf-8') as f_reader:
        for line in f_reader:
            line = delete_r_n(line)
            stop_words.append(line)
 
    stop_words = set(stop_words)
    return stop_words

#结巴精准分词
def jieba_cut(content, stop_words):
    word_list = []
 
    if content != "" and content is not None:
        seg_list = jieba.cut(content)
        for word in seg_list:
            if word not in stop_words:
                word_list.append(word)
 
    return word_list

# 加工中文
def preprocessing_text(text_dir, after_process_text_dir, stop_words_dir):
    stop_words = get_stop_words(stop_words_dir)
    setences = []
    f_writer = open(after_process_text_dir,"a", encoding='utf-8')
    count = 0
    with open(text_dir, "r", encoding='utf-8') as f_reader:
        for line in f_reader:
            # print(line)
            # line_list = line.split(",")
            # print(line_list)

            line= delete_r_n(line)
            word_list = jieba_cut(line, stop_words)

            setences.append(word_list)
            f_writer.write(" ".join(word_list) + "\n" )  # 
            f_writer.flush()

    f_writer.close()
    return setences


#将一个文件夹下的txt 写入语料库
def whole_dir(CORPUS_FOLDER):
    #input corpus seg
    train_corpus = CORPUS_FOLDER+"\\a_zh_corpus_seg.txt"

    for file in os.listdir(CORPUS_FOLDER):
        if file.endswith('.txt'):
            path = CORPUS_FOLDER +"/"+file 
            preprocessing_text(path,train_corpus,"stop_list.txt")

# whole_dir(CORPUS_FOLDER)

def get_corpus(CORPUS_FOLDER): 
    #input corpus seg
    train_corpus = CORPUS_FOLDER+"\\a_zh_corpus_seg.txt"

    doc = open(train_corpus, 'r', encoding='utf-8')
    docs = doc.readlines()
    train_docs = []
    for i, text in enumerate(docs):
        word_list = text.split(' ')
        length = len(word_list)
        #print(word_list)
        word_list[length - 1] = word_list[length - 1].strip()
        document = TaggededDocument(word_list, tags=[i])
        train_docs.append(document)
    return train_docs

def train_model(x_train,saved_model,vector_size=200, epoch_num=70):

    model_dm = Doc2Vec(x_train, min_count=5, window=8, vector_size=vector_size, sample=1e-3, negative=5, workers=4)
    model_dm.train(x_train, total_examples=model_dm.corpus_count, epochs=epoch_num)
    model_dm.save(saved_model)
    return model_dm

# x_train = get_corpus()
# train(x_train,saved_model)

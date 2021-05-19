 # -*- coding:utf-8 -*-
import gensim
from gensim.models.doc2vec import Doc2Vec, LabeledSentence
import jieba
import math
TaggededDocument = gensim.models.doc2vec.TaggedDocument

saved_model = "upload\\SE101-专题2作业：关于Python语言(2019-01-18前提交）-685\\"+"a_model_doc2vec"


def use_model(test_text):
    model_dm = Doc2Vec.load(saved_model)
    
    text_cut = jieba.cut(test_text)
    text_raw = []
    for i in list(text_cut):
        text_raw.append(i)
    inferred_vector_dm = model_dm.infer_vector(text_raw)
    # print(inferred_vector_dm)
    sims = model_dm.docvecs.most_similar([inferred_vector_dm], topn=5)
 
    return sims



txt='Python 种 脚本语言   开发 代码 效率 高 具有 强大 丰富 实用 第三方 标准 库 编程 变得 简洁 快速 Python 语言 语法 表达 优美 易读 Python 支持 广泛 程序开发 简单 文字处理 Web 开发 游戏 设计 应用 Python 语言   C C++ Java 语言 脚本语言 比较 国内 知名度 不高 常见 编程语言 比较 许多 优秀 表现 Python   语言 Python   语言 实际 教学内容 分支 循环 函数 程序逻辑 关系 功能强大 函数库 应用 目前 最 接近 自然语言 通用 编程语言 语言 只 关心 计算 问题 求解 轻量级 语法 高层次 语言 表示 表达 应用 计算机 解决问题 计算 思维 理念 Python   语言 抽象 问题 解决方案 自动化 问题 求解 复杂 信息系统 时代 利用计算机 解决问题 最 直观 表达 工具   Python   著名 特性 ① 字典 ② 切片 ③ 生成式 ④ 生成器 ⑤ 逗号 用法 ⑥ 简单 循环 ⑦ 浅 拷贝 深 拷贝 ⑧ 类 属性 实例 属性 ⑨ 装饰 器 ⑩ 正则表达式 帮助 Python 库 第三方 库 了解 运用 程度 结合 人工智能 编程 思路 带领 了解 人工智能 日常生活 中 运用 大型项目 无法 直接 入手 课程 教学活动 中需 帮助 了解 大型项目 开发 流程 模块 分割 联合 调试 使 学会 协作 编程 提高 企业 项目 编程 能力'
sims = use_model(txt)
print(sims)
for i,score_data in enumerate(sims):
    if i == 0:
        continue
    id,score=score_data
    if round(score-0.355,4) > 0:
        print(id)
        print(round(score,5))
    


# for count, sim in sims:
    # sentence = x_train[count]
    # words = ''
    # for word in sentence[0]:
    #     words = words + word + ' '
    # print(words, sim, len(sentence[0]))



from flask import Flask,request,jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.linalg import norm

app = Flask(__name__)
CORS(app)

@app.route('/')
def Compare():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    return jsonify(result=a + b)    # 返回json 形式的结果

@app.route('/compare_string')
def tfidf_similarity():
    s1 = request.args.get('a',type=str,default=None)
    s2 = request.args.get('b',type=str,default=None)
    def add_space(s):
        return ' '.join(list(s))
    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]  #语料库
    #print(corpus)
    vectors = cv.fit_transform(corpus).toarray()

    # 计算TF系数
    result=np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))
    return jsonify(result)
        #计算余弦值cosθ
if __name__ == '__main__':
    app.run()
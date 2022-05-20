#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author Xu
# @date 2022/5/19
# @file GloveModel.py
import os

from gensim.models.word2vec import Text8Corpus

import DatasetPre
import gensim.models as w2v
import gensim

class GloveModel(DatasetPre.DatasetPre):
    def __init__(self):
        super(GloveModel, self).__init__()
        self.object_net=['杨过','郭靖','段誉','降龙十八掌','全真剑法','武当派','屠龙刀','功夫']
        pass

    def trainModel(self):
        model1 = w2v.Word2Vec(sentences=Text8Corpus((self.file + '\\'  + 'corpus.txt')), vector_size=200, window=5, min_count=5, sg=0,workers=8)
        model1.save('model_cbow.model')
        model2 = w2v.Word2Vec(sentences=Text8Corpus((self.file + '\\' + 'corpus.txt')), vector_size=200, window=5, min_count=5,sg=1, workers=8)
        model2.save( 'model_skip.model')

    def modelBasedAnalysis(self):
        model_cbow=gensim.models.Word2Vec.load("model_cbow.model")
        print("-"*40)
        print("主角相关词")
        for i in self.object_net:
            word=model_cbow.wv.most_similar(str(i), topn=10)
            print('{}前十个最相关词{}'.format(i,word))
        print("-" * 40)
        print("相关词推理")
        word1 = model_cbow.wv.most_similar(positive=['郭靖','黄蓉'],negative=['小龙女'],topn=1)
        print('根据郭靖+黄蓉=小龙女+X,找到X:{},对应概率：{}'.format( word1[0][0],word1[0][1]))
        word2 = model_cbow.wv.most_similar(positive=['黄蓉', '打狗棒法'], negative=['洪七公'], topn=10)
        print('根据黄蓉+打狗棒法=洪七公+X，找到X:{},对应概率：{}'.format(word2[0][0], word2[0][1]))
        word3=model_cbow.wv.doesnt_match("郭靖 小龙女 门户 段誉".split())
        print('郭靖\小龙女\门户\段誉中排除异类的词是:{}'.format(word3))
        word4 = model_cbow.wv.doesnt_match("乔峰 虚竹 段延庆 段誉".split())
        print('乔峰\虚竹\段延庆\段誉中排除异类的词是:{}'.format(word4))
        word5 = model_cbow.wv.doesnt_match("木婉清 阿朱 王语嫣 阿碧".split())
        print('阿朱\木婉清\王语嫣\阿碧中排除异类的词是:{}'.format(word5))
        print("-" * 40)
        print("相似度")
        word6 = model_cbow.wv.similarity("段誉","王语嫣")
        word7 = model_cbow.wv.similarity("段誉","钟灵")
        word8 = model_cbow.wv.similarity("段誉","木婉清")
        print("段誉喜欢王语嫣/钟灵/木婉清的程度:{}{}{}".format(word6,word7,word8))
        model_skip = gensim.models.Word2Vec.load("model_skip.model")
        print("-" * 40)
        print("主角相关词")
        for i in self.object_net:
            word = model_skip.wv.most_similar(str(i), topn=10)
            print('{}前十个最相关词{}'.format(i, word))
        print("-" * 40)
        print("相关词推理")
        word1 = model_skip.wv.most_similar(positive=['郭靖', '黄蓉'], negative=['小龙女'], topn=1)
        print('根据郭靖+黄蓉=小龙女+X,找到X:{},对应概率：{}'.format(word1[0][0], word1[0][1]))
        word2 = model_skip.wv.most_similar(positive=['黄蓉', '打狗棒法'], negative=['洪七公'], topn=10)
        print('根据黄蓉+打狗棒法=洪七公+X，找到X:{},对应概率：{}'.format(word2[0][0], word2[0][1]))
        word3 = model_skip.wv.doesnt_match("郭靖 小龙女 门户 段誉".split())
        print('郭靖\小龙女\门户\段誉中排除异类的词是:{}'.format(word3))
        word4 = model_skip.wv.doesnt_match("乔峰 虚竹 段延庆 段誉".split())
        print('乔峰\虚竹\段延庆\段誉中排除异类的词是:{}'.format(word4))
        word5 = model_skip.wv.doesnt_match("木婉清 阿朱 王语嫣 阿碧".split())
        print('阿朱\木婉清\王语嫣\阿碧中排除异类的词是:{}'.format(word5))
        print("-" * 40)
        print("相似度")
        word6 = model_skip.wv.similarity("段誉", "王语嫣")
        word7 = model_skip.wv.similarity("段誉", "钟灵")
        word8 = model_skip.wv.similarity("段誉", "木婉清")
        print("段誉喜欢王语嫣/钟灵/木婉清的程度:{}{}{}".format(word6, word7, word8))
if __name__ == '__main__':
    glove=GloveModel()
    # glove.trainModel()
    glove.modelBasedAnalysis()




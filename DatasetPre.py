#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author Xu
# @date 2022/5/19
# @file DatasetPre.py
import jieba
import gensim.models as w2v

class DatasetPre():
    def __init__(self):
        self.file='./fiction'
        with open(self.file+'/inf.txt') as file:
            self.text = file.read()
        file.close()
        self.rabbish=['本书来自www.cr173.com免费txt小说下载站\n更多更新免费电子书请关注www.cr173.com', '----〖新语丝电子文库(www.xys.org)〗', '新语丝电子文库','\u3000', '\n', '。', '？', '！', '，', '；', '：', '、', '《', '》', '“', '”', '‘', '’', '［', '］', '....', '......', '『', '』', '（', '）', '…', '「', '」', '\ue41b', '＜', '＞', '+', '\x1a', '\ue42b']

    def content_clean(self,data):
        for i in self.rabbish:
             data= data.replace(i, '')
        return data


    def textAbstract(self):
        path=self.file
        files = self.text
        with open('./trainset/stop_word.txt') as file:
            stop_word_list = file.read()
        file.close()
        with open('./trainset/小说人物.txt') as file:
            people_names=list()
            for line in file.readlines():
                line=line.strip()
                jieba.add_word(line)
                people_names.append(line)
        file.close()
        with open('./trainset/小说武功.txt') as file:
            kongfu_names = list()
            for line in file.readlines():
                line = line.strip()
                jieba.add_word(line)
                kongfu_names.append(line)
        file.close()
        with open('./trainset/小说门派.txt') as file:
            menpai_names = list()
            for line in file.readlines():
                line = line.strip()
                jieba.add_word(line)
                menpai_names.append(line)
        file.close()
        data_txt = ''
        seg_novel=[]
        with open((path + '\\' + 'corpus.txt'), 'w', encoding='utf-8') as corpus:
            for file in files.split(','):
                forward_rows = len(seg_novel)
                with open((path + '\\' + file + '.txt' ), 'r', encoding='ANSI') as f:
                    text = f.read().split('。')
                    for num in range(len(text)):
                        data=text[num]
                        data = self.content_clean(data)
                        data = jieba.lcut(data)
                        tmp=''
                        for word in data:
                            if word not in stop_word_list:
                                if word !='\t':
                                    if word[:2] in people_names:
                                        word=word[:2]
                                tmp+=(word+' ')
                        if len(str(tmp.strip())) != 0:
                            seg_novel.append(str(tmp.strip()).split())
                        data_txt+=(tmp+'\n')
                    print("{} finished，with {} Row".format(file, len(seg_novel)-forward_rows))
                    print("-" * 40)
                    f.close()
            print("-" * 40)
            print("-" * 40)
            print("All finished，with {} Row".format(len(seg_novel)))
            corpus.write(data_txt)
            corpus.close()
        # model = w2v.Word2Vec(sentences=seg_novel, size=200, window=5, min_count=5, sg=0)
        # model.save(data_path + 'all_CBOW.model')
        return data_txt, files





    '''
    
            path = os.path.join(data_roots, tmp_file_name)
            if os.path.isfile(path):
                with open(path, "r", encoding="gbk", errors="ignore") as tmp_file:
                    tmp_file_context = tmp_file.read()
                    tmp_file_lines = tmp_file_context.split("。")
                    for tmp_line in tmp_file_lines:
                        for tmp_char in char_to_be_replaced:
                            tmp_line = tmp_line.replace(tmp_char, "")
                        # for tmp_char in stop_words_list:
                        #     tmp_line = tmp_line.replace(tmp_char, "")
                        tmp_line = tmp_line.replace("本书来自免费小说下载站更多更新免费电子书请关注", "")
                        if tmp_line == "":
                            continue
                        tmp_line = list(jieba.cut(tmp_line))
                        tmp_line_seg = ""
                        for tmp_word in tmp_line:
                            tmp_line_seg += tmp_word + " "
                        output_file.write(tmp_line_seg.strip() + "\n")

        output_file.close()
        print("Data succesfully prepared!")
    
    '''

if __name__ == '__main__':
    datasetPre=DatasetPre()
    datasetPre.textAbstract()

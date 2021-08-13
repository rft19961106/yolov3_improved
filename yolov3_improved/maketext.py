import os
import random

trainval_percent = 0.3  #test和val一共占的比例
train_percent = 0   #test所占比例
txtfilepath = 'data/labels'
txtsavepath = 'data/ImageSets'
total_txt = os.listdir(txtfilepath)#返回path指定的文件夹包含的文件或文件夹的名字的列表

num = len(total_txt)
list = range(num)#创建一个整数列表
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('data/ImageSets/trainval.txt', 'w')#‘w’打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
ftest = open('data/ImageSets/test.txt', 'w')
ftrain = open('data/ImageSets/train.txt', 'w')
fval = open('data/ImageSets/val.txt', 'w')

for i in list:
    name = total_txt[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
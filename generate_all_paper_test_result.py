import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from models import SimpleFeatureExtractor,LogReg

# class SimpleClassifier(nn.Module):
#     def __init__(self, n_in, n_h, nb_classes):
#         super(SimpleClassifier, self).__init__()
#         self.fc = SimpleFeatureExtractor(n_in, n_h)
#         self.out = LogReg(n_h, nb_classes)
#
#     def forward(self, input_data):
#         h = self.fc(input_data)
#         res = self.out(h)
#         return res

class SimpleClassifier(nn.Module):
    def __init__(self, n_in, n_h, n_h1, nb_classes):
        super(SimpleClassifier, self).__init__()
        self.fc = SimpleFeatureExtractor(n_in, n_h)
        # self.fc1 = SimpleFeatureExtractor(n_h, n_h1)
        self.out = LogReg(n_h, nb_classes)
        self.dropout = nn.Dropout(p=0.2)

    def forward(self, input_data):
        h = self.fc(input_data)
        h = self.dropout(h)
        # h = self.fc1(h)
        res = self.out(h)
        return res

weight_path = 'weights/test36_99.pth'
model = torch.load(weight_path)

feature_dict = {}
# with open('features/total_feature_l.txt', 'r') as f:
with open('features/total_feature_all_meta_512_ABC.txt', 'r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        # print(split_content)
        cur_paper_id = int(split_content[0])
        # if cur_paper_id < 4844:
        #     continue
        feature_dict[cur_paper_id] = [float(split_content[1])]
        for feat_num in split_content[2:-1]:
            feature_dict[cur_paper_id].append(float(feat_num))

def get_feature(index):
    global feature_dict
    # global true_labels
    # if index < 4844:
    #     return np.array(true_labels[index])
    # else:
    return np.array(feature_dict[index])

# start_ind = 4844
# end_ind = 24251
# # start_ind = 1
# # end_ind = 101
#
# testX = torch.Tensor([get_feature(i) for i in range(start_ind,end_ind)])
# with torch.no_grad():
#     testY = model(testX)
#
# predictions = zip(range(start_ind,end_ind),list(testY.max(1)[1].data.tolist()))
# for (i,x) in predictions:
#     print(i,x)

model.eval()

with open('mid_result/ABC_2048_99.txt','a+') as f:
    X = [get_feature(i) for i in range(24251)]
    testX = torch.Tensor(X)
    with torch.no_grad():
        testY = model(testX)
    predictions = zip(range(24251), list(testY.max(1)[1].data.tolist()))
    for (i, x) in predictions:
        # print(i, x)
        # print(i) # 当前检测paper
        if i < 4844:
            continue
        else:
            f.write(str(i)+" ")
            f.write(str(x)+"\n")


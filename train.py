import torch
import numpy as np
import torch.nn as nn
from models import SimpleFeatureExtractor, LogReg

# get the feature
feature_dict = {}
with open('features/total_feature_meta.txt', 'r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        # print(split_content)
        cur_paper_id = int(split_content[0])
        if cur_paper_id == 4844:
            break
        feature_dict[cur_paper_id] = [float(split_content[1])]
        for feat_num in split_content[2:-1]:
            feature_dict[cur_paper_id].append(float(feat_num))


def get_feature(index):
    global feature_dict
    return np.array(feature_dict[index])


def get_labels():
    total_labels = []
    with open('labels.txt', 'r') as f:
        for line in f.readlines():
            split_content = line.split(' ')
            cur_label = int(split_content[1])
            total_labels.append(cur_label)
    return total_labels


trX = torch.Tensor([get_feature(i) for i in range(4844)])
trY = torch.LongTensor(get_labels())
print(trX.shape)
print(trY.shape)

NUM_FEATURE = 256
# NUM_FEATURE = 128
NUM_HIDDEN = 250

class SimpleClassifier(nn.Module):
    def __init__(self, n_in, n_h, nb_classes):
        super(SimpleClassifier, self).__init__()
        self.fc = SimpleFeatureExtractor(n_in, n_h)
        self.out = LogReg(n_h, nb_classes)

    def forward(self, input_data):
        h = self.fc(input_data)
        res = self.out(h)
        return res

# model = torch.nn.Sequential(
#     torch.nn.Linear(NUM_FEATURE,NUM_HIDDEN),
#     torch.nn.ReLU(),
#     torch.nn.Linear(NUM_HIDDEN,10)
# )

# torch.nn.init.normal_(model[0].weight)
# torch.nn.init.normal_(model[2].weight)

model = SimpleClassifier(NUM_FEATURE,NUM_HIDDEN,10)

# 定义loss和优化器
loss_fn = torch.nn.CrossEntropyLoss()
# optimizer = torch.optim.SGD(model.parameters(),lr=0.005)
optimizer = torch.optim.Adam(model.parameters(),lr=0.0001)

# 开始训练
BATCH_SIZE = 64 # 批处理量
EPOCH_NUM = 10000
for epoch in range(EPOCH_NUM):
    for start in range(0,len(trX),BATCH_SIZE):
        end = start + BATCH_SIZE
        batchX = trX[start:end]
        batchY = trY[start:end]
        y_pred = model(batchX)
        loss = loss_fn(y_pred,batchY)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    # 计算当前批次产生的loss
    loss = loss_fn(model(trX),trY).item()
    print("Epoch:",epoch,"Loss:",loss)
    if epoch % 1000 == 999:
        torch.save(model, 'weights/test10_'+str(epoch)+".pth")

torch.save(model,'weights/test10.pth')
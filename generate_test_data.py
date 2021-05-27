import torch
import numpy as np
import pandas as pd

weight_path = 'weights/test6.pth'
model = torch.load(weight_path)

feature_dict = {}
with open('features/total_feature.txt', 'r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        # print(split_content)
        cur_paper_id = int(split_content[0])
        # if cur_paper_id < 4844:
        #     continue
        feature_dict[cur_paper_id] = [float(split_content[1])]
        for feat_num in split_content[2:-1]:
            feature_dict[cur_paper_id].append(float(feat_num))

# true_labels = {}
# with open('labels.txt','r') as f:
#     for line in f.readlines():
#         split_content = line.split(' ')
#         cur_paper_id = int(split_content[0])
#         true_labels[cur_paper_id] = int(split_content[1])

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

csv_list = []

with open('papers_to_pred.txt','r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        # print(split_content)
        cur_author_id = int(split_content[0])
        cur_dict = {}
        cur_dict["author_id"] = cur_author_id
        cur_papers = []
        for paper_num in split_content[1:-1]:
            cur_papers.append(int(paper_num))
        # if cur_papers == []:
        #     continue
        testX = torch.Tensor([get_feature(i) for i in cur_papers])
        with torch.no_grad():
            testY = model(testX)

        predictions = zip(cur_papers, list(testY.max(1)[1].data.tolist()))
        cur_author_papers = set()
        for (i, x) in predictions:
            # print(i, x)
            cur_author_papers.add(x)
        res = ''
        for i in cur_author_papers:
            res += str(i) + " "
        cur_dict["labels"] = res
        csv_list.append(cur_dict)

df = pd.DataFrame(csv_list,columns=["author_id","labels"])
df.to_csv("result/test3.csv",index=False)
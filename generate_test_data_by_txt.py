import torch
import torch.nn as nn
import numpy as np
import pandas as pd

true_labels = {}
with open('labels.txt','r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        cur_paper_id = int(split_content[0])
        true_labels[cur_paper_id] = int(split_content[1])

pred_labels = {}
with open('mid_result/final_5.txt','r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        cur_paper_id = int(split_content[0])
        pred_labels[cur_paper_id] = int(split_content[1])

csv_list = []

true_num = 0
pred_num = 0

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
        cur_author_papers = set()
        for i in cur_papers:
            if i < 4844:
                cur_author_papers.add(true_labels[i])
                true_num += 1
            else:
                cur_author_papers.add(pred_labels[i])
                pred_num += 1
        res = ''
        for i in cur_author_papers:
            res += str(i) + " "
        cur_dict["labels"] = res
        csv_list.append(cur_dict)

df = pd.DataFrame(csv_list,columns=["author_id","labels"])
df.to_csv("result/test34.csv",index=False)
print(true_num)
print(pred_num)
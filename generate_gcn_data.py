# haven't done yet.
import numpy as np
import tqdm
import pandas as pd

paper_to_author = {}
with open('all_paper_to_authors.txt','r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        # print(split_content)
        cur_paper_id = "v" + split_content[0]
        paper_to_author[cur_paper_id] = [int(split_content[1])]
        for feat_num in split_content[2:-1]:
            paper_to_author[cur_paper_id].append(int(feat_num))

# print(paper_to_author)

with open('features/paper_features.csv','a+') as f:
    f.write('paper_id'+',')
    for i in range(42613):
        cur_key = 'w'+str(i)
        f.write(cur_key+',')
    f.write('w42614')
    for key in paper_to_author:
        cur_paper = key
        cur_authors = paper_to_author[key]
        cur_feature = [0] * 42614
        for author in cur_authors:
            cur_feature[author] = 1
        f.write(cur_paper+',')
        for i in range(42613):
            f.write(str(cur_feature[i])+',')
        f.write(str(cur_feature[42613]))

# 保存为csv
# total_feature_list = []
# for key in paper_to_author:
#     cur_paper = key
#     cur_authors = paper_to_author[key]
#     cur_feature = [0] * 42614
#     for author in cur_authors:
#         cur_feature[author] = 1
#     cur_dict = {}
#     cur_dict['paper_id'] = cur_paper
#     for i in range(42614):
#         cur_feature_key = 'w'+str(i)
#         cur_dict[cur_feature_key] = cur_feature[i]
#     total_feature_list.append(cur_dict)
#
#
# columns = ['paper_id']
# for i in range(42614):
#     cur_key = 'w'+str(i)
#     columns.append(cur_key)
#
# df = pd.DataFrame(total_feature_list,columns=columns)
# df.to_csv("features/paper_features.csv",index=False)

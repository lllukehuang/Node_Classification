# 处理所有文章节点的边， 转化成 node1 node2 <权重用于表示引用还是被引用关系>

import pandas as pd

input_path = "origin_data/paper_reference.csv"
references = pd.read_csv(input_path)

total_length = len(references)

# print(len(references))
# print(references["paper_id"][0])
# print(references["reference_id"][0])

with open('graph.edgelist','a+') as f:
    for i in range(total_length):
        cur_id1 = references["paper_id"][i]
        cur_id2 = references["reference_id"][i]
        f.write(str(cur_id1)+" "+str(cur_id2)+"\n")
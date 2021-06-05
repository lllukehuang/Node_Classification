import pandas as pd

total_feature_list = []
input_path = "author_paper_all_with_year.csv/author_paper_all_with_year.csv"
references = pd.read_csv(input_path)
total_length = len(references)
for i in range(total_length):
    cur_paper = "v"+str(references["paper_id"][i])
    cur_author = "a"+str(references["author_id"][i])
    cur_year = "i"+str(references["year"][i])
    cur_dict = {}
    cur_dict["author_id"] = cur_author
    cur_dict["paper_id"] = cur_paper
    cur_dict["year"] = cur_year
    total_feature_list.append(cur_dict)

df = pd.DataFrame(total_feature_list,columns=["author_id","paper_id","year"])
df.to_csv("features/author_paper_year.csv",index=False)

total_feature_list = []
input_path = "origin_data/paper_reference.csv"
references = pd.read_csv(input_path)
total_length = len(references)
for i in range(total_length):
    cur_paper = "v"+str(references["paper_id"][i])
    cur_author = "v"+str(references["reference_id"][i])
    # cur_year = "i"+str(references["year"][i])
    cur_dict = {}
    cur_dict["reference_id"] = cur_author
    cur_dict["paper_id"] = cur_paper
    # cur_dict["year"] = cur_year
    total_feature_list.append(cur_dict)

df = pd.DataFrame(total_feature_list,columns=["paper_id","reference_id"])
df.to_csv("features/paper_paper.csv",index=False)

total_feature_list = []
with open('labels.txt','r') as f:
    for line in f.readlines():
        split_content = line.split(' ')
        cur_paper_id = "v" + split_content[0]
        cur_label = split_content[1][:-1]
        cur_dict = {}
        cur_dict["paper_id"] = cur_paper_id
        cur_dict["label"] = cur_label
        total_feature_list.append(cur_dict)

df = pd.DataFrame(total_feature_list,columns=["paper_id","label"])
df.to_csv("features/paper_labels.csv",index=False)
import pandas as pd

input_path = "origin_data/labeled_papers_with_authors.csv"
references = pd.read_csv(input_path)
total_length = len(references)
label_dict = {}
for i in range(total_length):
    cur_paper = references["paper_id"][i]
    cur_label = references["label"][i]
    if cur_paper not in label_dict:
        label_dict[cur_paper] = cur_label

with open('labels.txt','a+') as f:
    for key in label_dict:
        f.write(str(key)+' '+str(label_dict[key])+"\n")
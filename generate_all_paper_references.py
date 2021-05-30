import pandas as pd

total_reference_dict = {}
input_path = "origin_data/paper_reference.csv"
references = pd.read_csv(input_path)
total_length = len(references)
for i in range(total_length):
    cur_paper = references["paper_id"][i]
    cur_reference = references["reference_id"][i]
    if cur_paper in total_reference_dict:
        total_reference_dict[cur_paper].append(cur_reference)
    else:
        total_reference_dict[cur_paper] = [cur_reference]


with open('features/all_paper_reference.txt',"a+") as f:
    for key in range(24251):
        f.write(str(key)+' ')
        if key in total_reference_dict:
            cur_author_feature = total_reference_dict[key]
        else:
            cur_author_feature = [key]
        for feat in cur_author_feature:
            f.write(str(feat) + ' ')
        f.write("\n")
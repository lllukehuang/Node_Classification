import pandas as pd

total_feature_dict = {}
input_path = "../author_paper_all_with_year.csv/author_paper_all_with_year.csv"
references = pd.read_csv(input_path)
total_length = len(references)
for i in range(total_length):
    cur_paper = references["paper_id"][i]
    cur_year = references["year"][i]
    if cur_year in total_feature_dict:
        total_feature_dict[cur_year].append(cur_paper)
    else:
        total_feature_dict[cur_year] = [cur_paper]


with open('all_year_to_paper.txt', 'a+') as f:
    for key in total_feature_dict:
        f.write(str(key)+' ')
        cur_author_feature = total_feature_dict[key]
        for feat in cur_author_feature:
            f.write(str(feat)+" ")
        f.write("\n")
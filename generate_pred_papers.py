import pandas as pd

author_list = []
# input_path = "origin_data/authors_to_pred.csv"
# references = pd.read_csv(input_path)
# total_length = len(references)
# for i in range(total_length):
#     cur_author = references["author_id"][i]
#     author_list.append(cur_author)

# 获取所有author
for i in range(42614):
    author_list.append(i)

pred_paper_dict = {}
input_path = "author_paper_all_with_year.csv/author_paper_all_with_year.csv"
references = pd.read_csv(input_path)
total_length = len(references)
for i in range(total_length):
    cur_author = references["author_id"][i]
    if cur_author not in author_list:
        continue
    cur_paper = references["paper_id"][i]
    if cur_author in pred_paper_dict:
        pred_paper_dict[cur_author].append(cur_paper)
    else:
        pred_paper_dict[cur_author] = [cur_paper]
# print(author_list)
with open('all_author_to_papers.txt',"a+") as f:
    for a in author_list:
        f.write(str(a)+" ")
        pred_papers = pred_paper_dict[a]
        for paper in pred_papers:
            f.write(str(paper)+" ")
        f.write("\n")
import pandas as pd

paper_to_author_dict = {}
input_path = "author_paper_all_with_year.csv/author_paper_all_with_year.csv"
references = pd.read_csv(input_path)
total_length = len(references)
for i in range(total_length):
    cur_author = references["author_id"][i]
    cur_paper = references["paper_id"][i]
    if cur_paper in paper_to_author_dict:
        paper_to_author_dict[cur_paper].append(cur_author)
    else:
        paper_to_author_dict[cur_paper] = [cur_author]

with open('all_paper_to_authors.txt',"a+") as f:
    for a in paper_to_author_dict:
        f.write(str(a)+" ")
        authors = paper_to_author_dict[a]
        for author in authors:
            f.write(str(author) + " ")
        f.write("\n")
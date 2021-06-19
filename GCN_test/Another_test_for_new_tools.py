from stellargraph import StellarGraph
from stellargraph import StellarDiGraph
import pandas as pd
import numpy as np

from sklearn import model_selection, preprocessing

# 加载图数据
input_path = "../features/author_paper_year.csv"
author_paper = pd.read_csv(input_path)
author_to_paper_edge = author_paper[["author_id","paper_id"]]
# author_nodes = author_paper[["author_id"]]
# paper_nodes = author_paper[["paper_id"]]
author_to_paper_edge = author_to_paper_edge.rename(columns={'author_id':'source','paper_id':'target'})
# print(author_to_paper_edge)
# 读取paper ref信息
input_path1 = "features/paper_paper.csv"
references = pd.read_csv(input_path1)
references = references.rename(columns={'paper_id':'source','reference_id':'target'})
author_to_paper_edge = pd.concat([author_to_paper_edge,references],ignore_index=True)
# print(author_to_paper_edge)


author_list = []
paper_list = []
for i in range(24251):
    cur_paper = "v"+str(i)
    paper_list.append(cur_paper)

for i in range(42614):
    cur_author = "a"+str(i)
    author_list.append(cur_author)
author_nodes = pd.DataFrame(index=author_list)
paper_nodes = pd.DataFrame(index=paper_list)


# author_nodes = np.array(author_nodes).tolist()
# paper_nodes = np.array(paper_nodes).tolist()
#
# author_nodes_ = pd.DataFrame(index=author_nodes)
# paper_nodes_ = pd.DataFrame(index=paper_nodes)
# print(author_nodes_)
# print(paper_nodes_)

# print(author_to_paper_edge)
# square = StellarDiGraph(edges=author_to_paper_edge,source_column='author_id',target_column='paper_id')
# print(square.info())

square_author_and_paper = StellarDiGraph({"author": author_nodes, "paper": paper_nodes}, edges=author_to_paper_edge)
print(square_author_and_paper.info())

# 生成对应的标签
# input_path2 = "features/paper_labels.csv"
input_path2 = "origin_data/labeled_papers_with_authors.csv"
paper_labels = pd.read_csv(input_path2)
paper_labels = paper_labels[["paper_id","label"]]
print(paper_labels)
# print(type(paper_labels))
# test = paper_labels["paper_id"]
# print(test)
paper_labels = paper_labels.drop_duplicates(subset=['paper_id', 'label'], keep='first')
paper_labels.set_index("paper_id",drop=True, append=False, inplace=True)
print(paper_labels)


# print(paper_labels[["paper_id","label"]])
# paper_labels_series = pd.Series(paper_labels.to_numpy(copy=False).ravel('F'))
# paper_labels_series = paper_labels.to_numpy()
paper_labels_series = paper_labels.values
print(paper_labels_series)

# print(type(paper_labels_series[0][0]))

train_subjects, test_subjects = model_selection.train_test_split(
    paper_labels_series, train_size=0.75, test_size=None, stratify=paper_labels_series
)
train_subjects, val_subjects = model_selection.train_test_split(
    train_subjects, train_size=0.75, test_size=None, stratify=train_subjects
)

# print(train_subjects)

target_encoding = preprocessing.LabelBinarizer()

train_targets = target_encoding.fit_transform(train_subjects)
val_targets = target_encoding.transform(val_subjects)
test_targets = target_encoding.transform(test_subjects)

print(train_targets.shape)


from pandas.core.frame import DataFrame
from stellargraph import StellarDiGraph, StellarGraph
import pandas as pd
import numpy as np


def find_coauthor(df:DataFrame):
    print("Searching for co-authors...")
    source = []
    target = []
    new_df = df.copy()
    for row in new_df.itertuples():
        # print('---------------------------------')
        paper = getattr(row, 'paper_id')
        search_paper = new_df[new_df.paper_id==paper]

        if (search_paper.shape[0]==0):
            continue
        elif (search_paper.shape[0]==1):
            # print("Paper {} has only one author {}.".format(paper, search_paper['author_id']))
            new_df = new_df.drop(search_paper.index)
            if paper not in new_df.paper_id:
                # print("Paper {} deleted from new_df.".format(paper))
                if (new_df.shape[0]==0):
                    print("Search finish!")
                    # print(len(source))
                    return source, target
            # else:
                # print("Fail to delete!")
        else:
            author_list = search_paper['author_id'].tolist()
            # print("Paper {} is written by {}".format(paper, author_list))
            for a1 in author_list:
                tmp_author_list = author_list.copy()
                tmp_author_list.remove(a1)                
                for a2 in tmp_author_list:
                    source.append(a1)
                    target.append(a2)

            new_df = new_df.drop(search_paper.index)
            if paper not in new_df.paper_id:
                # print("Paper {} deleted from new_df.".format(paper))
                if (new_df.shape[0]==0):
                    print("Search finish!")
                    # print(len(source))
                    return source, target
            # else:
                # print("Fail to delete!")
        # print('---------------------------------\n')


### Load Raw Data ###
paper_author_info = pd.read_csv("./labeled_papers_with_authors.csv")
paper_reference_info = pd.read_csv("./paper_reference.csv")
# Pre-processing
print("Processing data...")
paper_reference_info = paper_reference_info[(paper_reference_info['paper_id']<4844) & (paper_reference_info['reference_id']<4844)].reset_index()

paper_author_info['author_id'] = paper_author_info['author_id'].apply(lambda x:'a' + str(int(x)))
paper_author_info['paper_id'] = paper_author_info['paper_id'].apply(lambda x:'p' + str(int(x)))

paper_reference_info['paper_id'] = paper_reference_info['paper_id'].apply(lambda x:'p' + str(int(x)))
paper_reference_info['reference_id'] = paper_reference_info['reference_id'].apply(lambda x:'p' + str(int(x)))
# print(paper_author_info)
# print(paper_reference_info)

### Edges Construction ###
print("Constructing edges...")
source = []
target = []

# paper -> paper (one_way)
ori_paper = paper_reference_info['paper_id'].tolist()
ref_paper = paper_reference_info['reference_id'].tolist()

# author -> paper (one-way)
author1 = paper_author_info['author_id'].tolist()
paper1 = paper_author_info['paper_id'].tolist()

# author <-> author (two-way)
author2, author3 = find_coauthor(paper_author_info)

print(ori_paper[0:50])
print(author1[0:50])
square_edges = {
    "p2p": pd.DataFrame({"source": ori_paper, "target": ref_paper}),
    # "a2p": pd.DataFrame({"source": author1, "target": paper1}),
    "a2a": pd.DataFrame({"source": author2, "target": author3})
}

### Nodes Construction ###
print("Constructing nodes...")
# paper nodes (with labels)
paper_node_info = pd.DataFrame({"paper_id":paper_author_info['paper_id'], "label":paper_author_info['label']}).drop_duplicates().reset_index()
square_paper = pd.DataFrame({"conference":paper_node_info['label']}, index=paper_node_info['paper_id'])

# author nodes (no labels)
author_node_info = pd.DataFrame({"author_id":paper_author_info['author_id']}).drop_duplicates().reset_index()
square_author = pd.DataFrame(index=author_node_info['author_id'])


### Merge ###
print("Constructing graph...")
square_paper_and_author = StellarGraph(
    {"paper":square_paper, "author":square_author},
    square_edges)
print('==================================')
print(square_paper_and_author.info())
print('==================================')
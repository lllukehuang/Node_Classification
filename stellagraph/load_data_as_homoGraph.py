from pandas.core.frame import DataFrame
from stellargraph import StellarDiGraph, StellarGraph
import pandas as pd
import numpy as np


def find_author(df: DataFrame, id: str):
    df1 = df.copy()
    search_paper = df1[df1.paper_id==id]
    author_list = search_paper['author_id'].tolist()

    return author_list

def find_co_relation(df: DataFrame):
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

def find_ref_relation(dfPA: DataFrame, dfPR: DataFrame):
    source = []
    target = []
    dfPA1 = dfPA.copy()
    dfPR1 = dfPR.copy()

    for row in dfPR1.itertuples():
        paper = getattr(row, 'paper_id')
        paper_author_list = find_author(dfPA1, paper)
        ref = getattr(row, 'reference_id')
        ref_author_list = find_author(dfPA1, ref)
        search_paper = dfPR1[dfPR1.paper_id==paper]

        if (search_paper.shape[0]==0):
            continue
        else:
            for a1 in paper_author_list:
                for a2 in ref_author_list:
                    source.append(a1)
                    target.append(a2)

            dfPR1 = dfPR1.drop(search_paper.index)
            if (dfPR1.shape[0]==0):
                print("Search finish!")
                return source, target

def find_author_label(dfPA: DataFrame):
    labels = {}
    dfPA_1 = dfPA.copy()
    for row in dfPA_1.itertuples():
        author = getattr(row, 'author_id')
        search_author = dfPA_1[dfPA_1.author_id==author]
        
        if(search_author.shape[0]==0):
            continue
        else:
            label = search_author['label'].tolist()
            labels[author] = label
            dfPA_1 = dfPA_1.drop(search_author.index)
            if (dfPA_1.shape[0]==0):
                print("Search finish!")
                return labels


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


### Edge Construction ###
print("Constructing edges...")
source = []
target = []
# Cooperation #
print("Searching for co-authors...")
author1, author2 = find_co_relation(paper_author_info)
# Citation #
print("Searching for referenced authors...")
author3, author4 = find_ref_relation(paper_author_info, paper_reference_info)

co_edges = pd.DataFrame({"source": author1, "target": author2})
ref_edges = pd.DataFrame({"source": author3, "target": author4})

### Node Construction ###
print("Searching for conferences that authors join...")
labels = find_author_label(paper_author_info)
labels = pd.DataFrame.from_dict(labels)
author_node_info = pd.DataFrame({"author_id":paper_author_info['author_id']}).drop_duplicates().reset_index()
nodes = pd.DataFrame({"label": [0]*author_node_info['author_id'].size},index=author_node_info['author_id'])


### Merge ###
print("Constructing graph...")
square_paper_and_author = StellarDiGraph(
    {"author": nodes},
    {"cooperate": co_edges, "cite": ref_edges}
    )
print('==================================')
print(square_paper_and_author.info())
print('==================================')
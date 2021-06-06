from pandas.core.frame import DataFrame
from stellargraph import StellarGraph
import pandas as pd
import numpy as np


def find_coauthor(df:DataFrame):
    source = []
    target = []
    new_df = df.copy()
    for row in df.itertuples():
        paper = getattr(row, 'paper_id')
        search_paper = new_df[new_df.paper_id==paper]
        if (search_paper.size<=1):
            new_df = new_df.drop(search_paper.index)
        else:
            author_list = search_paper['author_id']
            print(paper)
            print(type(author_list))
            print(author_list)
            break

    return source, target


### Load Raw Data ###
paper_author_info = pd.read_csv("./labeled_papers_with_authors.csv")
paper_reference_info = pd.read_csv("./paper_reference.csv")
# Pre-processing
paper_reference_info = paper_reference_info[(paper_reference_info['paper_id']<4844) & (paper_reference_info['reference_id']<4844)].reset_index()

paper_author_info['author_id'] = paper_author_info['author_id'].apply(lambda x:'a' + str(int(x)))
paper_author_info['paper_id'] = paper_author_info['paper_id'].apply(lambda x:'p' + str(int(x)))

paper_reference_info['paper_id'] = paper_reference_info['paper_id'].apply(lambda x:'p' + str(int(x)))
paper_reference_info['reference_id'] = paper_reference_info['reference_id'].apply(lambda x:'p' + str(int(x)))
# print(paper_author_info)
# print(paper_reference_info)

### Edges Construction ###
source = []
target = []

# paper -> paper (one_way)
source = source + paper_reference_info['paper_id'].tolist()
target = target + paper_reference_info['reference_id'].tolist()
# author -> paper (one-way)
source = source + paper_author_info['author_id'].tolist()
target = target + paper_author_info['paper_id'].tolist()
# author <-> author (two-way)
find_coauthor(paper_author_info)

square_edges = pd.DataFrame({"source":source, "target":target})



### Nodes Construction ###
# paper nodes (with labels)
paper_node_info = pd.DataFrame({"paper_id":paper_author_info['paper_id'], "label":paper_author_info['label']}).drop_duplicates().reset_index()
square_paper = pd.DataFrame({"conference":paper_node_info['label']}, index=paper_node_info['paper_id'])

# author nodes (no labels)
square_author = pd.DataFrame(index=paper_author_info['author_id'])

# Merge
#square_paper_and_author = StellarGraph({"paper":square_paper, "author":square_author}, square_edges)
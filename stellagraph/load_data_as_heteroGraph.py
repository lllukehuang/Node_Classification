from stellargraph import StellarGraph
import pandas as pd
import numpy as np


### Load Raw Data ###
paper_author_info = pd.read_csv("./labeled_papers_with_authors.csv")
paper_reference_info = pd.read_csv("./paper_reference.csv")
# Pre-processing
paper_reference_info = paper_reference_info[(paper_reference_info['paper_id']<4844) & (paper_reference_info['reference_id']<4844)].reset_index()

paper_author_info['author_id'] = paper_author_info['author_id'].apply(lambda x:'a' + str(int(x)))
paper_author_info['paper_id'] = paper_author_info['paper_id'].apply(lambda x:'p' + str(int(x)))

paper_reference_info['paper_id'] = paper_reference_info['paper_id'].apply(lambda x:'p' + str(int(x)))
paper_reference_info['reference_id'] = paper_reference_info['reference_id'].apply(lambda x:'p' + str(int(x)))
print(paper_author_info)
print(paper_reference_info)

### Edges Construction ###
source = []
target = []

# paper-paper (one_way)
source = source + paper_reference_info['paper_id'].tolist()
target = target + paper_reference_info['reference_id'].tolist()
# author-paper (one-way)

# author-author (two-way)

square_edges = pd.DataFrame({"source":source, "target":target})



### Nodes Construction ###
# paper nodes (with labels)
paper_node_info = pd.DataFrame({"paper_id":paper_author_info['paper_id'], "label":paper_author_info['label']}).drop_duplicates().reset_index()
square_paper = pd.DataFrame({"conference":paper_node_info['label']}, index=paper_node_info['paper_id'])

# author nodes (no labels)
square_author = pd.DataFrame(index=paper_author_info['author_id'])

# Merge
#square_paper_and_author = StellarGraph({"paper":square_paper, "author":square_author}, square_edges)
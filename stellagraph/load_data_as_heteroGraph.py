from stellargraph import StellarGraph
import pandas as pd


### Load original data ###
node_info = pd.read_csv("origin_data/labeled_papers_with_authors.csv")
edge_info = pd.read_csv("origin_data/paper_reference.csv")
edge_info = edge_info[(edge_info['paper_id']<4844) & (edge_info['reference_id']<4844)]


### Edges Construction ###
source = []
target = []

# paper-paper (one_way)
source += edge_info['paper_id']
target += edge_info['reference_id']
# author-paper (one-way)

# author-author (two-way)

square_edges = pd.DataFrame({"source":source, "target":target})



### Nodes Construction ###
# paper nodes (with labels)
paper_node_info = pd.DataFrame({"paper_id":node_info['paper_id'], "label":node_info['label']}).drop_duplicates().reset_index()
square_paper = pd.DataFrame({"conference":paper_node_info['label']}, index=paper_node_info['paper_id'])

# author nodes (no labels)
square_author = pd.DataFrame(index=node_info['author_id'])

# Merge
#square_paper_and_author = StellarGraph({"paper":square_paper, "author":square_author}, square_edges)
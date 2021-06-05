from stellargraph import StellarGraph
import pandas as pd

### Load original data ###
node_info = pd.read_csv("origin_data/labeled_papers_with_authors.csv")
edge_info = pd.read_csv("origin_data/paper_reference.csv")

### Nodes Construction ###
# paper nodes (no feature)
# author nodes (with labels)

### Edges Construction ###
# author-paper (one-way)
# author-author (two-way)

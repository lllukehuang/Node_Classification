import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score

import os
import networkx as nx
import numpy as np
import pandas as pd

from stellargraph.data import BiasedRandomWalk
from stellargraph import StellarGraph, StellarDiGraph
from stellargraph import datasets
from IPython.display import display, HTML

# add dataset
input_path = "../features/author_paper_year.csv"
author_paper = pd.read_csv(input_path)
author_to_paper_edge = author_paper[["author_id","paper_id"]]
author_to_paper_edge = author_to_paper_edge.rename(columns={'author_id':'source','paper_id':'target'})
input_path1 = "features/paper_paper.csv"
references = pd.read_csv(input_path1)
references = references.rename(columns={'paper_id':'source','reference_id':'target'})
author_to_paper_edge = pd.concat([author_to_paper_edge,references],ignore_index=True)
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
square_author_and_paper = StellarDiGraph({"author": author_nodes, "paper": paper_nodes}, edges=author_to_paper_edge)
print(square_author_and_paper.info())

# random walk
rw = BiasedRandomWalk(square_author_and_paper)

walks = rw.run(
    nodes=list(square_author_and_paper.nodes()),  # root nodes
    length=100,  # maximum length of a random walk
    n=10,  # number of random walks per root node
    p=0.5,  # Defines (unormalised) probability, 1/p, of returning to source node
    q=2.0,  # Defines (unormalised) probability, 1/q, for moving away from source node
)
print("Number of random walks: {}".format(len(walks)))

from gensim.models import Word2Vec

str_walks = [[str(n) for n in walk] for walk in walks]
model = Word2Vec(str_walks, size=128, window=5, min_count=0, sg=1, workers=2, iter=1)


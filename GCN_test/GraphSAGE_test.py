import networkx as nx
import pandas as pd
import os
import itertools

import stellargraph as sg
from stellargraph.mapper import GraphSAGENodeGenerator
from stellargraph.layer import GraphSAGE

from tensorflow.keras import layers, optimizers, losses, metrics, Model
import tensorflow as tf

import numpy as np

from sklearn import preprocessing, feature_extraction, model_selection
from sklearn.calibration import calibration_curve
from sklearn.linear_model import LogisticRegressionCV
from sklearn.isotonic import IsotonicRegression

from sklearn.metrics import accuracy_score

from stellargraph.calibration import TemperatureCalibration, IsotonicCalibration
from stellargraph.calibration import plot_reliability_diagram, expected_calibration_error

from stellargraph import datasets,StellarDiGraph
from IPython.display import display, HTML
# %matplotlib inline

# Given a GraphSAGE model, a node generator, and the number of predictions per point
# this method makes n_predictions number of predictions and then returns the average
# prediction for each query node.
def predict(model, node_generator, n_predictions=1):
    preds_ar = np.array([model.predict(node_generator) for _ in range(n_predictions)])
    print(preds_ar.shape)
    return np.mean(preds_ar, axis=0)

epochs = 20  # number of training epochs for GraphSAGE model
n_predictions = 5  # number of predictions per query node

## 加载数据集
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
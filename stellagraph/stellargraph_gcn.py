import pandas as pd
from sklearn import model_selection
import stellargraph as sg
import tensorflow as tf
from . import load_data_as_heteroGraph


### 
# Data preparation 
###
# def load_my_data():
#     # your own code to load data into Pandas DataFrames, e.g. from CSV files or a database
#     ...

# nodes, edges, targets = load_my_data()


# Use scikit-learn to compute training and test sets
train_targets, test_targets = model_selection.train_test_split(targets, train_size=0.5)

###
# Graph machine learning model 
###
# convert the raw data into StellarGraph's graph format for faster operations
# graph = sg.StellarGraph(nodes, edges)
graph = load_data_as_heteroGraph.constructHeteroGraph()

generator = sg.mapper.FullBatchNodeGenerator(graph, method="gcn")

# two layers of GCN, each with hidden dimension 16
gcn = sg.layer.GCN(layer_sizes=[16, 16], generator=generator)
x_inp, x_out = gcn.in_out_tensors() # create the input and output TensorFlow tensors

# use TensorFlow Keras to add a layer to compute the (one-hot) predictions
predictions = tf.keras.layers.Dense(units=len(ground_truth_targets.columns), activation="softmax")(x_out)

# use the input and output tensors to create a TensorFlow Keras model
model = tf.keras.Model(inputs=x_inp, outputs=predictions)


###
# Training and evaluation
###
# prepare the model for training with the Adam optimiser and an appropriate loss function
model.compile("adam", loss="categorical_crossentropy", metrics=["accuracy"])

# train the model on the train set
model.fit(generator.flow(train_targets.index, train_targets), epochs=5)

# check model generalisation on the test set
(loss, accuracy) = model.evaluate(generator.flow(test_targets.index, test_targets))
print(f"Test set: loss = {loss}, accuracy = {accuracy}")
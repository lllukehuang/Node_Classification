# EE226 Project1: Node Classification

Kaggle's competition page: [Node Classification](https://www.kaggle.com/c/EE226-2021spring-problem1)

## Our method

Using metapath2vec to get the node's feature, and build a linear classifier for feature classification.

We also tried some model integration method to get a more accurate result.

## Experiment Environment

- Ubuntu 16.04
- NVIDIA GTX1080TI

## How to reproduce our work

1. Generate the metapath. You can change corresponding metapath categories in [generate_metapath.py](./generate_metapath.py)

2. Run metapath2vec code(from the origin paper [metapath2vec](https://dl.acm.org/doi/abs/10.1145/3097983.3098036)). See more detail in [here](./code_metapath2vec/readme.txt).

3. Change the format of node features with using [total_feature_change_format.py](./total_feature_change_format.py)

4. Train your model at [train.py](./train.py).

5. Get the result from [generate_test_data.py](generate_test_data.py).

6. If you want to use model integration, see [generate_pred_papers.py](generate_pred_papers.py), [model_intergration.py](model_intergration.py) and [generate_test_data_by_txt.py](generate_test_data_by_txt.py).
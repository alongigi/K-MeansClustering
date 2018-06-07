import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm

import pandas as pd
import numpy as np


class KMeansClass:
    def __init__(self, df):
        self.df = df

    def doKMeans(self):
        x = pd.DataFrame(self.df.data)
        x.columns = list(self.df.columns.values)

        model = KMeans(n_clusters=3)
        model.fit(x)

        print(model.labels_)

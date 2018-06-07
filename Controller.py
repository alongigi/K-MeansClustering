import pandas as pd
import numpy as np
import matplotlib as plt
from scipy.stats import mode

from sklearn.cluster import KMeans

class Controller():
    def __init__(self):
        pass

    def KMean(self, n_clusters, n_init):
        kmeans = KMeans(n_clusters, n_init)
        print ("clustering is done")

    def set_path(self, path):
        self.df = pd.read_excel(path)

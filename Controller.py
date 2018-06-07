import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode
import PreProcessing
import KMeansClass


from sklearn.cluster import KMeans

class Controller():
    def __init__(self):
        pass

    def KMean(self, n_clusters, n_init):
        km = KMeans(n_clusters=int(n_clusters), n_init=int(n_init))
        km.fit(self.df)
        self.x = km.fit_predict(self.df)
        for i in range(0,len(self.x)):
            print("{} : {}".format(self.df['country'][i],self.x[i]))

        df1 = self.df[['Generosity']]
        df2 = self.df[['Social support']]
        plt.scatter(df1, df2, c=self.x, label="skiscat")
        plt.xlabel('Generosity')
        plt.ylabel('Social support')
        plt.title('title')
        plt.legend()
        plt.show()

    def set_path(self, path):
        self.df = pd.read_excel(path)

    def pre_proess(self):
        self.df = PreProcessing.fillMissingValuesWithMean(self.df)
        self.df = PreProcessing.normalize(self.df)
        self.df = PreProcessing.kibuzData(self.df)
        print(self.df)

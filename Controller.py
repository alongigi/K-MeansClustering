import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode
import PreProcessing


from sklearn.cluster import KMeans

class Controller():
    def __init__(self):
        pass

    def KMean(self, n_clusters, n_init):
        km = KMeans(n_clusters=int(n_clusters), n_init=int(n_init))
        km.fit(self.df)
        self.x = km.fit_predict(self.df)
        for i in range(0,len(self.x)):
            print("{} : {}".format(self.df.index[i],self.x[i]))

        df1 = self.df[['Social support']]
        df2 = self.df[['Generosity']]
        t = plt.scatter(df1, df2, c=self.x)
        plt.colorbar(t)
        plt.xlabel('Social support')
        plt.ylabel('Generosity')
        plt.title('Generosity depending on social support')
        plt.legend()
        plt.show()

    def set_path(self, path):
        self.df = pd.read_excel(path)

    def pre_process(self):
        del self.df['year']
        self.df = PreProcessing.fillMissingValuesWithMean(self.df)
        self.df = PreProcessing.normalize(self.df)
        self.df = PreProcessing.kibuz_data(self.df)
        print(self.df)

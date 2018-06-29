import pandas as pd

import Cluster
import PreProcessing

class Controller():

    def algorithm(self, n_clusters, n_init):
        Cluster.KMean(self.df, n_clusters, n_init)
        Cluster.save_result(self.df, self.path)

    def set_path(self, path):
        self.path = path
        self.df = pd.read_excel(self.path)

    def pre_process(self):
        del self.df['year']
        self.df = PreProcessing.fillMissingValuesWithMean(self.df)
        self.df = PreProcessing.normalize(self.df)
        self.df = PreProcessing.kibuz_data(self.df)
        print(self.df)

    def check_clusters(self):
        t = len(self.df.index)
        return len(self.df.index)

    def showinfo(self):
        return len(self.df.index)

    def get_size(self):
        return len(self.df)


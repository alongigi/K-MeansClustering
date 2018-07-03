import pandas as pd

import Cluster
import PreProcessing

"""
Responsible for sending the commands which were recieved from the user.
"""


class Controller():
    """
    Responsible for the Kmeans idea as taught in class.
    :Param {n_clusters} The number of clusters
    :Param {n_init} Num of runs.
    """
    def algorithm(self, n_clusters, n_init):
        Cluster.KMean(self.df, n_clusters, n_init)
        Cluster.save_result(self.df, self.path)

    """
     Responsible for setting the path of the folder that will consist the results of the program.
     :Param {path} The path of the folder that will consist the results of the program.
     """
    def set_path(self, path):
        self.path = path
        self.df = pd.read_excel(self.path)

    """
    Responsible for doing the pre process of the data.
    First filling missing values with its mean with the fillMissingValuesWithMean function
    Secondly normalizing the data with normalize function
    Third making "kibuz data" with kibuz_data function

    At every spet the data frame is updated (df - data frame)
    """
    def pre_process(self):
        del self.df['year']
        self.df = PreProcessing.fillMissingValuesWithMean(self.df)
        self.df = PreProcessing.normalize(self.df)
        self.df = PreProcessing.kibuz_data(self.df)
        print

    """
    Responsible for returning the size of the data drame (df)
    """
    def get_size(self):
        return len(self.df)

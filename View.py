import pickle
# from tkinter import filedialog
import os

import tkFileDialog
from Tkinter import Tk, Entry, Checkbutton, Button, HORIZONTAL, Label, StringVar, Toplevel, Scrollbar, VERTICAL, E, W


class View():
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("K-Means Clustering By: Anatoly and Alon")
        self.file_entry = Entry(self.root)
        self.file_entry['width'] = 50
        self.nums_of_runs_entry = Entry(self.root)
        self.nums_of_runs_entry['width'] = 10
        self.num_of_clusters_entry = Entry(self.root)
        self.num_of_clusters_entry['width'] = 10
        self.preprocess_btn = Button(text="Pre-process", fg="blue", command=self.pre_process)
        self.cluster_btn = Button(text="Cluster", fg="red", command=self.cluster)
        self.create_view()

    def start(self):
        '''
        start the user interface
        '''
        self.root.mainloop()

    def create_view(self):
        '''
        create the view window
        '''
        theme_label = Label(self.root, text="K-Means Clustering", bg="blue", fg="white")
        theme_label.grid(row=0, column=1)
        doc_label = Label(self.root, text="Data File:")
        file_btn = Button(self.root, text="Browse", command=self.data_browse_location)
        cluster_label = Label(self.root, text="Num of clusters k")
        runs_label = Label(self.root, text="Num of runs")

        doc_label.grid(row=1, sticky=E)
        cluster_label.grid(row=2, sticky=E)
        runs_label.grid(row=3, sticky=E)
        self.file_entry.grid(row=1, column=1)
        self.nums_of_runs_entry.grid(row=3, column=1)
        self.num_of_clusters_entry.grid(row=2, column=1)
        file_btn.grid(row=1, column=2)
        self.preprocess_btn.grid(row=5, column=1)
        self.cluster_btn.grid(row=6, column=1)

    def data_browse_location(self):
        '''
        ask the carpus and stopwords directory path
        '''
        file_path = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        self.controller.set_path(file_path)
        self.file_entry.delete(0, len(self.file_entry.get()))
        self.file_entry.insert(0, file_path)

    def pre_process(self):
        self.controller.pre_process()

    def cluster(self):
        self.controller.algorithm(self.num_of_clusters_entry.get(), self.nums_of_runs_entry.get())

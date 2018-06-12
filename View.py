import pickle
# from tkinter import filedialog
import os
import tkMessageBox
from PIL import Image

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


import tkFileDialog
from Tkinter import Tk, Entry, Checkbutton, Button, HORIZONTAL, Label, StringVar, Toplevel, Scrollbar, VERTICAL, E, W, \
    Image

from PIL import ImageTk


class View():
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("K Means Clustering")
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
        try:
            file_path = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
            self.controller.set_path(file_path)
            self.file_entry.delete(0, len(self.file_entry.get()))
            self.file_entry.insert(0, file_path)
        except:
            msg = """
            You have to enter excel file.
            """
            self.pop_alert(msg)

    def pre_process(self):
        self.controller.pre_process()
        msg = """
        Preprocessing completed successfully!"
        """
        self.pop_alert(msg)

    def cluster(self):
        try:
            self.controller.algorithm(self.num_of_clusters_entry.get(), self.nums_of_runs_entry.get())
            img = mpimg.imread('KMeansWorldMap.png')
            plt.imshow(img)
            plt.show()
            img = mpimg.imread('Clustering.png')
            plt.imshow(img)
            plt.show()
            world_map = Image.open('KMeansWorldMap.png')
            view_map = ImageTk.PhotoImage(world_map)
            if tkMessageBox.showinfo("K Means Clustering", "The classification processing completed successfully!"):
                self.root.destroy()
        except:
            msg = """
            Please enter only numbers in the 1-300.
            """
            self.pop_alert(msg)


    def pop_alert(self, msg):
        '''
        display alert for upload file
        '''
        tkMessageBox.showinfo(message=msg)
        pass

import tkFileDialog
import tkMessageBox
from Tkinter import *

from PIL import Image
from PIL import ImageTk

"""
The view is responsible for getting the user's input and showing him the results.
"""

"""
Responsible for popping up a message
"""


def pop_alert(msg):
    tkMessageBox.showinfo("K Means Clustering", message=msg)
    pass


class View():
    """"""
    """
    Responsible of initializing the view.
    initializing the root by initializing instance of TK.
    initializing the root title as "K Means clustering"
    initializing the entry with ENTRY object with the root
    initializing the width of the gui for 50
    initializing number of runs entry with the ENTRY object with root
    initializing number of runs entry width with value of 10
    initializing the number of clusters entry with Entry object with the root
    initializing a button for the pre processing
    initializing the clustering button.
    initializing the map image
    initializing the map image label.
    initializing the scattered image label
    initializing the scattered image label grid
    Calling for the view function

    Param {controller} the controller
    """

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
        self.cluster_btn = Button(text="Cluster", fg="red", command=self.check_input)
        self.map_img_lbl = Label(self.root)
        self.map_img_lbl.grid(row=6, column=1)
        self.scatter_img_lbl = Label(self.root)
        self.scatter_img_lbl.grid(row=6, column=2)
        self.create_view()

    """
    start the user interface by running the main loop function.
    """

    def start(self):
        self.root.mainloop()

    '''
    create the view window
    initializing the label of data file with the root
    initializing the button of browse
    initializing the label of number of clusters
    putting the doc label in grid
    putting the cluster label in grid
    putting the run label in grid
    putting the file entry in grid
    putting the number of runs entry in grid
    putting the number of clusters entry in grid
    initializing the file button
    putting the processing button in grid
    Disabling the cluster button in the code
    putting the clustering button in the grid.
    disabling the cluster button
    '''

    def create_view(self):

        doc_label = Label(self.root, text="Data File:")
        file_btn = Button(self.root, text="Browse", command=self.data_browse_location)
        cluster_label = Label(self.root, text="Num of clusters k")
        runs_label = Label(self.root, text="Num of runs")
        doc_label.grid(row=0, sticky=E)
        cluster_label.grid(row=1, sticky=E)
        runs_label.grid(row=2, sticky=E)
        self.file_entry.grid(row=0, column=1)
        self.nums_of_runs_entry.grid(row=2, column=1)
        self.num_of_clusters_entry.grid(row=1, column=1)
        file_btn.grid(row=0, column=2)
        self.preprocess_btn.grid(row=4, column=1)
        self.preprocess_btn['state'] = 'disabled'
        self.cluster_btn.grid(row=5, column=1)
        self.cluster_btn['state'] = 'disabled'

    """
    Responsible for getting the location of the excel file
    Asking from the user the location of the excel file
    if the user inserts something different than excel pop alert pops with the message "Insert a valid Excel file"
    else inserting to the program the path to the excel file amd switching the process button state to clickable
    """

    def data_browse_location(self):
        try:
            self.file_path = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                          filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
            self.controller.set_path(self.file_path)
            self.file_entry.delete(0, len(self.file_entry.get()))
            self.file_entry.insert(0, self.file_path)
            self.preprocess_btn['state'] = 'normal'
        except:
            pop_alert("Insert a valid Excel file")

    """
    Responsible for the pre processes of the program
    1. asks from the controller to run its method of pre process ('pre_process function')
    2. disabling the process button
    3. enabling the cluster button
    4. finally popping up a message with the content - 'Preprocessing completed successfully'
    """

    def pre_process(self):
        try:
            self.controller.pre_process()
            self.preprocess_btn['state'] = 'disabled'
            self.cluster_btn['state'] = 'normal'
            pop_alert("Pre-processing completed successfully!")
        except:
            pop_alert("Insert a valid Excel file, the current is not valid")


    """
    Responsible for the clustering
    1. running the clustering algorithm in the controller with the number of clusers and runs arguments
    2. Creating an image 'HoroplethMap.png'
    3. putting the image in the smap image label
    4. Creating an image 'Scatter.png'
    5. putting the image in the scatter image label
    6. showing a message - 'K Means Clustering", "The classification processing completed successfully!'
    7. if failing the load the message than exiting the program.

    Params - {clusters} The number of clusters
    Params - {runs} The number of runs
    """

    def cluster(self, clusters, runs):
        self.controller.algorithm(clusters, runs)
        map_img = ImageTk.PhotoImage(Image.open(self.file_path + "HoroplethMap.png"))
        self.map_img_lbl['image'] = map_img
        scatter_img = ImageTk.PhotoImage(Image.open(self.file_path + "Scatter.png"))
        self.scatter_img_lbl['image'] = scatter_img
        if tkMessageBox.showinfo("K Means Clustering", "The classification processing completed successfully!"):
            self.root.destroy()

    """
    Responsible for checking the input
    parsing the number of runs and clusters to int
    checking if the number of clusters is between 0 to the number of rows of the data frame
    Checking if the number of runs is between 1 to 300
    if all the checks are ok then run the cluster with the number of runs and clustering.
    """

    def check_input(self):
        try:
            runs = int(self.nums_of_runs_entry.get())
            clusters = int(self.num_of_clusters_entry.get())
            if clusters < 1 or clusters > self.controller.get_size():
                pop_alert("Clusters should be between 1 and number of records!")
            elif runs > 300 or runs < 1:
                pop_alert("Runs should be between 1 and 300!")
            else:
                self.cluster(clusters, runs)
        except:
            pop_alert("The input should be an integer!")

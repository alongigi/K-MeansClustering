
import tkMessageBox
from PIL import Image



import tkFileDialog
from Tkinter import *

from PIL import Image, ImageTk


class View():
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.geometry("1250x750")
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
        self.map_img_lbl.grid(row=7, column=1)
        self.scatter_img_lbl = Label(self.root)
        self.scatter_img_lbl.grid(row=7, column=2)
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
        self.preprocess_btn['state'] = 'disabled'
        self.cluster_btn.grid(row=6, column=1)
        self.cluster_btn['state'] = 'disabled'

    def data_browse_location(self):
        try:
            self.file_path = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
            self.controller.set_path(self.file_path)
            self.file_entry.delete(0, len(self.file_entry.get()))
            self.file_entry.insert(0, self.file_path)
            self.preprocess_btn['state'] = 'normal'
        except:
            msg = """
            You have to enter excel file.
            """
            self.pop_alert(msg)

    def pre_process(self):
        self.controller.pre_process()
        self.preprocess_btn['state'] = 'disabled'
        self.cluster_btn['state'] = 'normal'
        msg = """
        Preprocessing completed successfully!"
        """
        self.pop_alert(msg)

    def cluster(self, clusters, runs):
        self.controller.algorithm(clusters, runs)
        map_img = ImageTk.PhotoImage(Image.open(self.file_path + "KMeansWorldMap.png"))
        self.map_img_lbl['image'] = map_img
        scatter_img = ImageTk.PhotoImage(Image.open(self.file_path + "Clustering.png"))
        self.scatter_img_lbl['image'] = scatter_img
        #img = mpimg.imread(self.file_path + 'Clustering.png')
        #plt.imshow(img)
        #plt.show()
        #img = mpimg.imread(self.file_path + 'KMeansWorldMap.png')
        #plt.imshow(img)
        #plt.show()
        if tkMessageBox.showinfo("K Means Clustering", "The classification processing completed successfully!"):
            self.root.destroy()

    def check_input(self):
        try:
            runs = int(self.nums_of_runs_entry.get())
            clusters = int(self.num_of_clusters_entry.get())
            if runs > 300 or runs < 1:
                msg = """
                        Runs can be between 1 to 300!"
                        """
                self.pop_alert(msg)
            elif clusters < 1 or clusters > self.controller.get_size():
                msg = """
                        Clusters can be between 1 to number of records!"
                        """
                self.pop_alert(msg)
            else:
                self.cluster(clusters, runs)
        except:
            msg = """
                    Input can be only integer!"
                    """
            self.pop_alert(msg)


    def pop_alert(self, msg):
        '''
        display alert for upload file
        '''
        tkMessageBox.showinfo("K Means Clustering", message=msg)
        pass

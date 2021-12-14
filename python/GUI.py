from tkinter import Tk, Frame, Label, StringVar, Entry, Button, messagebox
import ActionManager as aM
from Task import Task


class GUI:
    """This class runs and manages the GUI"""

    def __init__(self):

        self.root = Tk()
        self.root.title('CW2 - Caoilinn Hughes')
        # self.root.geometry('950x400')

        self.topFrame = Frame(self.root)
        self.topFrame.pack()

        self.bottomFrame = Frame(self.root)
        self.bottomFrame.pack()

        # GUI Entries - File Name, User ID, Document ID (task id doesn't need to be passed through as it is selected using the GUI)
        self.file_label = Label(self.topFrame, text="File:")
        self.file_id = StringVar()
        self.file_id_entry = Entry(
            self.topFrame, width=10, textvariable=self.file_id)

        self.uid_label = Label(self.topFrame, text="User ID:")
        self.user_id = StringVar()
        self.user_id_entry = Entry(
            self.topFrame, width=10, textvariable=self.user_id)

        self.document_label = Label(self.topFrame, text="Document ID")
        self.document_id = StringVar()
        self.document_id_entry = Entry(
            self.topFrame, width=10, textvariable=self.document_id)

        # GUI Button Elements
        self.country_button = Button(
            self.bottomFrame, text="Country Views", command=self.country_views)
        self.continent_button = Button(
            self.bottomFrame, text="Continent Views", command=self.continent_views)
        self.browser_verbose_button = Button(
            self.bottomFrame, text="Browser Views (verbose)", command=self.browser_views_verbose)
        self.browser_name_button = Button(
            self.bottomFrame, text="Browser Views (name)", command=self.browser_views_name)
        self.reader_profiles_button = Button(
            self.bottomFrame, text="Reader Profiles", command=self.reader_profiles)
        self.also_likes_button = Button(
            self.bottomFrame, text="Also Likes", command=self.also_likes)
        self.exitButton = Button(
            self.bottomFrame, text="Quit", command=self.root.quit)

        self.topFrame.grid_rowconfigure(1, weight=1)
        self.topFrame.grid_columnconfigure(1, weight=1)
        self.topFrame.grid_rowconfigure(2, weight=1)
        self.topFrame.grid_columnconfigure(2, weight=1)
        self.topFrame.grid_rowconfigure(3, weight=1)
        self.topFrame.grid_columnconfigure(3, weight=1)
        self.topFrame.grid_rowconfigure(4, weight=1)
        self.topFrame.grid_columnconfigure(4, weight=1)
        self.topFrame.grid_rowconfigure(4, weight=1)
        self.topFrame.grid_columnconfigure(4, weight=1)
        self.topFrame.grid_rowconfigure(5, weight=1)
        self.topFrame.grid_columnconfigure(5, weight=1)
        self.topFrame.grid_rowconfigure(6, weight=1)
        self.topFrame.grid_columnconfigure(6, weight=1)

        self.file_label.grid(column=1, row=1)
        self.file_id_entry.grid(column=2, row=1)

        self.uid_label.grid(column=3, row=1)
        self.user_id_entry.grid(column=4, row=1)

        self.document_label.grid(column=5, row=1)
        self.document_id_entry.grid(column=6, row=1)

        # Position buttons on GUI

        self.bottomFrame.grid_rowconfigure(1, weight=1)
        self.bottomFrame.grid_rowconfigure(2, weight=1)

        self.bottomFrame.grid_columnconfigure(1, weight=1)
        self.bottomFrame.grid_columnconfigure(2, weight=1)
        self.bottomFrame.grid_columnconfigure(3, weight=1)

        self.country_button.grid(column=1, row=1)
        self.continent_button.grid(column=2, row=1)
        self.browser_verbose_button.grid(column=3, row=1)
        self.browser_name_button.grid(column=1, row=2)
        self.reader_profiles_button.grid(column=2, row=2)
        self.also_likes_button.grid(column=3, row=2)
        self.exitButton.grid(column=2, row=3, pady=50)

        self.root.mainloop()

    def country_views(self):
        task_id = Task.country
        file_id = self.file_id.get()
        user_id = self.user_id.get()
        doc_id = self.document_id.get()

        if file_id == "":
            messagebox.showwarning(
                title="No File", message="Cannot perform this function without a file")
        elif doc_id == "":
            messagebox.showwarning(
                title="No Document ID", message="Cannot perform this function without a document id")
        else:
            aM.ActionManager(file_id, user_id,
                             doc_id, task_id)
            self.clear_entries()

    def continent_views(self):
        task_id = Task.continent

        file_id = self.file_id.get()
        user_id = self.user_id.get()
        doc_id = self.document_id.get()

        if file_id == "":
            messagebox.showwarning(
                title="No File", message="Cannot perform this function without a file")
        elif doc_id == "":
            messagebox.showwarning(
                title="No Document ID", message="Cannot perform this function without a document id")
        else:
            aM.ActionManager(file_id, user_id,
                             doc_id, task_id)
            self.clear_entries()

    def browser_views_verbose(self):
        task_id = Task.browser_verbose

        file_id = self.file_id.get()
        user_id = self.user_id.get()
        doc_id = self.document_id.get()

        if file_id == "":
            messagebox.showwarning(
                title="No File", message="Cannot perform this function without a file")
        else:
            aM.ActionManager(file_id, user_id,
                             doc_id, task_id)
            self.clear_entries()

    def browser_views_name(self):

        task_id = Task.browser_name

        file_id = self.file_id.get()
        user_id = self.user_id.get()
        doc_id = self.document_id.get()

        if file_id == "":
            messagebox.showwarning(
                title="No File", message="Cannot perform this function without a file")
        else:
            aM.ActionManager(file_id, user_id,
                             doc_id, task_id)
            self.clear_entries()

    def reader_profiles(self):
        task_id = Task.reader

        file_id = self.file_id.get()
        user_id = self.user_id.get()
        doc_id = self.document_id.get()

        if file_id == "":
            messagebox.showwarning(
                title="No File", message="Cannot perform this function without a file")
        else:
            aM.ActionManager(file_id, user_id,
                             doc_id, task_id)
            self.clear_entries()

    def also_likes(self):
        task_id = Task.also_likes

        file_id = self.file_id.get()
        user_id = self.user_id.get()
        doc_id = self.document_id.get()

        aM.ActionManager(file_id, user_id,
                         doc_id, task_id)
        self.clear_entries()

    def clear_entries(self):
        """Clears every field in the GUI so the user can perform another action"""
        # https://stackoverflow.com/questions/34667710/pattern-matching-tkinter-child-widgets-winfo-children-to-determine-type
        for items in self.topFrame.winfo_children():
            if isinstance(items, Entry):
                items.delete(0, "end")

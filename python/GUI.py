from tkinter import *
import ActionManager as am


class GUI:
    def __init__(self):

        self.root = Tk()
        self.root.title('CW2 - Caoilinn Hughes')
        self.root.geometry('1200x600')

        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()

        self.country_button = Button(
            self.mainFrame, text="Country Views", command=self.country_views)
        self.continent_button = Button(
            self.mainFrame, text="Continent Views", command=self.continent_views)
        self.browser_verbose_button = Button(
            self.mainFrame, text="Browser Views (verbose)", command=self.browser_views_verbose)
        self.browser_name_button = Button(
            self.mainFrame, text="Browser Views (name)", command=self.browser_views_name)
        self.reader_profiles_button = Button(
            self.mainFrame, text="Reader Profiles", command=self.reader_profiles)
        self.also_likes_button = Button(
            self.mainFrame, text="Also Likes", command=self.also_likes)
        self.exitButton = Button(
            self.mainFrame, text="Quit", command=self.root.quit)

        self.country_button.pack(pady=20)
        self.continent_button.pack(pady=20)
        self.browser_verbose_button.pack(pady=20)
        self.browser_name_button.pack(pady=20)
        self.reader_profiles_button.pack(pady=20)
        self.also_likes_button.pack(pady=20)
        self.exitButton.pack(pady=20)

        self.root.mainloop()

    def country_views(self):
        print("Country Views")

        task_id = 1

        am.ActionManager("File 1234", "User ID: 12345",
                         "Document ID: 12345", task_id)

    def continent_views(self):
        print("Continent Views")

        task_id = 2

        am.ActionManager("File 1234", "User ID: 12345",
                         "Document ID: 12345", task_id)

    def browser_views_verbose(self):
        print("Browser Views (verbose)")

        task_id = 3

        am.ActionManager("File 1234", "User ID: 12345",
                         "Document ID: 12345", task_id)

    def browser_views_name(self):
        print("Browser Views (name)")

        task_id = 4

        am.ActionManager("File 1234", "User ID: 12345",
                         "Document ID: 12345", task_id)

    def reader_profiles(self):
        print("Reader Profiles")

        task_id = 5

        am.ActionManager("File 1234", "User ID: 12345",
                         "Document ID: 12345", task_id)

    def also_likes(self):
        print("Also Likes")

        task_id = 6

        am.ActionManager("File 1234", "User ID: 12345",
                         "Document ID: 12345", task_id)

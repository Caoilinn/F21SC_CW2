from tkinter.constants import N
from Task import Task


class ActionManager():
    def __init__(self, file, user_id, document_id, task_id):
        self.file = file
        self.user_id = user_id
        self.document_id = document_id
        self.task_id = task_id

        # Check if file is empyt - no functions can be performed without a file - checks for doc and user will be where they are needed
        if self.file == "":
            print("Failure")
        else:
            self.perfromAction()

    # Use function decoration here

    def perfromAction(self):
        print(self.file)
        if self.task_id == Task.country:
            self.country_views()
        elif self.task_id == Task.continent:
            self.continent_views()
        elif self.task_id == Task.browser_verbose:
            self.browser_views_verbose()
        elif self.task_id == Task.browser_name:
            self.browser_views_name()
        elif self.task_id == Task.reader:
            self.reader_profiles()
        else:
            self.also_likes()

    def country_views(self):
        print("Country Views")

    def continent_views(self):
        print("Continent Views")

    def browser_views_verbose(self):
        print("Browser Views Verbose")

    def browser_views_name(self):
        print("Browser Views Name")

    def reader_profiles(self):
        print("Reader Profiles")

    def also_likes(self):
        print("Also Likes")

from enum import Enum
from GUI import Task
# This class controls what functions get called from the


class ActionManager():
    def __init__(self, file, user_id, document_id, task_id):
        self.file = file
        self.user_id = user_id
        self.document_id = document_id
        self.task_id = task_id

        self.perfromAction()

    # Use function decoration here

    def perfromAction(self):
        print(
            f"Action Manager:\n\tFile:\t{self.file}\n\tUser:\t{self.user_id}\n\tDoc:\t{self.document_id}\n\tTask:\t{self.task_id}")
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
        print()

    def continent_views(self):
        print()

    def browser_views_verbose(self):
        print()

    def browser_views_name(self):
        print()

    def reader_profiles(self):
        print()

    def also_likes(self):
        print()

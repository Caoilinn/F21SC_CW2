from argparse import ArgumentParser
import ActionManager as aM
from Task import Task


# Used https://stackoverflow.com/questions/11604653/how-to-add-command-line-arguments-with-flags-in-python3 for information on argparse

class CLI:
    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument("-u", "--user", help="Visitor UUID")
        self.parser.add_argument("-d", "--doc", help="Document ID")
        self.parser.add_argument("-t", "--task", help="Task ID")
        self.parser.add_argument("-f", "--file", help="File Location")

        self.args = self.parser.parse_args()

        self.document_id = self.args.doc
        self.user_id = self.args.user
        self.file_id = self.args.file
        self.task_id = self.args.task

        # If no file has been passed in as a command line argument then the application will quit
        if self.file_id is None:
            print("Cannot complete any function without a file")
            quit()

        # If the user is trying to run the document fetch tasks without a document id then the application will quit
        if self.task_id == "2a" or self.task_id == "2b" and self.document_id is None:
            print("Cannot complete this task without a document id")
            quit()

        self.set_task_id()
        self.perform_task()

    def perform_task(self):
        """Selects the specific task to be run based on the input task id"""
        aM.ActionManager(self.file_id, self.user_id,
                         self.document_id, self.task_id)

    def set_task_id(self):
        """Sets the input task ID to one of the enum tasks"""
        if self.task_id == "2a":
            self.task_id = Task.country
        elif self.task_id == "2b":
            self.task_id = Task.continent
        elif self.task_id == "3a":
            self.task_id = Task.browser_verbose
        elif self.task_id == "3b":
            self.task_id = Task.browser_name
        elif self.task_id == "4":
            self.task_id = Task.reader
        elif self.task_id == "5d":
            self.task_id = Task.also_likes
        elif self.task_id == "6":
            self.task_id = Task.also_likes_graph

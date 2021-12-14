from Task import Task
from JSONReader import JSONReader
from DataAnalysis import DataAnalysis


# Function declared here so that it can be passed to the also_likes function as the sorting function
def sort_by_readers(docs_weights):
    top_constraint = 10
    return dict(
        sorted(docs_weights.items(), key=lambda x: x[1], reverse=True)[:top_constraint])


class ActionManager:
    def __init__(self, file, user_id, document_id, task_id):
        self.file = file
        self.user_id = user_id
        self.document_id = document_id
        self.task_id = task_id
        self.data_analyser = DataAnalysis()

        self.data = JSONReader().process_file(self.file)

        if self.data is None:
            quit()

        # Perform whatever task is passed through from either the GUI or the command line
        self.perform_action()

    def perform_action(self):
        """Selects which function will be performed based on the task ID that is set"""
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
        """This method calls the analysis functions to create the country view dictionary and generate and show the histogram"""
        self.data_analyser.countries(self.document_id, self.data)
        self.data_analyser.show_histogram(self.data_analyser.num_countries_dict, "Num Viewed", "Views by Country")

        self.data_analyser.clear_dictionaries()

    def continent_views(self):
        """This method calls the analysis functions to create the continent view dictionary and generate and show the histogram"""
        self.data_analyser.continents(self.document_id, self.data)
        self.data_analyser.show_histogram(self.data_analyser.num_continents_dict, "Num Viewed", "Views by Continent")

        self.data_analyser.clear_dictionaries()

    def browser_views_verbose(self):
        """This method calls the analysis functions to create the browser verbose dictionary and generate and show the histogram"""
        self.data_analyser.browsers_verbose(self.data)
        self.data_analyser.show_histogram(self.data_analyser.num_browsers_verbose, "Num Used",
                                          "Views by Browser (verbose)")

        self.data_analyser.clear_dictionaries()

    def browser_views_name(self):
        """This method calls the analysis functions to create the browser name dictionary and generate and show the histogram"""
        self.data_analyser.browsers_name(self.data)
        self.data_analyser.show_histogram(self.data_analyser.num_browsers_name, "Num Used", "Views by Browser (name)")

        self.data_analyser.clear_dictionaries()

    def reader_profiles(self):
        """Prints the top ten readers by time spend reading"""
        self.data_analyser.reader_profiles(self.data)
        # print(self.data_analyser.sorted_readers)

        count = 0
        for key, value in self.data_analyser.sorted_readers.items():
            count += 1
            print(f"{count}:\nVisitor ID: {key}\tTime Spent Reading: {value}")

        self.data_analyser.clear_dictionaries()

    def also_likes(self):
        liked_docs = self.data_analyser.also_likes(self.document_id, self.data, sort_by_readers, self.user_id)
        print(f"Liked Documents (Weighted):\n{liked_docs}")

from Task import Task
from JSONReader import JSONReader
from DataAnalysis import DataAnalysis


class ActionManager:
    def __init__(self, file, user_id, document_id, task_id):
        self.file = file
        self.user_id = user_id
        self.document_id = document_id
        self.task_id = task_id
        self.data_analyser = DataAnalysis()

        self.data = JSONReader().process_file(self.file)
        # Perform whatever task is passed through from either the GUI or the command line
        self.perform_action()

    # Use function decoration here

    def perform_action(self):
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
        """This method calls the analysis functions to create the country view dictionary and generate and show the histogram"""
        self.data_analyser.countries(self.document_id, self.data)
        self.data_analyser.show_histogram(self.data_analyser.num_countries_dict, "Num Viewed", "Views by Country")

        # TODO: Remove later this is debug only
        print("Countries: ", self.data_analyser.num_countries_dict)

    def continent_views(self):
        """This method calls the analysis functions to create the continent view dictionary and generate and show the histogram"""
        self.data_analyser.continents(self.document_id, self.data)
        self.data_analyser.show_histogram(self.data_analyser.num_continents_dict, "Num Viewed", "Views by Continent")

        # TODO: Remove later this is debug only
        print("Continents: ", self.data_analyser.num_continents_dict)

    def browser_views_verbose(self):
        """This method calls the analysis functions to create the browser verbose dictionary and generate and show the histogram"""
        self.data_analyser.browsers_verbose(self.data)
        self.data_analyser.show_histogram(self.data_analyser.num_browsers_verbose, "Num Used", "Views by Browser")
        print(self.data_analyser.num_browsers_verbose)

    def browser_views_name(self):
        """This method calls the analysis functions to create the browser name dictionary and generate and show the histogram"""
        self.data_analyser.browsers_name()

    def reader_profiles(self):
        self.data_analyser.reader_profiles()

    def also_likes(self):
        print("Also Likes")

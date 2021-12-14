import httpagentparser
import matplotlib.pyplot as plt


class DataAnalysis:
    # Dictionaries that hold how many of each country and continent there are in the returned data
    num_countries_dict = {}
    num_continents_dict = {}
    num_browsers_verbose = {}
    num_browsers_name = {}
    reader_profile = {}
    sorted_readers = {}

    # Taken from sample http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/Samples/simple_histo.py
    cntry_to_cont = {
        'AF': 'AS',
        'AX': 'EU',
        'AL': 'EU',
        'DZ': 'AF',
        'AS': 'OC',
        'AD': 'EU',
        'AO': 'AF',
        'AI': 'NA',
        'AQ': 'AN',
        'AG': 'NA',
        'AR': 'SA',
        'AM': 'AS',
        'AW': 'NA',
        'AU': 'OC',
        'AT': 'EU',
        'AZ': 'AS',
        'BS': 'NA',
        'BH': 'AS',
        'BD': 'AS',
        'BB': 'NA',
        'BY': 'EU',
        'BE': 'EU',
        'BZ': 'NA',
        'BJ': 'AF',
        'BM': 'NA',
        'BT': 'AS',
        'BO': 'SA',
        'BQ': 'NA',
        'BA': 'EU',
        'BW': 'AF',
        'BV': 'AN',
        'BR': 'SA',
        'IO': 'AS',
        'VG': 'NA',
        'BN': 'AS',
        'BG': 'EU',
        'BF': 'AF',
        'BI': 'AF',
        'KH': 'AS',
        'CM': 'AF',
        'CA': 'NA',
        'CV': 'AF',
        'KY': 'NA',
        'CF': 'AF',
        'TD': 'AF',
        'CL': 'SA',
        'CN': 'AS',
        'CX': 'AS',
        'CC': 'AS',
        'CO': 'SA',
        'KM': 'AF',
        'CD': 'AF',
        'CG': 'AF',
        'CK': 'OC',
        'CR': 'NA',
        'CI': 'AF',
        'HR': 'EU',
        'CU': 'NA',
        'CW': 'NA',
        'CY': 'AS',
        'CZ': 'EU',
        'DK': 'EU',
        'DJ': 'AF',
        'DM': 'NA',
        'DO': 'NA',
        'EC': 'SA',
        'EG': 'AF',
        'SV': 'NA',
        'GQ': 'AF',
        'ER': 'AF',
        'EE': 'EU',
        'ET': 'AF',
        'FO': 'EU',
        'FK': 'SA',
        'FJ': 'OC',
        'FI': 'EU',
        'FR': 'EU',
        'GF': 'SA',
        'PF': 'OC',
        'TF': 'AN',
        'GA': 'AF',
        'GM': 'AF',
        'GE': 'AS',
        'DE': 'EU',
        'GH': 'AF',
        'GI': 'EU',
        'GR': 'EU',
        'GL': 'NA',
        'GD': 'NA',
        'GP': 'NA',
        'GU': 'OC',
        'GT': 'NA',
        'GG': 'EU',
        'GN': 'AF',
        'GW': 'AF',
        'GY': 'SA',
        'HT': 'NA',
        'HM': 'AN',
        'VA': 'EU',
        'HN': 'NA',
        'HK': 'AS',
        'HU': 'EU',
        'IS': 'EU',
        'IN': 'AS',
        'ID': 'AS',
        'IR': 'AS',
        'IQ': 'AS',
        'IE': 'EU',
        'IM': 'EU',
        'IL': 'AS',
        'IT': 'EU',
        'JM': 'NA',
        'JP': 'AS',
        'JE': 'EU',
        'JO': 'AS',
        'KZ': 'AS',
        'KE': 'AF',
        'KI': 'OC',
        'KP': 'AS',
        'KR': 'AS',
        'KW': 'AS',
        'KG': 'AS',
        'LA': 'AS',
        'LV': 'EU',
        'LB': 'AS',
        'LS': 'AF',
        'LR': 'AF',
        'LY': 'AF',
        'LI': 'EU',
        'LT': 'EU',
        'LU': 'EU',
        'MO': 'AS',
        'MK': 'EU',
        'MG': 'AF',
        'MW': 'AF',
        'MY': 'AS',
        'MV': 'AS',
        'ML': 'AF',
        'MT': 'EU',
        'MH': 'OC',
        'MQ': 'NA',
        'MR': 'AF',
        'MU': 'AF',
        'YT': 'AF',
        'MX': 'NA',
        'FM': 'OC',
        'MD': 'EU',
        'MC': 'EU',
        'MN': 'AS',
        'ME': 'EU',
        'MS': 'NA',
        'MA': 'AF',
        'MZ': 'AF',
        'MM': 'AS',
        'NA': 'AF',
        'NR': 'OC',
        'NP': 'AS',
        'NL': 'EU',
        'NC': 'OC',
        'NZ': 'OC',
        'NI': 'NA',
        'NE': 'AF',
        'NG': 'AF',
        'NU': 'OC',
        'NF': 'OC',
        'MP': 'OC',
        'NO': 'EU',
        'OM': 'AS',
        'PK': 'AS',
        'PW': 'OC',
        'PS': 'AS',
        'PA': 'NA',
        'PG': 'OC',
        'PY': 'SA',
        'PE': 'SA',
        'PH': 'AS',
        'PN': 'OC',
        'PL': 'EU',
        'PT': 'EU',
        'PR': 'NA',
        'QA': 'AS',
        'RE': 'AF',
        'RO': 'EU',
        'RU': 'EU',
        'RW': 'AF',
        'BL': 'NA',
        'SH': 'AF',
        'KN': 'NA',
        'LC': 'NA',
        'MF': 'NA',
        'PM': 'NA',
        'VC': 'NA',
        'WS': 'OC',
        'SM': 'EU',
        'ST': 'AF',
        'SA': 'AS',
        'SN': 'AF',
        'RS': 'EU',
        'SC': 'AF',
        'SL': 'AF',
        'SG': 'AS',
        'SX': 'NA',
        'SK': 'EU',
        'SI': 'EU',
        'SB': 'OC',
        'SO': 'AF',
        'ZA': 'AF',
        'GS': 'AN',
        'SS': 'AF',
        'ES': 'EU',
        'LK': 'AS',
        'SD': 'AF',
        'SR': 'SA',
        'SJ': 'EU',
        'SZ': 'AF',
        'SE': 'EU',
        'CH': 'EU',
        'SY': 'AS',
        'TW': 'AS',
        'TJ': 'AS',
        'TZ': 'AF',
        'TH': 'AS',
        'TL': 'AS',
        'TG': 'AF',
        'TK': 'OC',
        'TO': 'OC',
        'TT': 'NA',
        'TN': 'AF',
        'TR': 'AS',
        'TM': 'AS',
        'TC': 'NA',
        'TV': 'OC',
        'UG': 'AF',
        'UA': 'EU',
        'AE': 'AS',
        'GB': 'EU',
        'US': 'NA',
        'UM': 'OC',
        'VI': 'NA',
        'UY': 'SA',
        'UZ': 'AS',
        'VU': 'OC',
        'VE': 'SA',
        'VN': 'AS',
        'WF': 'OC',
        'EH': 'AF',
        'YE': 'AS',
        'ZM': 'AF',
        'ZW': 'AF'
    }

    def countries(self, doc_id, data):
        """Finds out how many times a given document ID has been read in certain countries"""
        for i in data:
            # Check if the json object is a reader or not
            if i["event_type"] == "read":
                # Check if the record matches the provided document ID
                if i['subject_doc_id'] == doc_id:
                    # Check if the country already exists in the num_countries dictionary
                    if i['visitor_country'] in self.num_countries_dict:
                        # If it does increment the count
                        self.num_countries_dict[i['visitor_country']] += 1
                    else:
                        # If it does not then add it to the dictionary with an initial value of 1
                        self.num_countries_dict[i['visitor_country']] = 1

    def continents(self, doc_id, data):
        """Uses the num_countries_dict to populate the continents' dictionary (determines the continents where given documents are view in) """
        if bool(self.num_countries_dict):
            # Loop through the countries dictionary
            for key in self.num_countries_dict:
                # Check if the country code matches up
                if key in self.cntry_to_cont:
                    # Check if the continent already exists in the num_continent dictionary
                    cont_key = self.cntry_to_cont.get(key)
                    print("The continent is ", cont_key)
                    if self.cntry_to_cont[key] in self.num_continents_dict:
                        self.num_continents_dict[cont_key] += 1
                    else:
                        self.num_continents_dict[cont_key] = 1
        else:
            # If the country dictionary is not populated then populate it and try again
            self.countries(doc_id, data)
            self.continents(doc_id, data)

    def browsers_verbose(self, data):
        """Finds out how many of each browser is used to view files"""
        for i in data:
            # Check if the json object is a reader or not
            if i["event_type"] == "read":
                if i['visitor_useragent'] in self.num_browsers_verbose:
                    self.num_browsers_verbose[i['visitor_useragent']] += 1
                else:
                    self.num_browsers_verbose[i['visitor_useragent']] = 1

    def browsers_name(self, data):
        """Finds out how many of each browser is used to view files - this version shortens the browser name by using the httpagentparser library"""
        if bool(self.num_browsers_verbose):
            for key in self.num_browsers_verbose:
                browser_name = httpagentparser.simple_detect(key)[1]
                if browser_name in self.num_browsers_name:
                    self.num_browsers_name[browser_name] += 1
                else:
                    self.num_browsers_name[browser_name] = 1
        else:
            # If the browser's dictionary is empty then populate it and try again
            self.browsers_verbose(data)
            self.browsers_name(data)

    def reader_profiles(self, data):
        """Finds all the readers in the JSON file and adds up how much time they spent reading documents as a whole,
        adds this to a dictionary and then finds the top 10 readers - i.e. those who have spent the most time reading"""
        for i in data:
            # Check if the json object is a pagereadtime event
            if i["event_type"] == "pagereadtime":
                if i["visitor_uuid"] in self.reader_profile:
                    # Adding to the overall readtime - this is because readers are ranked by the overall amount of time they have spent reading document
                    self.reader_profile[i["visitor_uuid"]] += i["event_readtime"]
                else:
                    self.reader_profile[i["visitor_uuid"]] = i["event_readtime"]
        top_constraint = 10
        self.sorted_readers = dict(
            sorted(self.reader_profile.items(), key=lambda x: x[1], reverse=True)[:top_constraint])

    def also_likes(self, doc_id, data, sort_func, visitor_id=None):
        """This function returns a sorted list of documents that readers of the provided document id have also read
        The sorting is not done within this function, rather a sorting function is passed in which takes care of the sorting"""
        linked_docs = []
        doc_weight = {}

        # Get a list of all who have read a certain document
        readers = self.document_visitors(doc_id, data)

        # Check if the visitor id has been set, and if so add it to the reader list
        if not (visitor_id is None) or not (visitor_id == " "):
            print("added to readers")
            readers.append(visitor_id)
            print(f"Readers:\n{readers}")

        # Find all the documents that readers of the input document have read
        for reader in readers:
            linked_docs.append(self.visitor_documents(reader, data))
            self.clear_dictionaries()

        # For all the lists of documents returned apply a weighting to each doc (how many times it has been read by the other visitors)
        for docs in linked_docs:
            for doc in docs:
                if doc in doc_weight:
                    doc_weight[doc] += 1
                else:
                    doc_weight[doc] = 1

        sorted_docs = sort_func(doc_weight)
        return sorted_docs

    @staticmethod
    def document_visitors(doc_id, data):
        """Given a document id this function returns a list of all the visitors who have read said document"""
        readers = []
        doc_readers = {}
        for i in data:
            if i["event_type"] == "read":
                if i["subject_doc_id"] == doc_id:
                    if i["visitor_uuid"] in doc_readers:
                        pass
                    else:
                        readers.append(i["visitor_uuid"])
                        doc_readers[i["visitor_uuid"]] = i["subject_doc_id"]
        return readers

    @staticmethod
    def visitor_documents(visitor_id, data):
        """Given a visitor id this function returns a list of all documents that visitor has read"""
        docs_read = []
        reader_docs = {}
        for i in data:
            if i["event_type"] == "read":
                if i["visitor_uuid"] == visitor_id:
                    if i["subject_doc_id"] in reader_docs:
                        pass
                    else:
                        docs_read.append(i["subject_doc_id"])
                        reader_docs[i["subject_doc_id"]] = i["visitor_uuid"]
        return docs_read

    @staticmethod
    def show_histogram(data, label, title):
        """Displays a histogram, the data displayed in the histogram is dependent on the data passed into the method"""
        length = len(data)

        plt.barh(range(length), list(data.values()), align='center', alpha=0.4)
        plt.yticks(range(length), list(data.keys()))  # counts.values())
        plt.xlabel(label)
        plt.title(title)
        plt.show()

    def clear_dictionaries(self):
        """The purpose of this function is to clear the dictionaries after each operation,
        if the dictionaries are not cleared then there is the possibility of repeated data if
        the same function is used twice, or data that is not relevant to the search query showing up
        in the search results"""
        self.num_countries_dict.clear()
        self.num_continents_dict.clear()
        self.num_browsers_verbose.clear()
        self.num_browsers_name.clear()
        self.reader_profile.clear()
        self.sorted_readers.clear()

import matplotlib.pyplot as plt


class DataAnalysis:
    # Dictionaries that hold how many of each country and continent there are in the returned data
    num_countries_dict = {}
    num_continents_dict = {}

    # Taken from sample http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/Samples/simple_histo.py
    continents = {
        'AF': 'Africa',
        'AS': 'Asia',
        'EU': 'Europe',
        'NA': 'North America',
        'SA': 'South America',
        'OC': 'Oceania',
        'AN': 'Antarctica'
    }
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
                    # Check if the continent alreay exists in the num_continent dictionary
                    cont_key = self.cntry_to_cont.get(key)
                    print("The continent is ", cont_key)
                    if self.cntry_to_cont[key] in self.num_continents_dict:
                        self.num_continents_dict[cont_key] += 1
                    else:
                        self.num_continents_dict[cont_key] = 1
        else:
            print("There are no countries in the dictionary")

    def browsers_name(self):
        print()

    def browsers_verbose(self):
        print()

    def reader_profiles(self):
        print()

    def also_likes(self):
        print()

    def show_histogram(self, data, label, title):
        """Displays a histogram, the data displayed in the histogram is dependent on the data passed into the method"""
        length = len(data)

        plt.barh(range(length), list(data.values()), align='center', alpha=0.4)
        plt.yticks(range(length), list(data.keys()))  # counts.values())
        plt.xlabel(label)
        plt.title(title)
        plt.show()

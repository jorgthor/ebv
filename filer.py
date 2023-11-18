import json
"""
Deals with the different files used for storage or configuration 
"""


def getVersionJson():
    """
    Returns the different versions
    :return: dict
    """
    version_file = 'versionFile.json'
    with open(version_file) as json_file:
        data = json.load(json_file)
        return data


def writeVersionJson(data):
    """
    Writes the different versions
    :param data: dict
    """
    version_file = 'versionFile.json'
    with open(version_file, 'w') as outfile:
        json.dump(data, outfile)

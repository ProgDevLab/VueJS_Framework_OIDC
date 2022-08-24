"""
E Sphere Framework Install Script
"""

# Generic Libs
from os import path, makedirs
from json import load
from datetime import date

CONFIG_FILE = "install.json"

__author__ = "ProgOwer"
__copyright__ = "Copyright 2022, E Sphere Framework Install Script"
__credits__ = ["ProgOwer"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "ProgOwer"
__email__ = "progower0770@gmail.com"
__status__ = "Production"


def getConfig(path):
    data = None
    with open(path, 'r') as stream:
        data = load(stream)
    return data


def configureGit(git_list):
    if not path.exists("tools"):
        makedirs("tools")

    with open('tools/git.sh', "w") as file:
        file.write("#!/bin/bash\n\n")
        file.write("# Git Repository\n")

        for gitName in git_list:
            gitURL = git_list.get(gitName)
            file.write(f"git remote add {gitName} {gitURL}\n")
            file.write(f"git remote set-url --add --push origin {gitURL}\n\n")

        file.write("# Display Config\n")
        file.write("git remote show origin\n")
        file.write("git config --list\n")


def searchAndReplace(fileList, searchAndReplaceList):
    searchAndReplaceList['start-year'] = str(date.today().year)
    for file in fileList:
        fileData = ""

        with open(file, 'r') as file_raw:
            fileData = file_raw.read()

        for word in searchAndReplaceList:
            fileData = fileData.replace(word, searchAndReplaceList.get(word))

        with open(file, 'w') as file_raw:
            file_raw.write(fileData)


if __name__ == '__main__':
    print("Init Installation Script ...")

    print("Read Config file ...")
    config = getConfig(path=CONFIG_FILE)

    print("Prepare Git Script ...")
    configureGit(git_list=config.get('gitList'))

    print("Search and Replace in each files ...")
    searchAndReplace(
        fileList=config.get('fileList'),
        searchAndReplaceList=config.get('searchAndReplaceList'))

    print("Complete Installation !")
    exit(0)

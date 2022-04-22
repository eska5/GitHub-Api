import requests
import json
import functools
import operator
from collections import Counter

# Class -> Downloads information from GitHub
class DataFromGithub:

    # Authorization token needed to proceed
    header = {'Authorization': 'token %s' % "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"}

    # Get user data form GitHub
    def getUserDataFromGithub(self, user: str):
        userDataRequestUrl = f"https://api.github.com/users/{user}"
        userData = requests.get(userDataRequestUrl, headers = self.header).json()
        return userData

    # Get repositories data form GitHub
    def getRepositoriesDataFromGithub(self, userData: json):
        repositoriesDataRequestUrl = userData['repos_url']
        repositoriesData = requests.get(repositoriesDataRequestUrl, headers = self.header).json()
        return repositoriesData

    # Get languages data form GitHub
    def getLanguagesDataFromGithub(self, repositoriesData: json):
        languagesData = []
        for repositoryData in repositoriesData:
            languagesDataRequest = requests.get(repositoryData['languages_url'], headers = self.header).json()
            languagesData.append(languagesDataRequest)
        return languagesData


# Repositories data converted to JSON format
def repositoriesDataMergeInJSON(repositoriesData: json, languagesData: list):
    combinedData = []
    for index in range(len(languagesData)):
        combinedData.append({
        "name" : repositoriesData[index]['name'],
        "languages" : languagesData[index]
        })
    finalData = {
            "repositories": combinedData
        }
    jsonDump = json.dumps(finalData)
    return json.loads(jsonDump)

# User data Sum amount of bytes for each language
def languagesSum(languagesData: list):
    languageDataList = []
    for index in range(len(languagesData)):
        languageDataList.append(
            languagesData[index]
        )
    # function that changes list to dictionary and sums up their size
    languageDataDictionary = dict(functools.reduce(operator.add,
                                map(Counter, languageDataList)))
    return json.dumps(languageDataDictionary)

# User data converted to JSON format
def userDataMergeInJSON(userData: json, languagesDictionary: str):
    # string to list
    convertedlanguagesDictionary = json.loads(languagesDictionary)
    finalData = {
        "login" : userData['login'],
        "name" : userData['name'],
        "bio" : userData['bio'],
        "languages" : dict(convertedlanguagesDictionary)
    }
    jsonDump = json.dumps(finalData)
    return json.loads(jsonDump)

# User data converted to JSON format without languages <EXCEPTION NO LANGUAGES>
def userDataMergeInJSONException(userData: json):
    finalData = {
        "login" : userData['login'],
        "name" : userData['name'],
        "bio" : userData['bio'],
        "languages" : None
    }
    jsonDump = json.dumps(finalData)
    return json.loads(jsonDump)

# main Function -> returns repositories data
def returnRepositoriesData(user: str):
    try:
        DataFromGithubObject = DataFromGithub()
        userData = DataFromGithub.getUserDataFromGithub(DataFromGithubObject,user)
        repositoriesData = DataFromGithub.getRepositoriesDataFromGithub(DataFromGithubObject,userData)
        languagesData = DataFromGithub.getLanguagesDataFromGithub(DataFromGithubObject,repositoriesData)
        return repositoriesDataMergeInJSON(repositoriesData,languagesData)
    except:
        return "Username does not exist or username is invalid! Please check if the username is written correctly."

# main Function -> returns user data
def returnUserData(user: str):
    # Check if user exists
    try:
        DataFromGithubObject = DataFromGithub()
        userData = DataFromGithub.getUserDataFromGithub(DataFromGithubObject,user)
        # Check if user has repository
        try:
            repositoriesData = DataFromGithub.getRepositoriesDataFromGithub(DataFromGithubObject,userData)
            languagesData = DataFromGithub.getLanguagesDataFromGithub(DataFromGithubObject,repositoriesData)
            languagesDictionary = languagesSum(languagesData)
            return userDataMergeInJSON(userData,languagesDictionary)
        except:
            return userDataMergeInJSONException(userData)
    except:
        return "Username does not exist or username is invalid! Please check if the username is written correctly."



import requests
import json
import functools
import operator
import collections


# Class -> Downloads information from GitHub
class DataFromGithub:

    header = {'Authorization': 'token %s' % "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"}

    # Get user data form GitHub
    def getUserDataFromGithub(self, user:str):
        userDataRequestUrl = f"https://api.github.com/users/{user}"
        userData = requests.get(userDataRequestUrl, headers = self.header).json()
        return userData

    # Get repositories data form GitHub
    def getRepositoriesDataFromGithub(self, userData:json):
        repositoriesDataRequestUrl = userData['repos_url']
        repositoriesData = requests.get(repositoriesDataRequestUrl, headers = self.header).json()
        return repositoriesData

    # Get languages data form GitHub
    def getLanguagesDataFromGithub(self, repositoriesData:json):

        languagesData = []
        for repositoryData in repositoriesData:
            languagesDataRequest = requests.get(repositoryData['languages_url'], headers = self.header).json()
            languagesData.append(languagesDataRequest)
        return languagesData


# Repositories data converted to JSON format
def repositoriesDataMergeInJSON(repositoriesData:json, languagesData:list):
    finalData = []
    for index in range(len(languagesData)):
        finalData.append({
        "nazwa" : repositoriesData[index]['name'],
        "jezyki" : languagesData[index]
        })
    return json.dumps(finalData, indent=4, sort_keys=True)

# User data Sum amount of bytes for each language
def languageSumAndSort(repositoriesData:json, languagesData:list):
    languageDataList = []
    for index in range(len(languagesData)):
        languageDataList.append(
            languagesData[index]
        )
    # function that changes list to dictionary and sums up their size
    languageDataDictionary = dict(functools.reduce(operator.add,
                            map(collections.Counter, languageDataList)))
    print(languageDataDictionary)                        
    # function that sorts dictionary in descending order
    languageDataDictionarySorted = sorted(languageDataDictionary.items(), key=lambda x: x[1], reverse=True)

    print(languageDataDictionary)
    return json.dumps(languageDataDictionarySorted)

# User data converted to JSON format
def userDataMergeInJSON(userData:json, languagesDictionary:dict):
    finalData = {
        "login" : userData['login'],
        "nazwa" : userData['name'],
        "bio" : userData['bio'],
        "jezyki" : languagesDictionary
    }
    return json.dumps(finalData, indent=4, sort_keys=True)


# main Function -> returns repositories data
def returnRepositoriesData(user:str):
    DataFromGithubObject = DataFromGithub()
    userData = DataFromGithub.getUserDataFromGithub(DataFromGithubObject,user)
    repositoriesData = DataFromGithub.getRepositoriesDataFromGithub(DataFromGithubObject,userData)
    languagesData = DataFromGithub.getLanguagesDataFromGithub(DataFromGithubObject,repositoriesData)
    return repositoriesDataMergeInJSON(repositoriesData,languagesData)

# main Function -> returns user data
def returnUserData(user:str):
    DataFromGithubObject = DataFromGithub()
    userData = DataFromGithub.getUserDataFromGithub(DataFromGithubObject,user)
    repositoriesData = DataFromGithub.getRepositoriesDataFromGithub(DataFromGithubObject,userData)
    languagesData = DataFromGithub.getLanguagesDataFromGithub(DataFromGithubObject,repositoriesData)
    languagesDictionary = languageSumAndSort(repositoriesData,languagesData)
    return userDataMergeInJSON(userData,languagesDictionary)


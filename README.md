# allegro-summer-experience-2022

My email in recruitment process : `kuba.sachajko@gmail.com`

--
# Task Number 3 - Creating Software API

# GitHub Api
To start this application, GitHub Authentication token will be needed. This token has to be passed exactly to backend.py in line 11 :

10.   # Authorization token needed to proceed
11.   header = {'Authorization': 'token %s' % "<PLACE FOR GITHUB AUTHENTICATION TOKEN>"}

In order to start this application apiHandler.py has to be started.
This application will start flask server hosted on `localhost:5000`.

When apiHandler.py is running two types of requests are available:
1. On url: `localhost:5000/GitHubApi/User/{user}`. Information in JSON format about GitHub user will be provied.
Fields with pieces of information such as:
  - GitHub Bio
  - List of languages used in repositories {language name: bytes of code}
  - GitHub Login
  - GitHub Name
2. On url: `localhost:5000/GitHubApi/Repositories/{user}`. Information in JSON format about GitHub user repositories will be provided.
Fields with pieces of information such as:
  - GitHub Repository Name
  - List of languages used in repository {language name: bytes of code}

```
# REPOSITORIES JSON FORMAT:
```
{
  "repositories": [
    {
      "languages": {
        "languageName": bytesOfCode,
        "languageName": bytesOfCode,
        "languageName": bytesOfCode
      }, 
      "name": "GitHubRepositoryName"
    }, 
    {
      "languages": {
        "languageName": bytesOfCode,
        "languageName": bytesOfCode
      }, 
      "name": "GitHubRepositoryName"
    }
  ]
}
```

# USER JSON FORMAT:
```
{
  "bio": "GitHubBion",
  "languages": {
    "languageName": bytesOfCode,
    "languageName": bytesOfCode,
    "languageName": bytesOfCode
  },
  "login": "GitHubLogin",
  "name": "GitHubName",
}
```
# Error Handling
Server should respond if given username does not exist or if there is a typing error.
In user querry there was an error when there were no repositories, but account was present. If this error is present field languages will return `null`.
Server runs in debug mode just to format the data.
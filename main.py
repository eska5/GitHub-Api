import requests
from tkinter import *
import customtkinter

# github Username to find
username = "eska5"

# url to request
url = f"https://api.github.com/users/{username}"

# make the request and return the json
user_data = requests.get(url).json()

# pretty print JSON data
print(user_data)
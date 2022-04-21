from flask import Flask, redirect, render_template, url_for, request
from flask_cors import CORS, cross_origin
import backend as backendApi

app = Flask(__name__)
cors = CORS(app, resources={r"/GitHubApi": {"origins": "http://localhost:5000"}})

@app.route('/GitHubApi/Repositories/<string:user>', methods=["GET"], strict_slashes=False)
def Repositories(user : str):
    response = backendApi.returnRepositoriesData(user)
    return response

@app.route('/GitHubApi/User/<string:user>', methods=["GET"], strict_slashes=False)
def User(user : str):
    response = backendApi.returnUserData(user)
    return response
    
if __name__ == '__main__':
   app.run(debug = True)
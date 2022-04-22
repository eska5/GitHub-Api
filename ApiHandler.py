from flask import Flask
import backend

app = Flask(__name__)

@app.route('/GitHubApi/Repositories/<string:user>', methods=["GET"], strict_slashes=False)
def Repositories(user:str):
    response = backend.returnRepositoriesData(user)
    return response

@app.route('/GitHubApi/User/<string:user>', methods=["GET"], strict_slashes=False)
def User(user:str):
    response = backend.returnUserData(user)
    return response
    
if __name__ == '__main__':
   app.run(debug = True)
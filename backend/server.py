from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

server = Flask(__name__)
CORS(server,resources={r"*": {"origins": "*"}})

forAccessToken = 'https://www.linkedin.com/oauth/v2/accessToken'

ForEmail = 'https://api.linkedin.com/v2/clientAwareMemberHandles?q=members&projection=(elements*(primary,type,handle~))'

ForUserProfile = 'https://api.linkedin.com/v2/me?projection=(id,localizedFirstName,localizedLastName,profilePicture(displayImage~digitalmediaAsset:playableStreams))'

def getAccessToken(code):
    Headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    parameters = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:5173/',
        'client_id':'86zllnqjpdcyws',
        'client_secret':'9jbQvqg1Gmyun0O5'
    }
    token = requests.post(forAccessToken,data=parameters,headers=Headers)
    return token.json().get('access_token')

def getUserProfile(accessToken):
    Headers = {
        "Authorization": "Bearer " + accessToken
    }
    response = requests.get(ForUserProfile,headers=Headers).json()
    profile = {
        "id":response.get('id'),
        "firstName":response.get('localizedFirstName'),
        "lastName":response.get('localizedLastName'),
        "profilePicture":response.get('profilePicture').get('displayImage~').get('elements')[0].get('identifiers')[0].get('identifier')
    }
    return profile

def getUserEmail(accessToken):
    Headers = {
        "Authorization": "Bearer " + accessToken
    }
    email = requests.get(ForEmail,headers=Headers).json().get('elements')[0].get('handle~').get('emailAddress')
    return email

@server.route('/auth', methods=['GET'])
def auth():
    code = request.args.get('code')
    accessToken = getAccessToken(code)
    userProfile = getUserProfile(accessToken)
    userEmail = getUserEmail(accessToken)
    return jsonify({'userProfile':userProfile,"EMail":userEmail})

if __name__ == '__main__':
    server.run(debug=True)
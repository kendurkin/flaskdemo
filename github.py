import requests
import json

#url = "https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript"
#response = requests.get(url)
#response_dict = response.json()

#print response_dict

gh_username = raw_input('GitHub username: ')
gh_password = raw_input('Github password: ')
payload = json.dumps({'scopes':[],'note':"adicu tutorial"})

gh_response = requests.post('https://api.github.com/authorizations',auth=(gh_username,gh_password), data = payload)
print gh_response.json()['token']

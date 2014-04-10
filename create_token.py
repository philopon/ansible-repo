#!/usr/bin/env python

import requests
import getpass
import json
import sys
import os.path

GITHUB      = True
GITHUB_USER = "philopon"
GITHUB_URL  = "https://api.github.com/authorizations"

HEROKU      = True
HEROKU_USER = "philopon.dependence@gmail.com"
HEROKU_URL  = "https://api.heroku.com/oauth/authorizations"

result = {}

## github

if GITHUB:
    github_r = requests.get(GITHUB_URL, auth=(GITHUB_USER, getpass.getpass(prompt = "github password:")))
    github   = filter(lambda x: x[u"note"] == "ansible", github_r.json())

    if github:
       result["github_api_token"] = github[0][u"token"]

# heroku

if HEROKU:
    heroku_r = requests.get(HEROKU_URL, auth=(HEROKU_USER,  getpass.getpass(prompt = "heroku password:")))
    heroku   = filter(lambda x: x[u"description"] == "Heroku CLI", heroku_r.json())
    if heroku:
        result["heroku_api_token"] = heroku[0][u"access_tokens"][0][u"token"]

## write file

filename = os.path.join(os.path.dirname(sys.argv[0]), "token.json")
with open(filename, 'w') as file:
    file.write(json.dumps(result) + '\n')

os.chmod(filename, 0600)


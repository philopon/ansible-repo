#!/usr/bin/env python

import getpass
import json
import sys
import os.path
import urllib2
import base64

GITHUB      = True
GITHUB_URL  = "https://api.github.com/authorizations"

HEROKU      = True
HEROKU_URL  = "https://api.heroku.com/oauth/authorizations"

def request (url, username, password):
    b64 = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    req = urllib2.Request(url)
    req.add_header("Authorization", "Basic %s" % b64)
    return json.load(urllib2.urlopen(req))

result = {}

if GITHUB:
    sys.stdout.write("github username:")
    userid = raw_input()
    passwd = getpass.getpass(prompt = "github password:")
    r = request(GITHUB_URL, userid, passwd)
    s = filter(lambda x: x[u"note"] == "ansible", r)
    if s:
       result["github_user_name"] = userid
       result["github_api_token"] = s[0][u"token"]

# heroku

if HEROKU:
    sys.stdout.write("heroku username:")
    userid = raw_input()
    passwd = getpass.getpass(prompt = "heroku password:")
    r = request(HEROKU_URL, userid, passwd)
    s = filter(lambda x: x[u"description"] == "Heroku CLI", r)
    if s:
        result["heroku_user_name"] = userid
        result["heroku_api_token"] = s[0][u"access_tokens"][0][u"token"]

## write file

filename = os.path.join(os.path.dirname(sys.argv[0]), ".token.json")
with open(filename, 'w') as file:
    file.write(json.dumps(result) + '\n')

os.chmod(filename, 0600)


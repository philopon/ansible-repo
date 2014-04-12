#!/usr/bin/python

import urllib2, base64, json, sys

username = sys.argv[1]
password = sys.argv[2]
key      = sys.argv[3]

URL = "https://api.heroku.com/account/keys/"

base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

req = urllib2.Request(URL)
req.add_header("Accept", "application/vnd.heroku+json; version=3")
req.add_header("Content-Type", "application/json")
req.add_header("Authorization", "Basic %s" % base64string)

res = json.load(urllib2.urlopen(req))

if filter(lambda x: x[u'public_key'] == key, res):
    print "already exists."
    sys.exit(0)
else:
    print "not exists."
    sys.exit(1)



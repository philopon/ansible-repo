#!/usr/bin/env python

import urllib2
import re
BASE = 'http://hackage.haskell.org'
version_re = re.compile('^\s*version\s*:\s*(\S+)', re.I)

def get_latest_version(pkg, base = BASE):
    req = urllib2.urlopen(base + '/package/' + pkg + '/' + pkg + '.cabal')
    for line in req:
        version = version_re.match(line)
        if version:
            return version.group(1)
        


if __name__ == '__main__':
    import sys
    try:
        print get_latest_version(sys.argv[1])
    except urllib2.URLError as e:
        sys.stderr.write(str(e) + '\n')
        sys.exit(1)



#!/usr/bin/python

###
#
# InstaCLI
# Takes a URL as an argument and saves to Instapaper.
#
# By Josh Lapham [josh@joshlapham.com]
#
###

import sys
import urllib

# VARIABLES
username = "YOUR_USER_NAME"
password = "YOUR_PASSWORD"

# FUNCTIONS
# Post data to Instapaper API.
def postToAPI():
    # Put it all together into a URL to pass to Instapaper API.
    urldata = "username=%s&password=%s&url=%s" % (username,password,urlstring)
    f = urllib.urlopen("https://www.instapaper.com/api/add?", urldata)
    s = f.read()
    f.close()
    print s
    return

if len(sys.argv) == 1:
    sys.exit("Usage: insta [URL]")
elif len(sys.argv) >= 1:
    urlstring = sys.argv[1]
    postToAPI()

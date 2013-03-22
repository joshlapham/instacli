#!/usr/bin/python

###
#
# InstaCLI
# Takes a URL as an argument and adds to Instapaper.
#
# By Josh Lapham [josh@joshlapham.com]
#
# https://github.com/joshlapham/instacli
#
# License: Beerware
#
###

import sys
import urllib

## VARIABLES
# Instapaper username and password
username = "YOUR_USER_NAME"
password = "YOUR_PASSWORD"

## FUNCTIONS
# Post data to Instapaper API
def postToAPI(urlstring):
    # Put it all together into a URL to pass to Instapaper API
    urldata = "username=%s&password=%s&url=%s" % (username,password,urlstring)
    f = urllib.urlopen("https://www.instapaper.com/api/add?", urldata)
    s = f.read()
    f.close()
    if s == '201':
    	print "URL successfully saved to Instapaper."
    else:
    	print "ERROR: Could not save URL to Instapaper."
    return

## MAIN
# Check if an argument was given; exit with usage message if none
if len(sys.argv) == 1:
    sys.exit("Usage: insta [URL]")
# If an argument was given then pass to postToAPI function
elif len(sys.argv) >= 1:
    postToAPI(sys.argv[1])
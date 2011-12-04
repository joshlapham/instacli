# Instapaper CLI client written in Python

import urllib

# VARIABLES
username = "a@leagueofevil.org"
password = "crapone85"

# Prompt user for URL, put result in urlstring variable.
urlstring = raw_input("URL: ")

# Put it all together into a URL to pass to Instapaper API.
urldata = "username=%s&password=%s&url=%s" % (username,password,urlstring)

# Post data to Instapaper API.
f = urllib.urlopen("https://www.instapaper.com/api/add?", urldata)
s = f.read()
f.close()
print s

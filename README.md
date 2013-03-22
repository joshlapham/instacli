## InstaCLI

By Josh Lapham [josh@joshlapham.com]

https://github.com/joshlapham/instacli

License: Beerware

### What this does

A simple Python script that takes a URL as an argument and adds to [Instapaper](https://instapaper.com).

### Usage

Be sure to add your [Instapaper](https://instapaper.com) API key to the script.

Run the script and supply a URL as an argument.

e.g. `python instacli.py http://thoughtmaybe.com` or `thoughtmaybe.com` will add the URL to [Instapaper](https://instapaper.com) and return a message.

### TODO

* If status fails then prompt - [try again?, abort?].
* Option to add Title and Description (blank is optional).
* Check if strings are empty, omit from URL API data.
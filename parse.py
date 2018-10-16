
import re
import webbrowser

def Find(s):
    # findall() has been used
    # with valid conditions for urls in string
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', s)
    for x in url:
        x = str(x)
        webbrowser.open_new_tab(x)
    return url
s = 'The Hurricane Harvey and Irma have left many displaced and in need. A lot of organizations areâ€¦ https://t.co/MHbL8gnmv4'
Find(s)

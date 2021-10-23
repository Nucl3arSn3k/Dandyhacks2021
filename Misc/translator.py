import http.client
import html2text # https://pypi.org/project/html2text/
from bs4 import BeautifulSoup # https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_installation.htm 
from PyQt6 import QtCore


#
url = "http://kite.com"
html = urlopen(url).read()
soup = BeautifulSoup(html)

for script in soup(["script", "style"]):
    script.decompose() # deletes out tags

strips = soup.stripped_strings

# qt links: https://doc.qt.io/qtforpython/PySide6/QtCore/QStringConverter.html, https://doc.qt.io/qtforpython/quickstart.html

def switchNotation(argument):
    switcher = {
        "English": "en",
        "Spanish": "es",
        "Italian": "it",
        "French": "fr",
        "German": "de",
    }
    return switcher.get(argument, "en")


# Encode
string =  "Hello World"
targetLanguage = "Spanish"
sourceLanguage = "English"
targetLanguage = switchNotation(targetLanguage)
sourceLanguage = switchNotation(sourceLanguage)


fromUtf16 = QtCore.QStringEncoder(QtCore.QStringEncoder.Encoding.Utf8)
encodedString = fromUtf16(string)

# request logic
conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

# string as
encodedString = "q=Hello%2C%20world!&target=" + targetLanguage + "&source=" + sourceLanguage

headers = {  # all static fieldse
    "content-type": "application/x-www-form-urlencoded",
    "accept-encoding": "application/gzip",
    "x-rapidapi-key": "4679425f88mshcb1cacb0c2357d8p1e02e8jsn4e69292eb0dc",
    "x-rapidapi-host": "google-translate1.p.rapidapi.com",
}

conn.request("POST", "/language/translate/v2", encodedString, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
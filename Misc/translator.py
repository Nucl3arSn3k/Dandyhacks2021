import http.client
from PyQt6 import QtCore

# qt links: https://doc.qt.io/qtforpython/PySide6/QtCore/QStringConverter.html, https://doc.qt.io/qtforpython/quickstart.html

def switchNotation(argument):
    switcher = {
        "English": "en",
        "Spanish": "es",
        "Italian": "it",
        "French": "fr",
        "German": "de",
    }
    argument = switcher.get(argument, "en")


# Encode
string = "Hello World" # always in english
language = "Spanish"
switchNotation(language)


fromUtf16 = QtCore.QStringEncoder(QtCore.QStringEncoder.Encoding.Utf8)
encodedString = fromUtf16(string)

# request logic
conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

# string as
encodedString = "q=Hello%2C%20world!&target=" + language + "&source=en"
#                         target lang ^         ^ base lang (always in english)

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
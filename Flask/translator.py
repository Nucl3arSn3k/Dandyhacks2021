import http.client
import re
import html2text  # https://pypi.org/project/html2text/
from PyQt6 import QtCore
from urllib.request import urlopen


# do below upon page load?
def translate_html_from(url):

    rawHtml = urlopen(url).read()

    pList = re.findall("<p>(.*?)</p>", repr(rawHtml))

    resultPList = []
    for p in pList:
        resultPList.append(re.sub(" +", " ", re.sub("<.*?>", " ", p)))

    finalPList = []
    for p in resultPList:
        finalPList.append(translate(p))

    return finalPList


# qt links: https://doc.qt.io/qtforpython/PySide6/QtCore/QStringConverter.html, https://doc.qt.io/qtforpython/quickstart.html
def translate(string):
    resultTargetLang = switchNotation("English")
    resultSourceLang = switchNotation("Español")
    fromUtf16 = QtCore.QStringEncoder(QtCore.QStringEncoder.Encoding.Utf8)
    encodedString = fromUtf16(string)

    # request logic
    conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

    encodedString = (
        "q=Hello%2C%20world!&target=" + resultTargetLang + "&source=" + resultSourceLang
    )

    headers = {  # all static fields
        "content-type": "application/x-www-form-urlencoded",
        "accept-encoding": "application/gzip",
        "x-rapidapi-key": "4679425f88mshcb1cacb0c2357d8p1e02e8jsn4e69292eb0dc",
        "x-rapidapi-host": "google-translate1.p.rapidapi.com",
    }

    conn.request("POST", "/language/translate/v2", encodedString, headers)

    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")


def switchNotation(argument):
    switcher = {
        "English": "en",
        "Español": "es",
        "Italiano": "it",
        "Français": "fr",
        "Deutsche": "de",
    }
    return switcher.get(argument, "en")

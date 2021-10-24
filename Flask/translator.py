import http.client
import json
import re
import urllib.parse
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

    # print(resultPList)
    finalPList = []
    for p in resultPList:
        finalPList.append(translate(p))

    print(finalPList)
    return finalPList


# qt links: https://doc.qt.io/qtforpython/PySide6/QtCore/QStringConverter.html, https://doc.qt.io/qtforpython/quickstart.html
def translate(string):
    resultTargetLang = switchNotation("English")
    resultSourceLang = switchNotation("Español")
    encodedString = urllib.parse.quote(string)

    # request logic
    conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

    encodedString = (
        "q="+ encodedString + "&target=" + resultTargetLang + "&source=" + resultSourceLang
    )

    headers = {  # all static fields
        "content-type": "application/x-www-form-urlencoded",
        "accept-encoding": "application/gzip",
        "x-rapidapi-key": "5c9ed3bc87mshc7f85a2f9e9e010p12d5f4jsn46fd30e26dde",
        "x-rapidapi-host": "google-translate1.p.rapidapi.com",
    }

    conn.request("POST", "/language/translate/v2", encodedString, headers)

    res = conn.getresponse()
    data = res.read()
    lastLay = json.loads(data.decode("utf-8"))["data"]["translations"][0]["translatedText"]
    return lastLay


def switchNotation(argument):
    switcher = {
        "English": "en",
        "Español": "es",
        "Italiano": "it",
        "Français": "fr",
        "Deutsche": "de",
    }
    return switcher.get(argument, "en")

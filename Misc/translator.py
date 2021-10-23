import http.client
import PySide6.QtCore
#qt links: https://doc.qt.io/qtforpython/PySide6/QtCore/QStringConverter.html, https://doc.qt.io/qtforpython/quickstart.html


# Encode 
string = "Hello World"
fromUtf16 = QStringEncoder(QStringEncoder.Utf8)
encodedString = fromUtf16(string)

# request logic
conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

# string as 
encodedString = "q=Hello%2C%20world!&target=es&source=en"
#                         target lang ^         ^ base lang

headers = { # all static fields
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "4679425f88mshcb1cacb0c2357d8p1e02e8jsn4e69292eb0dc",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

conn.request("POST", "/language/translate/v2", encodedString, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
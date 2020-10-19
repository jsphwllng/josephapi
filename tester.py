import requests as r

html = r.get("http://127.0.0.1:5000/")
print(html.text)

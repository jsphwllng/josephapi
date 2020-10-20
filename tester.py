import requests as r

html = r.get("https://glacial-citadel-82094.herokuapp.com/cv/all")
print(html.text)

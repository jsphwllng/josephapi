# A RESTful API of [@jsphwllng's](https://twitter.com/jsphWllng) CV 😎
You can `get` my CV, contact details, etc. As this is relatively sensitive information I will not be allowing `POST` requests.

If you want to skip the nerd stuff and get my CV straight away run this in your terminal:
```bash
    pip3 install requests
    python3
```
```python
    import requests as r
    import json
    html = r.get("http://127.0.0.1:5000/cv/all")
    print(html.text)
```
or visit visit [here](/cv/all) but that's no fun at all!

***
**Uses**

`GET /cv/all`

`GET /cv/contact_details`

`GET /cv/languages`

`GET /cv/hobbies`

`GET /cv/experiences`

`GET /cv/projects`
***
<sub>have fun!</sub>


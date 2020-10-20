# A RESTful API of [@jsphwllng's](https://twitter.com/jsphWllng) CV.
You can `GET` my CV, contact details, etc. As this is relatively sensitive information I will not be allowing `POST`, `PATCH` or `DELETE` requests.

If you want to skip the ahead and get my CV straight away run this in your terminal:
```bash
    pip install requests
    python
```
```python
    import requests as r
    html = r.get("https://joseph-api.herokuapp.com/cv/all")
    print(html.text)
```
[or visit here](https://joseph-api.herokuapp.com/cv/all).

***
**Uses**

`GET /cv/all`

`GET /cv/about`

`GET /cv/contact_details`

`GET /cv/languages`

`GET /cv/hobbies`

`GET /cv/experiences`

`GET /cv/projects`
***
<sub>have fun!</sub>

<sub>-joe</sub>


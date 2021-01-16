from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import markdown
import markdown.extensions.fenced_code
from pygments.formatters import HtmlFormatter
import json

comments = {}

app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def page_not_found(e):
  return "<h1>page not found</h1>", 404


@app.route("/", methods=["GET"])
def index():
  if (request.method == 'GET'):
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code", "codehilite"]
    )

    # Generate Css for syntax highlighting s
    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"

    md_template = md_css_string + md_template_string
    return md_template
  else:
    return jsonify({f"request.method": "not allowed!"})


@app.route("/cv/", methods=["GET"])
def no():
  return "/cv is not a valid domain, sorry!"


@app.route('/cv/all', methods=["GET"])
def full_cv():
  full_cv = jsonify(

      about='A diplomat turned traveler turned developer. Experienced in development and managing teams. Having lived in 4 countries I have strong intercultural communication skills. I love learning new tech, automating my work, overusing the word groovy and eating barbecue.',
      contact_details=["jsphwllng@gmail.com",
                       "https://github.com/jsphwllng", "https://twitter.com/jsphWllng"],
      languages=["python", "ruby", "golang", "MERN", "rails",
                 "flask", "typeScript", "postgresql", "robot framework"],
      experiences=[
          {
          'role': "Backend Engineer",
          'company': "Alteos, Berlin",
          'description': ["Back end development including Unit, Integration and End to End testing using Typescript, Golang and Python.", "Experience using a large codebase"],
          "duration": "ongoing"
      },
          {
          'role': "Coding Teaching Assistant",
          'company': "Le Wagon, Berlin",
          'description': ["Lead a team during development of two webapps including code review and project management. Finished first place in the in -house coding tournament, finished in the top of my batch. In my spare time I also studied the MERN stack and Golang.", "currently acting as a teaching assistant in a freelance capacity"],
          "duration": "07/2020 - 11/2020"
      },
          {
          'role': "Global Project Management Intern",
          'company': "eBay, Berlin",
          'description': ["Oversaw projects within eBay including policy changes, dealing with 3rd party vendors, demergers and banking. This gave me an overall insight into project management with a managing people and tasks.", "Gained experience in project management alongside handling multiple deadlines, compliance and time management"],
          "duration": "11/2019 - 05/2020"
      },
          {
          'role': "Entry Clearance Officer",
          'company': "Foreign and Commonwealth Office, Abu Dhabi",
          'description': ["Assessed visa applications and justifying these decisions both orally and in writing. This position gave me great experience in handling a high pressure and demanding working environment.", "Managed the Tech Overhaul process for the embassy. Tech Overhaul comprised of updating existing software and hardware. In this capacity I managed a team of staff to implement and train in the new technologies."],
          "duration": "02/2016 - 09/2018"
      }],

      projects=[
          {
              "http://www.spontan.fun": "Lead a team of 4 developing a webapp to encourage spontaneous events. A 10 day coding and design sprint. Took the leading role in developing both the back and front -end of the website alongside taking a leadership position using scrum method and maintaining Trello boards, hosting standup meetings, code reviews and resolving group conflicts."
          },
          {"https://twitter.com/theanimalbands": "A twitter bot designed for fun however this project outlines my ability to self learn and use Python, Amazon AWS servers."
           },
          {"https://github.com/jsphwllng?tab=repositories": "smaller github projects including a webcam instagram account for my plants and an internet speed monitor"
           }
      ],
      hobbies=["disco", "eating", "cooking", "plant dad", "blogging", "yoga", "ping pong",
               "fermentation", "ginger beer connoisseur", "twitter bots", "overly complicated CVs"]
  )
  if (request.method == 'GET'):
    return full_cv


@app.route("/cv/contact_details", methods=["GET"])
def contact_details():
  if (request.method == 'GET'):
     return jsonify(
         contact_details=[
             "jsphwllng@gmail.com", "https://github.com/jsphwllng", "https: //twitter.com/jsphWllng"]
     )


@app.route("/cv/languages", methods=["GET"])
def languages():
  if (request.method == 'GET'):
     return jsonify(languages=["python", "ruby", "some golang", "MERN", "rails", "flask", "mongoDB", "heroku", "AWS", "github"]
                    )


@app.route("/cv/hobbies", methods=["GET"])
def hobbies():
  if (request.method == 'GET'):
    return jsonify(hobbies=["disco", "eating", "cooking", "plant dad", "blogging", "yoga", "ping pong", "Fermentation", "Ginger Beer Connoisseur", "twitter bots"])


@app.route("/cv/projects", methods=["GET"])
def projects():
  if (request.method == 'GET'):
     return jsonify(projects=[{
         "http://www.spontan.fun": "Lead a team of 4 developing a webapp to encourage spontaneous events. A 10 day coding and design sprint. Took the leading role in developing both the back and front -end of the website alongside taking a leadership position using scrum method and maintaining Trello boards, hosting standup meetings, code reviews and resolving group conflicts."
     },
         {"https://twitter.com/theanimalbands": "A twitter bot designed for fun however this project outlines my ability to self learn and use Python, Amazon AWS servers."},
         {"https://github.com/jsphwllng?tab=repositories": "smaller github projects including a webcam instagram account for my plants and an internet speed monitor"}]
     )


@app.route("/cv/experiences", methods=["GET"])
def experiences():
  if (request.method == 'GET'):
   return jsonify(experiences=[{
       'role': "Backend Engineer",
       'company': "Alteos, Berlin",
       'description': ["Back end development including Unit, Integration and End to End testing using Typescript, Golang and Python.", "Experience using a large codebase"],
       "duration": "ongoing"
   },
       {
       'role': "Coding Teaching Assistant",
       'company': "Le Wagon, Berlin",
       'description': ["Lead a team during development of two webapps including code review and project management. Finished first place in the in -house coding tournament, finished in the top of my batch. In my spare time I also studied the MERN stack and Golang.", "currently acting as a teaching assistant in a freelance capacity"],
       "duration": "07/2020 - 11/2020"
   },
       {
       'role': "Global Project Management Intern",
       'company': "eBay, Berlin",
       'description': ["Oversaw projects within eBay including policy changes, dealing with 3rd party vendors, demergers and banking. This gave me an overall insight into project management with a managing people and tasks.", "Gained experience in project management alongside handling multiple deadlines, compliance and time management"],
       "duration": "11/2019 - 05/2020"
   },
       {
       'role': "Entry Clearance Officer",
       'company': "Foreign and Commonwealth Office, Abu Dhabi",
       'description': ["Assessed visa applications and justifying these decisions both orally and in writing. This position gave me great experience in handling a high pressure and demanding working environment.", "Managed the Tech Overhaul process for the embassy. Tech Overhaul comprised of updating existing software and hardware. In this capacity I managed a team of staff to implement and train in the new technologies."],
       "duration": "02/2016 - 09/2018"
   }])


if __name__ == '__main__':
    app.run(debug=True)

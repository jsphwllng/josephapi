from flask import Flask, jsonify, request, redirect
from flask_restful import Resource, Api, reqparse
import markdown
import markdown.extensions.fenced_code
from pygments.formatters import HtmlFormatter
import cv_info

comments = {}

app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def page_not_found(e):
  return redirect("/", code=302)


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

@app.route("/contact_details", methods=["GET"])
def contact_details():
  if (request.method == 'GET'):
     return jsonify(
         cv_info.contact_details
     )


@app.route("/languages", methods=["GET"])
def languages():
  if (request.method == 'GET'):
     return jsonify(
         cv_info.languages
     )


@app.route("/hobbies", methods=["GET"])
def hobbies():
  if (request.method == 'GET'):
    return jsonify(
        cv_info.hobbies
    )


@app.route("/projects", methods=["GET"])
def projects():
  if (request.method == 'GET'):
     return jsonify(
         cv_info.projects
     )


@app.route("/experiences", methods=["GET"])
def experiences():
  if (request.method == 'GET'):
   return jsonify(
       cv_info.experiences
   )


@app.route("/about", methods=["GET"])
def about():
  if (request.method == 'GET'):
   return jsonify(
       cv_info.about
   )

if __name__ == '__main__':
    app.run(debug=True)

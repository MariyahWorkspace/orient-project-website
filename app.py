from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import load_courses

app = Flask(__name__)

@app.route("/")
def home():
  courses = load_courses()
  return render_template('home.html', courses=courses)

@app.route("/api/courses")
def course_list():
  courses = load_courses()
  return jsonify(courses)

@app.route("/about", methods=["GET", "POST"])
def about():
  return render_template(("about.html"))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

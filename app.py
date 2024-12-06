from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import load_courses, load_course, add_application_to_db

app = Flask(__name__)

@app.route("/")
def home():
  courses = load_courses()
  return render_template('home.html', courses=courses)

@app.route("/api/courses")
def course_list():
  courses = load_courses()
  return jsonify(courses)

@app.route("/courses/<id>")
def show_course(id):
  course = load_course(id)
  return render_template("course-page.html", course = course)

@app.route("/courses/<id>/apply", methods=["GET", "POST"])
def apply_course(id):
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        motivation = request.form.get("motivation")
    data = {
            "name": name,
            "email": email,
            "phone": phone,
            "motivation": motivation
        }
    course = load_course(id)
    add_application_to_db(id, data)
    return render_template("submit.html", application=data, course=course)

@app.route("/about", methods=["GET", "POST"])
def about():
  return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

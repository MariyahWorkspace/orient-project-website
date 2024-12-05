from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

COURSES = [{
    "id":
    1,
    "title":
    "Hadoop",
    "duration":
    "4 hours",
    "description":
    "Get an overview of Hadoop along with its ecosystem and use cases."
}, {
    "id":
    2,
    "title":
    "Machine Learning",
    "duration":
    "6 hours",
    "description":
    "Learn the fundamentals of machine learning, including algorithms and applications."
}, {
    "id":
    3,
    "title":
    "Web Development",
    "duration":
    "5 hours",
    "description":
    "Explore modern web development techniques, including HTML, CSS, and JavaScript."
}, {
    "id":
    4,
    "title":
    "Data Science",
    "duration":
    "8 hours",
    "description":
    "Dive into data science with practical techniques in data manipulation and visualization."
}]


@app.route("/")
def home():
  return render_template('home.html', courses=COURSES)


@app.route("/api/courses")
def course_list():
  return jsonify(COURSES)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

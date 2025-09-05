from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/project")
def projects():
    return render_template("project.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about_hobby")
def about_hobby():
    return render_template("about_hobby.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, redirect, url_for, render_template

app = Flask('__main__')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about/")
def about():
    return "About Page"


@app.route("/gallery/")
def gallery():
    return "Gallery Page"


@app.route("/contact/")
def contact():
    return "Contact Page"


@app.route("/admin/")
def admin():
    return "Admin Page"


if __name__ == "__main__":
    app.run(debug=True)

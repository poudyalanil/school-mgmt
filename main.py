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
    return render_template("gallery.html")


@app.route("/contact/")
def contact():
    return "Contact Page"

##############################
##############################
######### Admin Section ########


@app.route("/admin/")
def admin_dashboard():
    return render_template('admin_dashboard.html')


@app.route("/admin/application/")
def admin_application():
    return render_template('admin_applications.html')


@app.route("/admin/calendar/")
def admin_calendar():
    return render_template('admin_calendar.html')


@app.route("/admin/gallery/")
def admin_gallery():
    return render_template('admin_gallery.html')


@app.route("/admin/media/")
def admin_media():
    return render_template('admin_media.html')


@app.route("/admin/notice/")
def admin_notice():
    return render_template('admin_notice.html')


@app.route("/admin/profile/")
def admin_profile():
    return render_template('admin_profile.html')


@app.route("/admin/users/")
def admin_users():
    return render_template('admin_users.html')


if __name__ == "__main__":
    app.run(debug=True)

#views or routes are the url in the website /home etc
from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    print('hello word')
    return render_template("index.html",name = "Fernando")
    
@views.route("/about.html")
def about_page():
    return render_template("about.html")

@views.route("/contact.html")
def contact_page():
    return render_template("contact.html")

@views.route("/resume.html")
def resume_page():
    return render_template("resume.html")
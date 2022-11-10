#views or routes are the url in the website /home etc
from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    print('hello word')
    return render_template("index.html",name = "Fernando")
    
@views.route("/about")
def about_page():
    return render_template("about.html")

@views.route("/contact")
def contact_page():
    return render_template("contact.html")
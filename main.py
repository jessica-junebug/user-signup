from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=["GET"])
def index():
    return render_template('forms.html', name="", password="", vpass="", email="")

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

@app.route("/validated", methods=["POST"])
def valid_login():
 
    username = request.form['username']
    password = request.form['password']
    vpass = request.form["vpass"]
    email = request.form['email']
    
    username_error = ''
    password_error = ''
    email_error = ''
    
    if username == "":
        username_error += "username required"
    elif " " in username:
        username_error += "must contain no spaces"
    elif not (len(username) > 3 and  len(username) < 20):
        username_error += "must be 3-20 characters"

    if " "in password:
        password_error += "please mind the gap"
    elif not (len(password) > 3 and len(password) < 20):  
        password_error += "must be 3-20 characters"
    elif not password == vpass: 
        password_error += "go fish"

    if not email == "":
        if "@" not in email and "." not in email:
            email_error += "ah ha! invalid email"
        elif "" in email:
            email_error += "oops there's a space"
        elif len(email) < 3 and len(email) > 20:
            email_error += "must be this tall to ride (3-20 characters)"

    if not username_error and not password_error and not email_error:
        return redirect("/welcome?username={0}".format(username))
    else:
        return render_template("forms.html",
        username_error=username_error,password_error=password_error, email_error=email_error, username=username, email=email)

app.run()
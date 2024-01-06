from flask import Flask, request, redirect, render_template, url_for, flash, request
from config import Config

# Create a Flask application
app = Flask(__name__)
app.config.from_object(Config)
if app.config['DEBUG']:
    print("Debug mode is enabled.")


# Define other routes and view functions
@app.route("/")
def hello_world():
    return render_template("login.html")

database={'glasgow':'0727','james':'aac','karthik':'asdsf'}

@app.route("/form_login", methods=["POST", "GET"])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            return redirect(url_for('index', name=name1))

@app.route('/index')
def index():
    # Your view function logic here
    return render_template('index.html')

@app.route('/new')
def new():
    # Your view function logic here
    return render_template('new.html')

@app.route('/william_wood')
def william_wood():
    # Your view function logic here
    return render_template('williamWood.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
    
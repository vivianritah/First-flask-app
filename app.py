from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def home():
    return"<h1> Welcome to my Flask App<\h1>"


@app.route('/about')
def about():
    return"<h2> Am Vivian Athens </h2>"

@app.route('/contact')
def contact():
     return"<h3> 0765988756 </h3>"


@app.route('/user/<username>')
def greet_user(username):
    return f'Hello, {username}! Welcome to our website.'


# from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def greet_user(username):
    return render_template('hello.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)

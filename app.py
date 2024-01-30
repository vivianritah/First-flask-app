from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
     return render_template('contact.html')


@app.route('/user/<username>')
def greet_user(username):
    return render_template('Hello, {username}! Welcome to our website.')



# @app.route('/user/<username>')
# def greet_user(username):
#     return render_template('hello.html', username=username)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'Thank you, {name}! We received your submission with email: {email}'

#Modifying
@app.route('/hello', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle POST request
        return 'This is a POST request!'
    # Handle GET request
    return render_template('index.html')
    return render_template('submissionform.html')


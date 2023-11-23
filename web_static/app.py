from flask import Flask, render_template

app = Flask(__name__)

# sign up and sign in routes
@app.route('/login')
def login():
    return render_template('signUp.html', 
                           pageTitle='Sign In',
                           formAction='/formhandler',
                           formMethod='post',
                           submitButtonText='Log In',
                           alternateButtonText='Sign Up')
# @app.route('/signup')
# def signUp():
#     return render_template('signup.html')

# displays home page
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/discover')
def discover():
    return render_template('discover.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

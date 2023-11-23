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
# displays home page
@app.route('/home')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)

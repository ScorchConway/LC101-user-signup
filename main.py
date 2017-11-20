from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST'])
def post_to_index():
    username = request.form['username']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']
    print('smoke')
    email = request.form['email']

    username_error = ''
    password_error = ''
    password_conf_error = ''
    email_error = ''
    
    whitespace = re.compile('\s')
    if not username or whitespace.search(username) or not(2 < len(username) < 21):
        username_error = 'please submit a valid username (3-20 characters, no spaces)'
    
    if not password or whitespace.search(password) or not(2 < len(password) < 21):
        password_error = 'please submit a valid password (3-20 characters, no spaces)'

    if not (password == password_confirmation):
        password_conf_error = "passwords don't match"

    if email:
        if not '@' in email or not '.' in email or whitespace.search(email) or not(2 < len(email) < 21):
            email_error = 'please submit valid email (ex: fake@email.com)'

    if username_error or password_error or password_conf_error or email_error:
        return render_template("user-signup.html",  username_error=username_error,
                                                    password_error=password_error, 
                                                    password_conf_error=password_conf_error, 
                                                    email_error=email_error,
                                                    username=username,
                                                    email=email) 
    else: 
        return redirect('/welcome?username={0}'.format(username))

@app.route('/')
def index():
    return render_template("user-signup.html")

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template("welcome.html", username=username)
    

app.run()

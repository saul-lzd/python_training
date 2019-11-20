from flask import Flask, render_template, Response, redirect, url_for, request, make_response, session, flash
from data import Persons

app = Flask(__name__)

app.secret_key = "myPersonalAppSK"

# enable debug mode
# app.debug = True

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/home/')
def home_2():
    user = request.cookies.get("user")
    if (user == None):
        return redirect('/')
    else:
        return redirect(url_for('home', name = user))

@app.route('/home/<name>')
def home(name):
    # set cookie for logged user
    return render_template('home.html', username=name)

@app.route('/people')
def people():
    # get user from cookie
    # name = request.cookies.get("user")
    # get user from session
    name = session['user']
    return render_template('people.html', people=Persons(), user=name)

@app.route('/go_people')
def go_people():
    return redirect('/people')

@app.route('/getHtml')
def get_html():
    return "<h1>Hola</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    response = None
    if request.method == "POST":

       user = request.form['name']
       if (user == "admin"):
            response = make_response(redirect(url_for('home',  name=user)))
            # set user in cookie
            response.set_cookie("user", user)
            # set user in session
            session['user'] = user
            return response
       else:
            flash("User invalid")
            response = make_response(redirect(url_for('index')))
            return response
       '''
        # args is a dictionary object
        # containing form pair-values
        user = request.args.get('name')
        response = make_response(redirect(url_for('home', name=user)))
        # set user in cookie
        response.set_cookie("user", user)
        # set user in session
        session['user'] = user
        '''



if __name__ == '__main__':
    app.run()
    # enable   debug mode
    # app.run(debug=True)

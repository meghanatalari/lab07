# app.py

from flask import Flask, render_template, request, redirect, url_for
from model.user import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

# Registration Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password == confirm_password:
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('thankyou'))
        else:
            return 'Password and Confirm Password do not match!'
    return render_template('signup.html')

# Login Page
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    # Your login logic here
    # ... (authenticate user and handle login)

    return render_template('signin.html')


# Thank You Page
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return redirect(url_for('secret_page'))
        else:
            return 'Invalid email or password!'

    return render_template('signin.html')

# Secret Page
@app.route('/secret_page')
def secret_page():
    return render_template('secret_page.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

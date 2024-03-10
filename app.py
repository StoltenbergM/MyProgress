from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from database import db
from models import User, Goal  # Import your User model

'''
Flask: The Flask class is used to create an instance of a Flask web application.
render_template: This function is used to render HTML templates.
request: This object provides access to incoming request data such as form data.
redirect: This function is used to redirect the user to a different URL.
url_for: This function is used to generate URLs for Flask routes.
flash: This function is used to display a short message to the user, typically for success or error feedback.
SQLAlchemy: This is an Object-Relational Mapping (ORM) library for Python. It provides tools for working with databases in an object-oriented manner.
LoginManager: This class provides user session management for Flask applications, including login and logout functionality.
login_user, login_required, current_user, UserMixin, logout_user: These are utility functions and classes provided by Flask-Login for managing user authentication and sessions.
User: This imports the User model from models.py, which represents users in your application.
'''

'''Create a Flask Application'''

app = Flask(__name__, static_url_path='/static')

'''Set Up Database Integration'''

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'averyverysecret1020304050607'
db.init_app(app)

'''Call-back function that Flask-Login uses to load user'''

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

'''Home route'''

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

'''Register Route - Implement User Registration'''

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

'''Login Route - Implement User Login'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

'''Dashboard Route'''

@app.route('/dashboard')
@login_required
def dashboard():
    goals = current_user.goals
    return render_template('dashboard.html', goals=goals)

'''Create Goal Route'''

@app.route('/add_goal', methods=['POST'])
@login_required
def add_goal():
    if request.method == 'POST':
        name = request.form['name']
        target = int(request.form['target'])
        current = int(request.form['current'])
        new_goal = Goal(name=name, target=target, current=current, user_id=current_user.id)
        db.session.add(new_goal)
        db.session.commit()
        flash('Goal added successfully!', 'success')
        return redirect(url_for('dashboard'))

'''Logout Route'''

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

'''Error 404 Route'''

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

'''Main'''

if __name__ == '__main__':
    # Create the database tables before running the application
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)

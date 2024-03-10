'''Step 2: Create a Flask Application'''

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

'''Step 3: Set Up Database Integration'''

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'averyverysecret1020304050607'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

''''''

from flask import redirect, url_for

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

'''Step 4: Implement User Registration'''

from flask import render_template, request, redirect, url_for, flash

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

'''Step 5: Implement User Login'''

from flask_login import login_user

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

'''Step 6: Implement Session Management'''

from flask_login import LoginManager

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

'''Step 7: Protect Routes and Implement User Authentication'''

from flask_login import login_required, current_user

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

from flask_login import logout_user

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
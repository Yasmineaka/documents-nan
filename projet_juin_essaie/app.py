from flask import Flask, render_template, request, redirect, session
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

# Modèle d'utilisateur
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

# Vérification d'authentification
def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/login')
        return func(*args, **kwargs)
    return decorated_view

# Vérification d'administrateur
def is_admin(user_id):
    user = User.query.get(user_id)
    return user.is_admin

# Route d'accueil
@app.route('/')
def home():
    return 'Bienvenue sur le site !'

# Route d'inscription
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user = User(username=username, password=hashed_password, email=email)
        db.session.add(user)
        db.session.commit()

        return redirect('/login')
    return render_template('register.html')

# Route de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            session['user_id'] = user.id
            return redirect('/dashboard')
        else:
            return 'Informations de connexion invalides'

    return render_template('login.html')

# Route de déconnexion
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')

# Route du tableau de bord
@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']
    user = User.query.get(user_id)
    return f'Bienvenue sur votre tableau de bord, {user.username} !'

# Route du panneau d'administration
@app.route('/admin')
# @admin_required
def admin_panel():
    users = User.query.all()
    return render_template('admin_panel.html', users=users)

# Route de modification d'utilisateur dans le panneau d'administration
@app.route('/admin/edit/<int:user_id>', methods=['GET', 'POST'])
# @admin_required
def admin_edit_user(user_id):
    user = User.query.get(user_id)

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        user.username = username
        user.email = email

        db.session.commit()
        return redirect('/admin')

    return render_template('admin_edit_user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Simuler un compte bancaire avec un solde initial
# solde_compte = 1000
# historique_operations = []

# @app.route('/solde', methods=['GET'])
# def get_solde():
#     return jsonify({"solde": solde_compte})

# @app.route('/transfert', methods=['POST'])
# def transfert():
#     global solde_compte
#     destinataire = request.json.get('destinataire')
#     montant = request.json.get('montant')

#     if montant <= 0:
#         return jsonify({"message": "Le montant doit être positif."}), 400

#     if solde_compte < montant:
#         return jsonify({"message": "Solde insuffisant."}), 400

#     solde_compte -= montant
#     historique_operations.append(f"Transfert de ${montant} vers {destinataire}")
#     return jsonify({"message": "Transfert réussi."})

# @app.route('/retrait', methods=['POST'])
# def retrait():
#     global solde_compte
#     montant = request.json.get('montant')

#     if montant <= 0:
#         return jsonify({"message": "Le montant doit être positif."}), 400

#     if solde_compte < montant:
#         return jsonify({"message": "Solde insuffisant."}), 400

#     solde_compte -= montant
#     historique_operations.append(f"Retrait de ${montant}")
#     return jsonify({"message": "Retrait réussi."})

# @app.route('/historique', methods=['GET'])
# def get_historique():
#     return jsonify({"historique": historique_operations})

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# # Données utilisateur (simulation)
# utilisateur = {'nom': 'John Doe', 'solde': 1000}
# historique_transactions = []

# @app.route('/')
# def dashboard():
#     return render_template('dashboard.html', utilisateur=utilisateur, historique_transactions=historique_transactions)

# @app.route('/effectuer_transaction', methods=['POST'])
# def effectuer_transaction():
#     montant = float(request.form.get('montant'))
#     transaction_type = request.form.get('type')

#     # Gérez les transactions en fonction du type (dépôt ou retrait)
#     if transaction_type == 'depot':
#         # Ajoutez le montant au solde
#         utilisateur['solde'] += montant
#         historique_transactions.append(f'Dépôt de {montant} $')
#     elif transaction_type == 'retrait':
#         # Vérifiez si le solde est suffisant pour le retrait
#         if montant <= utilisateur['solde']:
#             # Retirez le montant du solde
#             utilisateur['solde'] -= montant
#             historique_transactions.append(f'Retrait de {montant} $')
#         else:
#             return "Solde insuffisant"

#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True)
# ===========================
# from flask import Flask, render_template, request, redirect, url_for
# from flask import Flask, jsonify, request
# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = 'votre_clé_secrète'
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'connexion'

# class Utilisateur(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.String(100))
#     email = db.Column(db.String(100), unique=True)
#     contact = db.Column(db.String(20), unique=True)
#     mot_de_passe = db.Column(db.String(100))

# @login_manager.user_loader
# def load_user(user_id):
#     return Utilisateur.query.get(int(user_id))

# @app.route('/')
# def accueil():
#     return render_template("accueil.html")

# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     if request.method == 'POST':
#         nom = request.form.get('nom')
#         email = request.form.get('email')
#         contact = request.form.get('contact')
#         mot_de_passe = request.form.get('mot_de_passe')

#         # Vérifiez si l'e-mail ou le contact est déjà enregistré
#         existe_email = Utilisateur.query.filter_by(email=email).first()
#         existe_contact = Utilisateur.query.filter_by(contact=contact).first()

#         if existe_email or existe_contact:
#             flash('Cet e-mail ou contact est déjà enregistré.', 'danger')
#             return redirect('/inscription')

#         # Créez un nouvel utilisateur
#         nouvel_utilisateur = Utilisateur(nom=nom, email=email, contact=contact, mot_de_passe=generate_password_hash(mot_de_passe, method='sha256'))

#         # Ajoutez l'utilisateur à la base de données
#         db.session.add(nouvel_utilisateur)
#         db.session.commit()

#         flash('Inscription réussie ! Vous pouvez maintenant vous connecter.', 'success')
#         return redirect('/connexion')

#     return render_template('inscription.html')

# @app.route('/connexion', methods=['GET', 'POST'])
# def connexion():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         mot_de_passe = request.form.get('mot_de_passe')
#         utilisateur = Utilisateur.query.filter_by(email=email).first()

#         if utilisateur and check_password_hash(utilisateur.mot_de_passe, mot_de_passe):
#             login_user(utilisateur)
#             flash('Connexion réussie !', 'success')
#             return redirect('/accueil')
#         else:
#             flash('Identifiants incorrects. Veuillez réessayer.', 'danger')

#     return render_template('connexion.html')

# @app.route('/deconnexion')
# @login_required
# def deconnexion():
#     logout_user()
#     flash('Déconnexion réussie.', 'success')
#     return redirect('/')





# # Simuler un compte bancaire avec un solde initial
# solde_compte = 1000
# historique_operations = []

# @app.route('/solde', methods=['GET'])
# def get_solde():
#     return jsonify({"solde": solde_compte})

# @app.route('/transfert', methods=['POST'])
# def transfert():
#     global solde_compte
#     destinataire = request.json.get('destinataire')
#     montant = request.json.get('montant')

#     if montant <= 0:
#         return jsonify({"message": "Le montant doit être positif."}), 400

#     if solde_compte < montant:
#         return jsonify({"message": "Solde insuffisant."}), 400

#     solde_compte -= montant
#     historique_operations.append(f"Transfert de ${montant} vers {destinataire}")
#     return jsonify({"message": "Transfert réussi."})

# @app.route('/retrait', methods=['POST'])
# def retrait():
#     global solde_compte
#     montant = request.json.get('montant')

#     if montant <= 0:
#         return jsonify({"message": "Le montant doit être positif."}), 400

#     if solde_compte < montant:
#         return jsonify({"message": "Solde insuffisant."}), 400

#     solde_compte -= montant
#     historique_operations.append(f"Retrait de ${montant}")
#     return jsonify({"message": "Retrait réussi."})

# @app.route('/historique', methods=['GET'])
# def get_historique():
#     return jsonify({"historique": historique_operations})

# if __name__ == '__main__':
#     app.run(debug=True)





# # Données utilisateur (simulation)
# utilisateur = {'nom': 'John Doe', 'solde': 1000}
# historique_transactions = []

# @app.route('/')
# def dashboard():
#     return render_template('dashboard.html', utilisateur=utilisateur, historique_transactions=historique_transactions)

# @app.route('/effectuer_transaction', methods=['POST'])
# def effectuer_transaction():
#     montant = float(request.form.get('montant'))
#     transaction_type = request.form.get('type')

#     # Gérez les transactions en fonction du type (dépôt ou retrait)
#     if transaction_type == 'depot':
#         # Ajoutez le montant au solde
#         utilisateur['solde'] += montant
#         historique_transactions.append(f'Dépôt de {montant} $')
#     elif transaction_type == 'retrait':
#         # Vérifiez si le solde est suffisant pour le retrait
#         if montant <= utilisateur['solde']:
#             # Retirez le montant du solde
#             utilisateur['solde'] -= montant
#             historique_transactions.append(f'Retrait de {montant} $')
#         else:
#             return "Solde insuffisant"

#     return redirect('/')

# @app.route('/accueil')
# @login_required
# def accueil_connecte():
#     # return 'Bienvenue sur la page d\'accueil (Connecté en tant que ' + current_user.nom + ')'
#     render_template("dashboard.html")
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
# =================
# ====================
# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = 'votre_clé_secrète'
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'connexion'

# class Utilisateur(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.String(100))
#     email = db.Column(db.String(100), unique=True)
#     contact = db.Column(db.String(20), unique=True)
#     mot_de_passe = db.Column(db.String(100))

# @login_manager.user_loader
# def load_user(user_id):
#     return Utilisateur.query.get(int(user_id))

# @app.route('/')
# def accueil():
#     return render_template("accueil.html")

# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     if request.method == 'POST':
#         nom = request.form.get('nom')
#         email = request.form.get('email')
#         contact = request.form.get('contact')
#         mot_de_passe = request.form.get('mot_de_passe')

#         # Vérifiez si l'e-mail ou le contact est déjà enregistré
#         existe_email = Utilisateur.query.filter_by(email=email).first()
#         existe_contact = Utilisateur.query.filter_by(contact=contact).first()

#         if existe_email or existe_contact:
#             flash('Cet e-mail ou contact est déjà enregistré.', 'danger')
#             return redirect('/inscription')

#         # Créez un nouvel utilisateur
#         nouvel_utilisateur = Utilisateur(nom=nom, email=email, contact=contact, mot_de_passe=generate_password_hash(mot_de_passe, method='sha256'))

#         # Ajoutez l'utilisateur à la base de données
#         db.session.add(nouvel_utilisateur)
#         db.session.commit()

#         flash('Inscription réussie ! Vous pouvez maintenant vous connecter.', 'success')
#         return redirect('/connexion')

#     return render_template('inscription.html')

# @app.route('/connexion', methods=['GET', 'POST'])
# def connexion():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         mot_de_passe = request.form.get('mot_de_passe')
#         utilisateur = Utilisateur.query.filter_by(email=email).first()

#         if utilisateur and check_password_hash(utilisateur.mot_de_passe, mot_de_passe):
#             login_user(utilisateur)
#             flash('Connexion réussie !', 'success')
#             return redirect('/dashboard')
#         else:
#             flash('Identifiants incorrects. Veuillez réessayer.', 'danger')

#     return render_template('connexion.html')

# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html', utilisateur=current_user)


# @app.route('/deconnexion')
# @login_required
# def deconnexion():
#     logout_user()
#     flash('Déconnexion réussie.', 'success')
#     return redirect('/')

# # ... Autres routes pour d'autres fonctionnalités ...

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)


# ============================
# ))))))))))))))))))))))))
# from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash, check_password_hash



# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = 'votre_clé_secrète'
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'connexion'

# class Utilisateur(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.String(100))
#     email = db.Column(db.String(100), unique=True)
#     contact = db.Column(db.String(20), unique=True)
#     mot_de_passe = db.Column(db.String(100))

# @login_manager.user_loader
# def load_user(user_id):
#     return Utilisateur.query.get(int(user_id))

# @app.route('/')
# def accueil():
#     return render_template("accueil.html")

# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     if request.method == 'POST':
#         nom = request.form.get('nom')
#         email = request.form.get('email')
#         contact = request.form.get('contact')
#         mot_de_passe = request.form.get('mot_de_passe')

#         # Vérifiez si l'e-mail ou le contact est déjà enregistré
#         existe_email = Utilisateur.query.filter_by(email=email).first()
#         existe_contact = Utilisateur.query.filter_by(contact=contact).first()

#         if existe_email or existe_contact:
#             flash('Cet e-mail ou contact est déjà enregistré.', 'danger')
#             return redirect('/inscription')

#         # Créez un nouvel utilisateur
#         nouvel_utilisateur = Utilisateur(nom=nom, email=email, contact=contact, mot_de_passe=generate_password_hash(mot_de_passe, method='sha256'))

#         # Ajoutez l'utilisateur à la base de données
#         db.session.add(nouvel_utilisateur)
#         db.session.commit()

#         flash('Inscription réussie ! Vous pouvez maintenant vous connecter.', 'success')
#         return redirect('/connexion')

#     return render_template('inscription.html')

# @app.route('/connexion', methods=['GET', 'POST'])
# def connexion():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         mot_de_passe = request.form.get('mot_de_passe')
#         utilisateur = Utilisateur.query.filter_by(email=email).first()

#         if utilisateur and check_password_hash(utilisateur.mot_de_passe, mot_de_passe):
#             login_user(utilisateur)
#             flash('Connexion réussie !', 'success')
#             return redirect('/dashboard')
#         else:
#             flash('Identifiants incorrects. Veuillez réessayer.', 'danger')

#     return render_template('connexion.html')

# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html', utilisateur=current_user)

# @app.route('/deconnexion')
# @login_required
# def deconnexion():
#     logout_user()
#     flash('Déconnexion réussie.', 'success')
#     return redirect('/')

# # Simuler un compte bancaire avec un solde initial
# solde_compte = 1000
# historique_operations = []

# # Simuler un compte bancaire avec un solde initial
# solde_compte = 1000
# historique_operations = []

# @app.route('/solde', methods=['GET'])
# def get_solde():
#     return jsonify({"solde": solde_compte})

# @app.route('/transfert', methods=['POST'])
# def transfert():
#     global solde_compte
#     destinataire = request.json.get('destinataire')
#     montant = request.json.get('montant')

#     if montant <= 0:
#         return jsonify({"message": "Le montant doit être positif."}), 400

#     if solde_compte < montant:
#         return jsonify({"message": "Solde insuffisant."}), 400

#     solde_compte -= montant
#     historique_operations.append(f"Transfert de ${montant} vers {destinataire}")
#     return jsonify({"message": "Transfert réussi."})


# @app.route('/retrait', methods=['POST'])
# def retrait():
#     global solde_compte
#     montant = request.json.get('montant')

#     if montant <= 0:
#         return jsonify({"message": "Le montant doit être positif."}), 400

#     if solde_compte < montant:
#         return jsonify({"message": "Solde insuffisant."}), 400

#     solde_compte -= montant
#     historique_operations.append(f"Retrait de ${montant}")
#     return jsonify({"message": "Retrait réussi."})

# @app.route('/historique', methods=['GET'])
# def get_historique():
#     return jsonify({"historique": historique_operations})

# @app.route('/effectuer_transaction', methods=['POST'])
# def effectuer_transaction():
#     montant = float(request.form.get('montant'))
#     transaction_type = request.form.get('type')

#     # Gérez les transactions en fonction du type (dépôt ou retrait)
#     if transaction_type == 'depot':
#         # Ajoutez le montant au solde
#         Utilisateur['solde'] += montant
#         historique_operations.append(f'Dépôt de {montant} F')
#     elif transaction_type == 'retrait':
#         # Vérifiez si le solde est suffisant pour le retrait
#         if montant <= Utilisateur['solde']:
#             # Retirez le montant du solde
#             Utilisateur['solde'] -= montant
#             historique_operations.append(f'Retrait de {montant} $')
#         else:
#             return "Solde insuffisant"

#     return redirect('/')
# if __name__ == '__main__':
#     app.run(debug=True)
# )))))))))))))))))

# from flask_migrate import Migrate
# from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = 'votre_clé_secrète'
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'connexion'
# migrate = Migrate(app, db)

# class Utilisateur(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.String(100))
#     email = db.Column(db.String(100), unique=True)
#     contact = db.Column(db.String(20), unique=True)
#     mot_de_passe = db.Column(db.String(100))
#     solde = db.Column(db.Float, default=0.0)  # Ajout du champ solde

# @login_manager.user_loader
# def load_user(user_id):
#     return Utilisateur.query.get(int(user_id))

# @app.route('/')
# def accueil():
#     return render_template("accueil.html")

# @app.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     if request.method == 'POST':
#         nom = request.form.get('nom')
#         email = request.form.get('email')
#         contact = request.form.get('contact')
#         mot_de_passe = request.form.get('mot_de_passe')

#         # Vérifiez si l'e-mail ou le contact est déjà enregistré
#         existe_email = Utilisateur.query.filter_by(email=email).first()
#         existe_contact = Utilisateur.query.filter_by(contact=contact).first()

#         if existe_email or existe_contact:
#             flash('Cet e-mail ou contact est déjà enregistré.', 'danger')
#             return redirect('/inscription')

#         # Créez un nouvel utilisateur
#         nouvel_utilisateur = Utilisateur(nom=nom, email=email, contact=contact, mot_de_passe=generate_password_hash(mot_de_passe, method='sha256'))

#         # Ajoutez l'utilisateur à la base de données
#         db.session.add(nouvel_utilisateur)
#         db.session.commit()

#         flash('Inscription réussie ! Vous pouvez maintenant vous connecter.', 'success')
#         return redirect('/connexion')

#     return render_template('inscription.html')

# @app.route('/connexion', methods=['GET', 'POST'])
# def connexion():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         mot_de_passe = request.form.get('mot_de_passe')
#         utilisateur = Utilisateur.query.filter_by(email=email).first()

#         if utilisateur and check_password_hash(utilisateur.mot_de_passe, mot_de_passe):
#             login_user(utilisateur)
#             flash('Connexion réussie !', 'success')
#             return redirect('/dashboard')
#         else:
#             flash('Identifiants incorrects. Veuillez réessayer.', 'danger')

#     return render_template('connexion.html')

# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html', utilisateur=current_user)

# @app.route('/deconnexion')
# @login_required
# def deconnexion():
#     logout_user()
#     flash('Déconnexion réussie.', 'success')
#     return redirect('/')

# # Simuler un compte bancaire avec un solde initial
# solde_compte = 1000
# historique_operations = []

# @app.route('/solde', methods=['GET'])
# def get_solde():
#     return jsonify({"solde": current_user.solde})

# @app.route('/transfert', methods=['POST'])
# def transfert():
#     global solde_compte
#     destinataire = request.json.get('destinataire')
#     montant = request.json.get('montant')

#     if montant <= 0:
#         return jsonify({"message": "Le montant doit être positif."}), 400

#     if current_user.solde < montant:
#         return jsonify({"message": "Solde insuffisant."}), 400

#     current_user.solde -= montant
#     historique_operations.append(f"Transfert de ${montant} vers {destinataire}")
#     return jsonify({"message": "Transfert réussi."})

# @app.route('/retrait', methods=['POST'])
# def retrait():
#     global solde_compte
#     montant = request.json.get('montant')

#     if montant <= 0:
#         return jsonify({"message": "Le montant doit être positif."}), 400

#     if current_user.solde < montant:
#         return jsonify({"message": "Solde insuffisant."}), 400

#     current_user.solde -= montant
#     historique_operations.append(f"Retrait de ${montant}")
#     return jsonify({"message": "Retrait réussi."})

# @app.route('/historique', methods=['GET'])
# def get_historique():
#     return jsonify({"historique": historique_operations})

# @app.route('/effectuer_transaction', methods=['POST'])
# def effectuer_transaction():
#     montant = float(request.form.get('montant'))
#     transaction_type = request.form.get('type')

#     # Gérez les transactions en fonction du type (dépôt ou retrait)
#     if transaction_type == 'depot':
#         # Ajoutez le montant au solde
#         current_user.solde += montant
#         historique_operations.append(f'Dépôt de {montant} $')
#     elif transaction_type == 'retrait':
#         # Vérifiez si le solde est suffisant pour le retrait
#         if montant <= current_user.solde:
#             # Retirez le montant du solde
#             current_user.solde -= montant
#             historique_operations.append(f'Retrait de {montant} $')
#         else:
#             return "Solde insuffisant"

#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True)

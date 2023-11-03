
from flask import Flask, render_template, request, redirect, url_for, session
from twilio.rest import Client

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète'

# Configuration de Twilio
TWILIO_SID = 'AC79b8753fd970263172401916cbbfeaef'
TWILIO_AUTH_TOKEN = 'ef7f27efb91527fab22755b9d299223e'
TWILIO_PHONE_NUMBER = '2250150420482'

# Initialisez le client Twilio
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

@app.route('/', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        telephone = request.form['telephone']
        choix_validation = request.form['choix_validation']

        # Générez un code de validation unique (par exemple, un code à 6 chiffres)
        code_validation = '123456'  # Vous pouvez générer un code unique ici

        # Enregistrez l'utilisateur dans la session pour la vérification ultérieure
        session['nom'] = nom
        session['email'] = email
        session['telephone'] = telephone
        session['choix_validation'] = choix_validation
        session['code_validation'] = code_validation

        # Envoyez le code de validation par SMS
        if choix_validation == 'SMS':
            message = client.messages.create(
                to=telephone,
                from_=TWILIO_PHONE_NUMBER,
                body=f'Votre code de validation est : {code_validation}'
            )

        return redirect(url_for('verification'))

    return render_template('inscription.html')

@app.route('/verification', methods=['GET', 'POST'])
def verification():
    if 'code_validation' not in session:
        return redirect(url_for('inscription'))

    if request.method == 'POST':
        code_saisi = request.form['code_verification']
        code_validation = session['code_validation']

        if code_saisi == code_validation:
            # Le code de validation est correct, vous pouvez enregistrer l'utilisateur dans la base de données
            # et rediriger vers une page de confirmation
            return redirect(url_for('confirmation'))

        # Si le code est incorrect, vous pouvez renvoyer l'utilisateur à la page de vérification
        return render_template('verification.html', message='Code incorrect')

    return render_template('verification.html')

@app.route('/confirmation')
def confirmation():
    if 'code_validation' not in session:
        return redirect(url_for('inscription'))

    # Récupérez les données de l'utilisateur depuis la session
    nom = session['nom']
    email = session['email']
    telephone = session['telephone']
    choix_validation = session['choix_validation']

    # Vous pouvez enregistrer l'utilisateur dans la base de données ici

    # Effacez les données de la session
    session.pop('nom', None)
    session.pop('email', None)
    session.pop('telephone', None)
    session.pop('choix_validation', None)
    session.pop('code_validation', None)

    return render_template('confirmation.html', nom=nom, email=email, telephone=telephone, choix_validation=choix_validation)

if __name__ == '__main__':
    app.run(debug=True)

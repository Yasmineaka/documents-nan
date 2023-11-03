# Liste des questions prédéfinies
questions = {
    1: "Quel est votre nom ?",
    2: "Quel est votre âge ?",
    3: "Quel est votre lieu de résidence ?",
    4: "Quel est votre animal préféré ?",
}

# Fonction pour obtenir la réponse en fonction du choix de l'utilisateur
def obtenir_reponse(choix):
    if choix in questions:
        question = questions[choix]
        if choix == 1:
            return f"Votre nom est {input(question)}"
        elif choix == 2:
            return f"Vous avez {input(question)} ans"
        elif choix == 3:
            return f"Vous habitez à {input(question)}"
        elif choix == 4:
            return f"Votre animal préféré est {input(question)}"
    else:
        return "Choix invalide"

# Boucle principale
while True:
    # Afficher les choix possibles
    print("Choisissez une question :")
    for choix, question in questions.items():
        print(f"{choix}. {question}")

    # Demander à l'utilisateur de faire un choix
    choix_utilisateur = int(input("Votre choix : "))

    # Obtenir la réponse en fonction du choix
    reponse = obtenir_reponse(choix_utilisateur)
    print(reponse)

    # Demander à l'utilisateur s'il est satisfait
    satisfaction = input("Êtes-vous satisfait de la réponse ? (oui/non) ")

    if satisfaction.lower() == "oui":
        break
    elif satisfaction.lower() == "non":
        print("Un humain viendra répondre plus tard.")
        break
    else:
        print("Répondez par 'oui' ou 'non'.")

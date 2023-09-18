import sys
import json

chemin = "c:\\Users\\Lenovo\\Desktop\\projet-python\\liste-de-courses-avec-sauvegarades\\liste.json"
with open(chemin, "r") as f:
            donnees = json.load(f)
LISTE = donnees

MENU = """Choisissez parmi les 5 options suivaantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quiter 
👉Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("veuillez choisir une option valide...")

    if user_choice == "1":
        item = input("Entrez le nom d'un élément à ajouter à la liste : ")
        LISTE.append(item)
        with open(chemin, "r") as f:
            donnees = json.load(f)

        donnees.append(item)

        with open(chemin, "w") as f:
            json.dump(donnees, f, indent=4)
        print(f"L'élément {item} a bien était ajouté à la liste.")
    elif user_choice == "2":
        item = input(
            "Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été suprimmé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif user_choice == "3":
        if LISTE:
            print("Voici le contenu de votre liste: ")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("votre liste ne contient aucun élément.")
    elif user_choice == "4":
        LISTE.clear()
        print("La liste a été vidée de son contenu")

    elif user_choice == "5":
        with open(chemin, "w") as f:
            json.dump(LISTE, f, indent=4, ensure_ascii= False)
        print("à bientot !")
        sys.exit()

    print("_" * 50)

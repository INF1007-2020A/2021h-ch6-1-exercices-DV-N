#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        max_values_collected = 1
        while len(values) < max_values_collected:
            entree = [input("Entrer une valeur ici :\n")]
            values.append(entree) # can be optimized with  values.append((input("Entrer une valeur ici :\n"))
    return sorted(values) # ou list.sort


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = []
        while len(words) < 2:                   #Lister min 2 mots
            words.append(input("Veuillez entrer un mot : "))

        return sorted(words[0]) == sorted(words[1]) #Erreur : pas besoin de if, return True/False pcq == inclus un bool


       # solution avec covnersion ASCII qui n'a pas fonctionnée
        '''words = []
        while len(words) < 2:
            words.append(input("Veuillez entrer un mot en majusucules : ")) # ajouter .capitalize
        if words[0].encode() == words[1].encode():
            return True
        return False
        '''

def contains_doubles(items: list) -> bool:
    return len(items) != len(set(items))        # != càd contient doublons
    # Alternative : return list(set(items)) != sorted(items)  # retourne liste == liste


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = {}
    past_avg = 0
    for key, values in student_grades.items():
        student_avg = sum(values)/len(values)

        if student_avg > past_avg:
            best_student = {key : student_avg}
            past_avg = student_avg
        else:
            continue

    return best_student

def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Meredith" : [90, 90, 90], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()

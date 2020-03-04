if __name__ == '__main__':
    #declaration de codage de caractère, utiliser souvent le UTF-8,
    # pour prendre en charge toutes du muliligue
    print ( "salam alaykom")
    print (u"السلام عليكم")
    #declaration des variables
    # pas de déclaration explicite
    # il suffit d'affecter une valeur pour spécifier le type d'une variable
    age = 125 # entier
    print("type de age", type(age))
    salaire = 3.14
    print("type de salaire", type(salaire))
    name = "Ahmed"
    print("type de name", type(name))
    #substitution
    s2 = "I am %s "%name
    s3 = "I am %d old"%age
    print(s2,s3)
    #listes
    liste = [1,2,31,4]
    print("type de ls:", type(liste))
    print(liste)
    #ajouter un element
    liste.append(5)
    print(liste)
    #liste des mots
    wordlist = ["I", "am","learning","english"]
    #structure de controle
    a = 15
    if a>15:
       #attention aux tabulations
        print('a supérieur à 15')
    elif a<=15 and a>=10:
        print('a entre 10 et 15')
    else:
        print('a est intfieur à 10')
    #tester si un elment appartient a une liste
    a = 5
    if a in liste:
     print('a existe dans la liste')

    #les boucles
    for word in wordlist:
        print(word)
    #boucles et tests
    #calculer le nombre d'ocuurence d'un caractère dans une chaine de caractère
    chaine = "Le TAL est l’ensemble des méthodes et des programmes qui permettent"
    caractere = "e"
    cpt = 0
    for c in chaine:
        if c == caractere:
            cpt += 1
    print("le caractere %s existe %d fois"%(caractere,cpt))
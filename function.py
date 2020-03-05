
def choice_perso():
    choice = ["", ""]
    choice_flip = ["", ""]
    print("Joueur 1, choisissez votre personnage,\nsi vous ne connaissez pas la liste des personnages, mettez \"liste\"\n")
    
    verif = False
    while verif == False:
        j1 = input("...")
        if j1.lower() == "liste":
            print("- Sakuya\n- Papacito")

        elif j1.lower() == "sakuya":
            choice[0] = "/images/sakuya.png"
            choice_flip[0] = "/images/sakuya_flip.png"
            verif = True

        elif j1.lower() == "papacito":
            choice[0] = "/images/papacito.png"
            choice_flip[0] = "/images/papacito_flip.png"
            verif = True

        else:
            print("Je n'ai pas bien compris, veuillez remettre le nom de votre personnage.")
    

    print("Joueur 2, choisissez votre personnage,\nsi vous ne connaissez pas la liste des personnages, mettez \"liste\"\n")
    
    verif = False
    while verif == False:
        j2 = input("...")
        if j2.lower() == "liste":
            print("- Sakuya\n- Papacito")

        if j2.lower() == "sakuya":
            choice[1] = "/images/sakuya.png"
            choice_flip[1] = "/images/sakuya_flip.png"
            verif = True

        elif j2.lower() == "papacito":
            choice[1] = "/images/papacito.png"
            choice_flip[1] = "/images/papacito_flip.png"
            verif = True

        else:
            print("Je n'ai pas bien compris, veuillez remettre le nom de votre personnage.")

    full_choice = [choice, choice_flip]
    return full_choice

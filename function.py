
def choice_perso():
    choice = ["", ""]
    choice_flip = ["", ""]
    print("Joueur 1, choisissez votre personnage,\nsi vous ne connaissez pas la liste des personnages, mettez \"liste\"\n")
    
    verif = False
    while verif == False:
        j1 = input("...")
        if j1.lower() == "liste":
            print("- Sakuya\n- Papacito\n- Nathan")

        elif j1.lower() == "sakuya":
            choice[0] = "/images/Sakuya.png"
            choice_flip[0] = "/images/Sakuya_flip.png"
            verif = True

        elif j1.lower() == "papacito":
            choice[0] = "/images/papacito.png"
            choice_flip[0] = "/images/papacito_flip.png"
            verif = True
        
        elif j1.lower() == "nathan":
            choice[0] = "/images/nathan.png"
            choice_flip[0] = "/images/nathan_flip.png"
            verif = True

        else:
            print("Je n'ai pas bien compris, veuillez remettre le nom de votre personnage.")
    

    print("Joueur 2, choisissez votre personnage,\nsi vous ne connaissez pas la liste des personnages, mettez \"liste\"\n")
    
    verif = False
    while verif == False:
        j2 = input("...")
        if j2.lower() == "liste":
            print("- Sakuya\n- Papacito\n- Nathan")

        if j2.lower() == "sakuya":
            choice[1] = "/images/Sakuya.png"
            choice_flip[1] = "/images/Sakuya_flip.png"
            verif = True

        elif j2.lower() == "papacito":
            choice[1] = "/images/papacito.png"
            choice_flip[1] = "/images/papacito_flip.png"
            verif = True
        
        elif j2.lower() == "nathan":
            choice[1] = "/images/nathan.png"
            choice_flip[1] = "/images/nathan_flip.png"
            verif = True

        else:
            print("Je n'ai pas bien compris, veuillez remettre le nom de votre personnage.")

    full_choice = [choice, choice_flip]
    return full_choice
"""
def menu(validation):
    print("affichage du menu")
    if validation is True:
        game = True
        while game:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    game = False
                elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            if event.pos[0] >= 700 and event.pos[0] <= 800 and event.pos[1] >= 800 and event.pos[1] <= 850: #rect player1 ; 0 pour x et 1 pour y 
                                print("BOUTON 1")
                            elif event.pos[0] >= 900 and event.pos[0] <= 1000 and event.pos[1] >= 800 and event.pos[1] <= 850: #rect player2
                                print("BOUTON 2")
                            elif event.pos[0] >= 1100 and event.pos[0] <= 1200 and event.pos[1] >= 800 and event.pos[1] <= 850:#rect player3
                                print("BOUTON 3")
                            elif event.pos[0] >= 700 and event.pos[0] <= 800 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                                print("BOUTON 4")
                            elif event.pos[0] >= 900 and event.pos[0] <= 1000 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                                print("BOUTON 5")
                            elif event.pos[0] >= 1100 and event.pos[0] <= 1200 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                                print("BOUTON 6")

    else: 
        print("ne fonctionne pas")"""
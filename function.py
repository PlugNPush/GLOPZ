
def choice_perso():
    choice = ["", ""]
    choice_flip = ["", ""]
    #print("Joueur 1, choisissez votre personnage,\nsi vous ne connaissez pas la liste des personnages, mettez \"liste\"\n")
    #
    #verif = False
    #while verif == False:
    #    j1 = input("...")
    #    if j1.lower() == "liste":
    #        print("- Sakuya\n- Papacito\n- Nathan")
#
    #    elif j1.lower() == "sakuya":
    #        choice[0] = "/images/Sakuya.png"
    #        choice_flip[0] = "/images/Sakuya_flip.png"
    #        verif = True
#
    #    elif j1.lower() == "papacito":
    #        choice[0] = "/images/papacito.png"
    #        choice_flip[0] = "/images/papacito_flip.png"
    #        verif = True
    #    
    #    elif j1.lower() == "nathan":
    #        choice[0] = "/images/nathan.png"
    #        choice_flip[0] = "/images/nathan_flip.png"
    #        verif = True
#
    #    else:
    #        print("Je n'ai pas bien compris, veuillez remettre le nom de votre personnage.")
    #
#
    #print("Joueur 2, choisissez votre personnage,\nsi vous ne connaissez pas la liste des personnages, mettez \"liste\"\n")
    #
    #verif = False
    #while verif == False:
    #    j2 = input("...")
    #    if j2.lower() == "liste":
    #        print("- Sakuya\n- Papacito\n- Nathan")
#
    #    if j2.lower() == "sakuya":
    #        choice[1] = "/images/Sakuya.png"
    #        choice_flip[1] = "/images/Sakuya_flip.png"
    #        verif = True
#
    #    elif j2.lower() == "papacito":
    #        choice[1] = "/images/papacito.png"
    #        choice_flip[1] = "/images/papacito_flip.png"
    #        verif = True
    #    
    #    elif j2.lower() == "nathan":
    #        choice[1] = "/images/nathan.png"
    #        choice_flip[1] = "/images/nathan_flip.png"
    #        verif = True
#
    #    else:
    #        print("Je n'ai pas bien compris, veuillez remettre le nom de votre personnage.")
#
    full_choice = [choice, choice_flip]
    return full_choice

def niveau_vie(posJ1, projectile, niveau_vie):

    if niveau_vie == 100 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            screen.blit(hp_90, pos_hp)
    else if niveau_vie == 90 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            screen.blit(hp_80, pos_hp)
    else if niveau_vie == 80 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            screen.blit(hp_70, pos_hp)
    else if niveau_vie == 70 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            screen.blit(hp_60, pos_hp)
    else if niveau_vie == 60 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            screen.blit(hp_50, pos_hp)
    else if niveau_vie == 50 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            screen.blit(hp_40, pos_hp)
    else if niveau_vie == 40 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            screen.blit(hp_30, pos_hp)
    else if niveau_vie == 30 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            screen.blit(hp_20, pos_hp)
    else if niveau_vie == 20 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            screen.blit(hp_10, pos_hp)
    else if niveau_vie == 10 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            screen.blit(hp_0, pos_hp)
    else if niveau_vie == 0 and hit == 1:
        if projectile.x == pos_j1.x or projectile.y == pos_j1.y:
            game = False
            """affichage ecran victoire"""
    


            

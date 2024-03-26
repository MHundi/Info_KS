# Funktionsbibliothek

def eingabe():
    a=input ("Bitte gib deine Punktzahl ein: ")
    a = int(a)
    return a

def ausgabe(s):
    print("Du hast", s , "erreicht.")
    
def umrechnung(b):
    if b == 0:
        c = "ungenügend"
    elif 0 <b < 4:
        c="mangelhaft"
    elif 3 <b< 7:
        c="ausreichend"
    elif 6< b < 10:
        c="befriedigend"
    elif 9< b < 13:
        c="gut"
    elif 12< b < 15:
        c="sehr gut"
    else:
        c="hervorragend"
    return c

        
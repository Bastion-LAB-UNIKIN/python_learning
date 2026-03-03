#fonction

f = lambda x,y:x**2 + y

def e_potentielle(masse,hauteur,g=9.81):
    E = masse * hauteur * g
    return E

resultat=e_potentielle(masse=80, hauteur=5)

print(resultat,"joule")

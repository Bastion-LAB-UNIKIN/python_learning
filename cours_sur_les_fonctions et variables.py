x = 1
y = 2.5

print(x+y)
print(x-y)
print(x*y)
print(x/y)

print(x<=y)
print(x>=y)
print(x==y)
print(x!=y)

def ep(masse,hauteur,g=9.81):
     E = masse * hauteur * g
     print(E,'Joules')
     return E
ep(10,10)

def ep_ee(masse,hauteur,ee,g=9.81):
     E= masse * hauteur * g
     return E < ee
ep_ee(100, 100, 1500)

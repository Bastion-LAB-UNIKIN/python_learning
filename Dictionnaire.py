inventaire = {
    "oranges":1000,
    "mangues":2000,
    "avocats":3000
}
print(inventaire)
print(inventaire.values())
print(len(inventaire))
print(inventaire.keys())
inventaire["pommes"]=1500
print(inventaire)
print(inventaire.get("ananas",10))
print(inventaire.get("avocats",10))
grignotage=("bonbon","biscuit","chips")
print(inventaire.fromkeys(grignotage,10))
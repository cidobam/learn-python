"""
d = {}
for x in [1, 2, 2, 3]:
    d[x] = d.get(x, 0) + 1
print(d)


a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

x = int(input("Please enter an integer: "))

if x<0:
    print("x is negative")
elif x==0:
    print("x is zero")
else:
    print("x is positive")



users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

kullanici = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Create a new collection
active_users = {}
for user, status in kullanici.items():
    if status == 'active':
        active_users[user] = status

print(active_users)



d = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for k in d:
    print(k)

for z in d.keys():
    print(z)

for v in d.values():
    print(v)

for i, s in d.items():
    print(i)





m = {"a": 1}
view = m.items()
m["b"] = 2
print(list(view)) 

# to modify an item in a collection while you are itrating is challenging. you have to be careful.
# for that there are 2 strategies:
# Strategy 1 : create a copy of the collection. loop over the copy and modify the original:

aile = {"Baba": "Soner", "Anne" : "Berna", "Büyük Kardeş" :  "Elif" , "Küçük Kardeş" : "Halil"}
for k, v in aile.copy().items():
    if v == "Elif":
        aile["Abla"] = aile.pop(k)
print(aile)

"""

#Strategy 2: create new collection
only_girls={}
ailem = {"Baba": "Soner", "Anne": "Berna", "Büyük Kardeş":  "Elif" , "Küçük Kardeş": "Halil"}
for c , g in ailem.items():
    if g in ("Berna" , "Elif"):
        only_girls[c]=g
print(only_girls)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

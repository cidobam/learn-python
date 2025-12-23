
#d = {"a": 1}    	  dict key -> value pairs
#s = {1,2}	

d = {}
for x in [1, 2, 2, 3]:
    d[x] = d.get(x, 0) + 1
print(d)
#this function overwrites the value of the key if it already exists. if not, it assigns the default value (0 here) and adds 1 to it.

#While loop: Executes as long as the condition remains true.
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
# this is a fibonacci sequence generator.
#a,b = b, a+b is a tuple unpacking assignment. it assigns the value of b to a and the value of a+b to b simultaneously.

#If-elif-else statement: Conditional execution of code blocks.
#int() function converts a string or number to an integer. 
#input() function is when you want to take input from the user.
#The string inside the input function is a prompt that is displayed to the user.
#The input function always returns a string, so we use int() to convert it to an integer.


x = int(input("Please enter an integer: "))

if x<0:
    print("x is negative")
elif x==0:
    print("x is zero")
else:
    print("x is positive")

#When you want to modify a dictionary, you can iterate over it.
#Strategy 1: Iterate over a copy
#copy() method creates a shallow copy of the dictionary.
#items() method returns the left side (keys)


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}


for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)



#When you want to modify a dictionary, you can create a new collection with wanted items.
# Strategy 2:  Create a new collection


kullanici = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
active_users = {}
for user, status in kullanici.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

# Iterating over dictionary keys, values, and items
#for k in d: print(k) returns the keys of the dictionary
#for z in d.keys(): print(z) returns the keys of the dictionary
#for v in d.values(): print(v) returns the values of the dictionary
#for i, s in d.items(): print(i) returns the keys of the dictionary

d = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for k in d:
    print(k)

for z in d.keys():
    print(z)

for v in d.values():
    print(v)

for i, s in d.items():
    print(i)

#Dictionary views reflect changes to the dictionary.
#When you create a view object, it reflects the current state of the dictionary.
#If the dictionary changes, the view reflects these changes.    

m = {"a": 1}
view = m.items()
m["b"] = 2
print(list(view)) 
#>>[('a', 1), ('b', 2)]


#Here, if the value is "Elif", I want to change the key to "Sister" instead of "Older Sister".
#pop() method removes the specified key and returns the corresponding value.


family = {"Father": "Soner", "Mother" : "Berna", "Older Sister" :  "Elif" , "Younger Brother" : "Halil"}
for k, v in family.copy().items():
    if v == "Elif":
        family["Sister"] = family.pop(k)
print(family)



#Create a new collection that only contains the girls in the family.

only_girls={}
family = {"Father": "Soner", "Mother" : "Berna", "Older Sister" :  "Elif" , "Younger Brother" : "Halil"}
for c , g in family.items():
    if g in ("Berna" , "Elif"):
        only_girls[c]=g
print(only_girls)

# Example of using range() to iterate over indices of a list 

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
    print(i+1, a[i])

   

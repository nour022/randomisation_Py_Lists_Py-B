 # random is a lib of rand() this giving a Random number von bis
import random
# is spicel in integer Number 
random_intager=random.randint(1,100)
print(random_intager)
# is spicel in float Number 
random_float=random.random()+random.randint(1,100)
print(random_float)

#Ex1 
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num=names[random.randint(0,(len(names)-1))]
print(f"{num} is going to buy the meal today!")


#Ex2 
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
num= position
map[int(num[1])-1][int(num[0])-1]="X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#----------------------------------

# python list Array
laender = ['Deutschland', 'USA', 'China', 'Russland', 'Frankreich', 'Japan', 'Indien', 'Kanada', 'Brasilien', 'Australien', 'Mexiko', 'Indonesien', 'Türkei', 'Südafrika', 'Südkorea', 'Nigeria', 'Ägypten', 'Argentinien', 'Thailand', 'Kolumbien', 'Saudi-Arabien', 'Iran', 'Pakistan', 'Spanien', 'Italien']

print(laender[0])
# print(laender[::-1])
# print(laender[0:3])
# print(laender[0::2]) # even item

# append() : to create a item
laender.append("Syria")
print(laender[(len(laender)-2):(len(laender))])

# extend() : verbeinden eine neue schleife mit der andere
laender.extend(['nour', 'gaser', 'mo'])
print(laender[(len(laender)-4):(len(laender))])
# remove() pop() clear() index() count() sort()

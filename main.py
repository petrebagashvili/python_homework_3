# სავარჯიშო 1

loop = True
while loop:
    chosen = input("შემოიტანე ასო: ")
    letters = "აეიოუ"
    georgian_letters = "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
    if chosen not in letters:
        print("შემოიტანე ხმოვანი ან თანხმოვანი!")
    elif chosen in letters:
        print(f"შემოტანილი ასო ხმოვანია და არის {chosen}")
    else:
        print(f"შემოტანილი ასო თახმოვანია და არის {chosen}")
    stop = input("გსურს თუ არა დასრულება :(კი,არა)").lower()
    if stop == "კი" or stop == "yes":
        loop = False
    elif stop == "no" or stop == "არა":
        loop = True

# სავარჯიშო 2

for i in range(10,1,-1):
    print(i)

# სავარჯიშო 3

import random
lst = [random.randint(1,20) for _ in range(10)]
print(lst)
sorted_list = sorted(lst)
print(sorted_list)
print(f"first place: {sorted_list[-1]}")
print(f"second place: {sorted_list[-2]}")
print(f"third place: {sorted_list[-3]}")

# სავარჯიშო 4

width = input("შეიყვანე სიგანე:")
height = input("შეიყვანე სიმაღლე:")
if not width.isdigit():
    print("შეიყვანე რიცხვი!")
elif not height.isdigit():
    print("შეიყვანე რიცხვი!")
elif int(width) <= 0 :
    print("შეიყვანე დადებითი რიცხვი")
elif int(height) <= 0:
    print("შეიყვანე დადებითი რიცხვი")
else:
    width = int(width)
    height = int(height)
    for i in range(height):
        for j in range(width):
            print("#", end=" ")
        print()
# სავარჯიშო 5

class Operations:
    def times(self,a,b):
        return a**b
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def division(self,a,b):
        return a/b
    def double_division (self,a,b):
        return a//b
    def percent_division(self,a,b):
        return a%b
    def multiplication(self,a,b):
        return a*b

operations = Operations()
print(operations.times(5,2))
print(operations.addition(5,2))
print(operations.subtraction(5,2))
print(operations.division(5,2))
print(operations.double_division(5,2))
print(operations.percent_division(5,2))

# სავარჯიშო 6
def square(width,height):
    if width <= 0 :
        print("შეიყვანე დადებითი რიცხვი")
    elif height <= 0:
        print("შეიყვანე დადებითი რიცხვი")
    else:
        for i in range(height):
            for j in range(width):
                print("#", end=" ")
            print()
square(10,10)

# სავარჯიშო 7

def char_count(text,char):
    count = 0
    for a in text:
        if a.lower() == char.lower():
            count += 1

    print(f'Character "{char}" in given string: {count} times')

# სავარჯიშო 8

def word_count(text):
    count = 0
    words = text.split()
    count = len(words)
    print(f'Words "{words}" in given string: {count} times')

# სავარჯიშო 9

words = ["python", "georgia", "computer", "school", "programming"]

secret_word = random.choice(words)
attempts = 10

print("გამოიცანი სიტყვა! (დაწერე ასო ან სრული სიტყვა)")
print("თამაშის გასათიშად დაწერე: exit")

while attempts > 0:
    guess = input("შენი მცდელობა: ")

    if guess == "exit":
        print("თამაში დასრულდა")
        break

    if guess == secret_word:
        print("გილოცავ ")
        break

    attempts -= 1

    print(f"არასწორია! დარჩენილი ცდები: {attempts}")

else:
    print("თქვენ დამარცხდით ")


# სავარჯიშო 10

import random

choices = ["მარჯვენა", "მარცხენა"]

correct_choice = random.choice(choices)

attempts = 5
correct_answers = 0

print("აირჩიე: 'მარჯვენა' ან 'მარცხენა'")
print("თამაშის გასათიშად დაწერე: exit")

for i in range(attempts):

    user = input(f"{i+1} მცდელობა: ")

    if user == "exit":
        print("თამაში დასრულდა")
        break

    if user == correct_choice:
        print("სწორია ")
        correct_answers += 1
    else:
        print("არასწორია ")

else:
    if correct_answers == 5:
        print("გამარჯვება ")
    else:
        print("შენ დამარცხდი ")
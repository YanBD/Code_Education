import random as r

print('Welcome to the Guessing Game')
print('Enter -1 to generate a new number')
print('Enter 0 to end at any point ')
x = r.randint(1, 100)
a = int(input('Pick a number between 1 - 100: '))
print(x)

while a != x:
    if a == -1:
        print('New random number will be generated')
        x = r.randint(1, 100)
        a = int(input('Pick a number between 1 - 100: '))
        print(x)
    if a >= 100 or a <= -2:
        print('Number is outside the range of 1 - 100')
        a = int(input('Pick a number between 1 - 100: '))
        print()
    if a < x:
        print('Your guess is less than the number')
        a = int(input('Pick a number between 1 - 100: '))
        print()
    if a > x:
        print('Your guess is higher than the number')
        a = int(input('Pick a number between 1 - 100: '))
        print()
    if a == x:
        print('Congrats on guessing the correct number')
        print('Enter 0 to end game or -1 to generate new number:')
        a = int(input('Please enter 0 or -1: '))
        print()
    if a == 0:
        print("Thanks for playing the game")
        break
    continue

# if a == x:
#     print('Congrats on guessing the correct number')
# if a < x:
#     print('Your guess is less than the number')
# if a > x:
#     print('Your guess is higher than the number')

import random
import math

play = 'Y'
start = 1
end = 100
direction = 'N'
smallest = start
largest = end


while play == 'Y':
    smallest = start
    largest = end
    print('Guess a number between 1 and 100: ')
    number = random.randint(start, end)
    print(number)
    counter = 0
    direction = 'N'
    smaller = (number < direction)
    larger = (number > direction)
    correct = (number == direction)

    while direction != 'C':
        direction = input('Is the number is too large, too small, or correct?: ')
        if direction == smaller:
            if number > smallest:
                smallest = number + 1
            number = random.randint(smallest, largest)
            print(number)
        if direction == larger:
            if number > largest:
                smallest = number - 1
            number = random.randint(smallest, largest)
            print(number)
        counter = counter + 1
    print("Sweet! I got it in", str(counter),"tries!")
    

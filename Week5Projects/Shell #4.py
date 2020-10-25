numbers = []
print("enter key to stop")
while(True):
    num = input("enter a number :")
    if num:
        numbers.append(int(num))
    elif(num == ''):
            break
add = 0
for num in numbers:
    add += num
avg = add / len(numbers)
print("The nummbers entered add to be", add)
print("The average is", avg)

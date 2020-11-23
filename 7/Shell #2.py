filename = input('Enter file name: ')
with open(filename,'r') as file:   
   numbers = []
   for line in file:
         numbers.append(line.strip())
print('The number of lines in the file is:', len(numbers))

while True:
   num = int(input('Enter line number: '))
   if num == 0:
       break
   else:
       x = num - 1
       print(numbers[num])
       break

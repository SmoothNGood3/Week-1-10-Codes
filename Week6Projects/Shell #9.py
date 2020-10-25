inputFileName = input("Please enter a filename: ")
file = open(inputFileName, 'r')
outputFileName = input("Output filename: ")

inputFile = open(inputFileName, 'r')  
outputFile = open(outputFileName, 'w')  

count = 1  
for line in inputFile:
    newLine = str(count).rjust(4, " ") + "> " + line
    outputFile.write(newLine) 
    print(newLine)
    count += 1

inputFile.close()
outputFile.close()

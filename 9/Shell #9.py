def main():
    fileName = input("Enter filename:")
    file = open(fileName, "r")
    
    inf = file.read().split()
    
    numb = []
    for line in inf:
        numb.append(int(line))
    file.close()
    
    average = float(sum(numb))/len(numb)
    print("The average is",average)
main()

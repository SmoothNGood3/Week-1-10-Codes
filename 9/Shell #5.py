def isSorted(numb):
     if len(numb) >= 0 and len(numb) < 2:
          return True
     else:        
          for i in range(len(numb)-1):
               if numb[i] > numb[i+1]:
                    return False
          return True

def main():
     numb = [100]
     print(isSorted(numb))
     numb = [11]
     print(isSorted(numb))   
     numb = [7]   
     print(isSorted(numb))
     numb = [3]  
     print(isSorted(numb))

main()

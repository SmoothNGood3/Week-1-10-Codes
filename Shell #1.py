
def median(list):
    if not list:
        return 0
    median = sorted(list.copy())
    if len(median) % 2 == 1:
        return median[int(len(median) / 2)]
    else:
        return (median[int(len(median) / 2)] + median[int(len(median) / 2) - 1]) / 2

def mean(list):
    if not list:
        return 0
    Sum = sum(list)
    return Sum / len(list)

def mode(list):
    if not list:
        return 0
    result = list[0]
    count = 0
    for number in list:
        if list.count(number) > count:
            result = number
        return result

def main():
    math = list(map(int, input("Enter a list of numbers: ").strip().split()))
    print("The Median is", median(math))
    print("The Mean is", mean(math))
    print("The Mode is", mode(math))

main()

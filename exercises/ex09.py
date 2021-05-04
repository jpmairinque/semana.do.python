print("Given the number (n), populate an array with all numbers up to and including that number, but excluding zero. ")

def monkey_count(n):
    arr = []
    for item in range(1,n+1):
        arr.append(item)
    
    return arr

print(monkey_count(5))
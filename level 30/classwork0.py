

def filter_odd(numbers):
    return [num for num in numbers if num % 2 == 0]

result = filter_odd([1,2,3,4,5,6,7,8,9,10])
print(result)  

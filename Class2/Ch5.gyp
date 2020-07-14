largest = None
smallest = None
while True:
    
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = float(num)
    except:
        print('Invalid Input')
        continue

    if largest is None:
        largest = num
        smallest = num
        continue

    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print("Maximum", largest)
print("Minimum", smallest)
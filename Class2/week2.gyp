try:
    scores = float(input("Enter Grade: "))
except :
    scores = -1
if scores < 0:
    grade = 'Invalid Entry'
elif scores >= 0.9: 
        grade = 'A'
elif scores  >= 0.8: 
        grade = 'B'
elif scores  >= 0.7: 
        grade = 'C'
elif scores  >= 0.6: 
        grade = 'D'
elif scores < 0.6:
        grade = 'F'

print(grade)
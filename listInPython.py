marks = [84, 96, 86, 33, 22, 42]
print(marks[1:3])

for score in marks:
    if score ==33:
        break;
    print(score)

print(" ==================  ") 
    
for score in marks:
    if score == 86:
        continue
    print(score)
    
marks = [41, 42, 43, 44, 45]
def addOneMark(mark):
    return mark+1

new_Marks = list(map(addOneMark, marks))
print(new_Marks)
liste=[1,2,3,1]
liste.extend(liste)

print(liste)

with open('names.txt', 'r+') as file:
    file.truncate(20)
    lines = file.readlines()
    
print(lines)


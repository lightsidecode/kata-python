# Posortowac wyrazy z napisu alfabetycznie oraz pod wzgledem dlugosci.

line = "Entliczek petliczek co zrobi Piechniczek..."

words = line.split()
print(words)

words.sort(key=len) # sort by len
print(words)

words.sort(key=str.lower) # sort by abc
print(words)

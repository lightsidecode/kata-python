# Zbudowac napis skladajacy sie z pierwszych/ostatnich znakow wszysthich slow 
# umieszczonych w zmiennej.

line = "I am Bond, James Bond"

words = line.split()

first_letters = "".join(x[0] for x in words)
last_letters = "".join(x[-1] for x in words)

print(first_letters)
print(last_letters)

# Lista zawiera liczby 1, 2 i 3 cyfrowe. Zbuduj napis z trzycyfrowych 
# blokow z listy. Braki w liczbach uzupelnij zerami np. 1 = 001, 
# 23 = 023, 481 = 481 itd.

L = [1, 2, 23, 43, 8, 100, 99, 7, 481]

print ("".join(str(x).zfill(3) for x in L))

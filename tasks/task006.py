# Wyszukac najdluzszy wyraz oraz dlugosc najdluzszego wyrazu w napisie.

line = "Zawze cos sie dzieje, nie ma zwyklych chwil..."

max_word = max(line.split(), key=len)

print("Nadluzszy napis: {}".format(max_word))
print("Najdluszy napis ma dlugosc: {}".format(len(max_word)))
# Obliczyc laczna dlugosc wyrazow w napisie.

line = "I am Bond, James Bond!"

words = line.split()

size = sum(map(lambda word: len(word), words))

print(size)

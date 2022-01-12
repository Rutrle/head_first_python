data = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)
print(evens)

evens_comp = [x for x in data if not x % 2]
print(evens_comp)

data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)
print(words)

words_comp = [x for x in data if isinstance(x, str)]
print(words_comp)

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())

title_comp = [word.title() for word in data]
print(title, title_comp)

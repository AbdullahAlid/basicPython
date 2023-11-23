sentence = "This is a common inter view question"
sentence = sentence.lower()
dictionary = {x: sentence.count(x) for x in sentence}
print(dictionary)

print(sorted(dictionary))

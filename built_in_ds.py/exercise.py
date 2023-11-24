# Find the most repeated character in this text
original_sentence = "This is a common interview question"
sentence = original_sentence.lower()
# print(sentence)

occ_set = set()
for i in sentence:
    occ_set.add((i, sentence.count(i)))


distinct_occurrance = list(occ_set)
# print(type(distinct_occurrance))

distinct_occurrance.sort(key=lambda item: item[1], reverse=True)
# print(distinct_occurrance)


print(list(
    filter(lambda item: item[1] == distinct_occurrance[0][1], distinct_occurrance)))

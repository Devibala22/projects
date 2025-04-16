sentence="the sky is blue and the grass is green"
words=sentence.split()
duplicates={word for word in words if words if words.count(word)>1}
print("Duplicate words:",duplicates)

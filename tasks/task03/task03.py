import string
texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]
res = {}
for ind, sentence in enumerate(texts):
    words = [word.strip(string.punctuation).lower() for word in sentence.split()]
    for word in words:
        if word not in res:
            res[word] = [1, ind]
        else:
            res[word][0] += 1
print("%-10s%-10s%-10s" % ("word", "count", "first line"))
for word, values in res.items():
    count, first_line = values
    print("%-10s%-10d%-10d" % (word, count, first_line))

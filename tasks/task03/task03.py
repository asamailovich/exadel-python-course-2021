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
for i in res.items():
    print("%-10s%-10d%-10d" % (i[0], i[1][0], i[1][1]))

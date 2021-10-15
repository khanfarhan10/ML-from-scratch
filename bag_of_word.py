from collections import defaultdict

corpus = ["good boy boy","good girl","boy girl good"]



"""
1. make a set of all the unique words  [good, boy, girl]
2. do count of each element of unique words in each sentances
    [1,2,0]
    [1,1,0]
    [1,1,1]

"""


# 1. unique words
unique_words = sorted(set(j for i in corpus for j in i.split(" ")))

# 2. do count for each word
temp1 = []
for cnt in range(len(corpus)):
    temp = []
    for i in unique_words:
        if i in corpus[cnt].split(" "):
            temp.append(corpus[cnt].split(" ").count(i))
        else:
            temp.append(0)
    temp1.append(temp)


print(temp1)





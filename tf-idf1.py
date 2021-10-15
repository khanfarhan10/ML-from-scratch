from collections import defaultdict
import math

corpus = ["good boy","good girl","boy girl good"]



# 1. unique words
unique_words = sorted(set(j for i in corpus for j in i.split(" ")))

# 2. do count for each word
# [[2, 0, 1], [0, 1, 1], [1, 1, 1]]
temp1 = []
for cnt in range(len(corpus)):
    temp = []
    for i in unique_words:
        if i in corpus[cnt].split(" "):
            temp.append(corpus[cnt].split(" ").count(i))
        else:
            temp.append(0)
    temp1.append(temp)


# crete tf matrix
tf = []
for i in range(len(temp1)):
    length = len(corpus[i].split(" "))
    tf_row = []
    for cnt in temp1[i]:
        tf_row.append(cnt/length)
    tf.append(tf_row)

# crete idf matrix
idf = []
sentance_len = len(corpus)
for i in unique_words:
    cnt = 0
    for j in corpus:
        temp = j.split(" ")
        if i in temp:
            cnt+=1

    idf.append(math.log(sentance_len/cnt))

# [[0.5, 0.0, 0.5],
# [0.0, 0.5, 0.5],
# [0.33, 0.33, 0.33]]

# do transpost of the tf matrix
def transpose(l1, l2):
    for i in range(len(l1[0])):
        row =[]
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2
tf_t = []
tf = transpose(tf,tf_t)

# calculate tf-idf matrix
tf_idf = []
row = 0
for i in range(len(tf)):
    temp = []
    for j in range(len(tf[i])):
        temp.append(tf[i][j] * idf[row])
    row+=1
    tf_idf.append(temp)

print(tf_idf)

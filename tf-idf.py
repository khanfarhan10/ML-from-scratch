
from collections import defaultdict


corpus = ["good boy","good girl","boy girl good"]
unique_words = set(j for i in corpus for j in i.split(" "))
sentance_len = len(corpus)
unique_words_len = len(unique_words)

def init_dict(unq_word_count):
    for val in unique_words:
        unq_word_count[val]=0


unq_word_count = {}
for val in unique_words:
    unq_word_count[val]=0

tf = []

for i in corpus:
    for j in i.split(" "):
        unq_word_count[j] += 1

cnt_wrd_by_snt = []
# for i in corpus:
#     temp = defaultdict(int)
#     for j in i.split(" "):
#         temp[j] += 1
#     cnt_wrd_by_snt.append(temp)
for i in range(len(corpus)):
    for j in unique_words:
        # temp = {}
        # for val in unique_words:
        #     temp[val]=0
        temp = [0]*len(unique_words)
        if j in corpus[i].split(" "):
            temp.append(corpus[i].split(" ").count(j))

    cnt_wrd_by_snt.append(temp)

print(cnt_wrd_by_snt)
# wrd = ["good","boy","boy"]
# print(wrd.count("boy"))
# for i in unique_words:
#     if i in

tf = []
for i in cnt_wrd_by_snt:
    length = len(i)
    tf_row = []
    for wrd,cnt in i.items():
        tf_row.append(cnt/length)
    tf.append(tf_row)

print(tf)


# # for i in range(len(corpus)):
# #     for j in corpus[i].split(" "):
# #         tf_row = []
# #         if j in unique_words:
# #             tf_num = cnt_wrd_by_snt[i][j]/len(corpus[i].split(" "))
# #             tf_row.append(tf_num)
# #     tf.append(tf_row)

# # print(cnt_wrd_by_snt[0]['good'])


# for i in unique_words:
#     for j in range(len(corpus)):
#         tf_row = []
#         if i in corpus[j].split(" "):
#             tf_num = cnt_wrd_by_snt[j][i]/len(corpus[j].split(" "))
#             tf_row.append(tf_num)
#     tf.append(tf_row)

# print(tf)


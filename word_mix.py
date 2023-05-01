word = input().split()   # welcome to your first problem
for i in word:
    length = len(i)
new_word = [""] * length
for i in range(length):
    for j in word:
        if i < len(j):
            new_word[i] += j[i] 
print(*new_word)  # wtyfp eooir luro crsb otl me em
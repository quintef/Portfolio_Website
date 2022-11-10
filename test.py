from collections import defaultdict
res = defaultdict(list)
count = [0]*26
count[ord('e')-ord('a')] +=1

res[tuple(count)].append('eat')

print(res)
dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
res = {}

for v in dict:
   if dict[v] >= 3:
       res[v] = dict[v]

print(res)


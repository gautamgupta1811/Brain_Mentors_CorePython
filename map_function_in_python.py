'''# space seperated intergs
# 1 2 3 4 5 6 7 
input().split()
# ["1", "2", "3", "4", "5", "6", "7"]
for i in range(len(list)):
    list[i] = int(list[i])
'''

s = list(map(int, input().split()))
print(s)

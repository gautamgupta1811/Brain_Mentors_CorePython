# for i in range(start, stop, step):

i = 0
while i<10:
    print(i)
    i = i + 1
print(i, "outside value")


while True:
    print(i)
    break

# ques-1:

a = [1,2,34,5,6,7]
b = tuple([i**3 for i in a])

print(b)

# ques-2:

a = [1,2,34,5,5,6,7,88]
count_even = 0
count_odd = 0
for element in a:
    if element%2==0:
        count_even += 1 # count_even = count_even + 1
    else:
        count_odd += 1
print("Total Number of even elements: "+str(count_even))
print("Total Number of odd elements: "+str(count_odd))

    

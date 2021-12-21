# to check if  a number is prime or not we simply divide it by all the number
# and check


for i in range(2, 21):
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        print("{} is a Prime Number".format(i))

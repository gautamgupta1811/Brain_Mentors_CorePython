def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

terms = 50
print("Fibonacci sequence:")
for i in range(terms):
    print(recur_fibo(i))

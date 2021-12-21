num = int(input("Enter a three digit number: "))
temp = num
new_num = 0
while temp > 0:
    digit = temp%10
    new_num += digit**3
    temp = temp // 10

print(f"{num} is a Armstrong Number") if new_num == num else print(f"{num} is a not Armstrong Number")


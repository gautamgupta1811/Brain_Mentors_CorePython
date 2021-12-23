a=input("Enter first no.:")
b=input("Enter second no.:")
choice=input("Enter your choice:")

dic = {"addition": "+", "subraction": "-", "multiplication":"*", "/": "division",
       "modoulo": "%", "square":"**"}
print(dic[choice])
print("exp: ", a+dic[choice]+b)
print(eval(a+dic[choice]+b))

try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter Second Number: "))
    res = num_1 / num_2
    print(res)

except ValueError:
    print("Please enter correct Integer Value")
except ZeroDivisionError:
    print("Division by zero not possible")
except BaseException as err:
    print(err)

else:
    print("Program Executed Successfully")

finally:
    print("Thank you")

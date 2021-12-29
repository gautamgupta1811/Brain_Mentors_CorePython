class roman:
    def convert(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV",
                  "I"]
        roman_num = ""
        i = 0
        while num > 0:
            for j in range(num//val[i]):
                roman_num += symbol[i]
                num -= val[i]
            i += 1
        return roman_num
num = int(input("Enter the number: "))
print(roman().convert(num))
                    

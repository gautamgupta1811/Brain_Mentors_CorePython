class ReverseString:
    def __init__(self, string):
        self.string = string
        self.reverse_string  = ""
        self.index = 0

    def reverse(self):
        for i in range(len(self.string)):
            if self.string[i] == " ":
                self.reverse_string = self.string[self.index:i] + " " + self.reverse_string
                self.index = i
        self.reverse_string = self.string[self.index:] + self.reverse_string
        return self.reverse_string

    
string = input("Enter string: ")
print(ReverseString(string).reverse())
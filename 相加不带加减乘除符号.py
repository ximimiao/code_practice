class resolution:
    def Add(self,num1,num2):
        while num2:
            sum = num2^num1
            carry = (num2&num1) << 1
            num1 = sum
            num2 = carry
        return num1

class resolution:
    def Add(selfsef,num1,num2):
        return sum([num1,num2])

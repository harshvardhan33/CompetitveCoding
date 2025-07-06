class BitArithmetic:
    def __init__(self):
        pass

    def invert(self,b_num):
        invert_b_num = ''.join(['1' if i=='0' else '0' for i in b_num])
        return invert_b_num
        


    def toggle_bit(self,b_num):
        pass

    def possible_nums_with_n_bits(self,b):
        return 2**b,2**(b) - 1


    def power_bit_arithmetic(self,n):
        """
        2 to the power n can be calcualted by the left shift operator easily
        """
        return 1<<n


    def set_bit(self,b_num,k):
        """
        In order to set the kth bit in a number all you need to do is simply perform or 
        operation with the kth bit set number and as a result you will get the kth bit set in the number.
        """
        num = int(b_num,2)
        return bin(num | (1<<k))[2:]


    def unset_bit(self,b_num,k):
        """
        If you have to unset a bit simply take the binary that helps in setting the bit,
        invert that binary and perform the and operation
        """
        num = int(b_num,2)
        
        # Approach 1 
        # kth = self.invert(bin(1<<k))
        # num = num & int(kth,2)
        
        # Approach 2 
        kth = ~(1<<k)
        num = num & kth 
        return format(num, '0{}b'.format(len(b_num)))


    def count_bits(self,b_num):
        if isinstance(b_num, str):
            return b_num.count('1')
        else:
            return bin(b_num).count('1')

    def check_set_bit(self,b_num,k):
        """
        To check any binary number kth bit is set or not. 
        All we need to do is perform & operation with the kth bit number of the binary number.
        If the resultant number is zero -> Bit is unset 
        if the resultant number is non zero -> Bit is set
        """
        num = int(b_num,2)
        if num & (1<<k)==0:
            return False 
        return True


class BitApplication:
    def __init__(self):
        self.obj = BitArithmetic()

    def check_odd_even(self,num):
        if num & 1 == 0:
            return "Even"
        else:
            return "Odd"

    def case_conversion(self,char,method="lower"):
        """ 
        Method 1 
        Uppercase to lower --> Take the binary of the character than OR with binary of the space 
        Lowercase to upper --> Take the binary of the character than AND with binary of the underscore
        
        Method 2 
        Upper to lower --> set the 6th (5th position) bit to 1 
        Lowet to uppet --> unset the 6th (5ht position)bit to 0 
        """
        if method=="lower":
            char_binary = bin(ord(char))[2:]
            lower_char_binary = self.obj.set_bit(char_binary,5)
            return chr(int(lower_char_binary,2))
        else:
            char_binary = bin(ord(char))[2:]
            upper_char_binary = self.obj.unset_bit(char_binary,5)
            return chr(int(upper_char_binary,2))
        

    def check_power_of_2(self,num):
        if num & (num-1) == 0:
            return True
        return False

    def clear_msb(self,b_num,k):
        """ 
        To clear all bits from the MSB down to (but not including) bit k, we AND with a mask that has lower k+1 bits set.
        """ 
        b_num = int(b_num,2)
        mask = (1<<(k+1))-1
        return bin(b_num & mask)[2:]

    def clear_lsb(self,b_num,k):
        """ 
        To clear all bits from 0 up to k (inclusive), we AND with a mask that has all 1’s except these bits as 0.
        """
        b_num = int(b_num,2)
        mask = ~((1<<(k+1))-1)
        return bin(b_num & mask)[2:]



b_obj = BitArithmetic()
b_app = BitApplication()

num = 16
i = 3

# Right Shift
print("Right Shift = Multiply the num by 2*i times : ",num<<2)
# Left Shift
print("Left Shift = Divide the num by 2*i times : ",num>>1)
print("---------------------------------------------------")
# Possible nums and max number
nums, max_num = b_obj.possible_nums_with_n_bits(i)
print(f"Possible Number with {i} bits max : {nums} , {max_num} ")
power = 5
print(f"2 to the power {power} = ", b_obj.power_bit_arithmetic(power))
print("---------------------------------------------------")

b_num = "1110"
k = 0
print(f"Is {k}th bit set in {b_num} ? : ",b_obj.check_set_bit(b_num,k))

b_num = "0110"
k = 3
print(f"{k}th bit set in {b_num} : ",b_obj.set_bit(b_num,k))
print("---------------------------------------------------")

b_num = "101"
print('Invert of binary number : ',b_obj.invert(b_num))

b_num = "0110"
k = 2
print(f"{k}th bit Unset in {b_num} : ",b_obj.unset_bit(b_num,k))

b_num = "0011"
print("Number of set bits are : ",b_obj.count_bits(b_num))
print("---------------------------------------------------")

num1 = 16 
num2 = 7 
num3 = 1
print(f"Number is {num1}: ",b_app.check_odd_even(num1))
print(f"Number is {num2}: ",b_app.check_odd_even(num2))
print(f"Number is {num3}: ",b_app.check_odd_even(num3))
print("---------------------------------------------------")


s1 = "A"
s2 = "a"
print(f"Upper to Lower : {s1} --> ",b_app.case_conversion(s1,method="lower"))
print(f"Lower to Upper : {s2} --> ",b_app.case_conversion(s2,method="upper"))

num1 = 16 
num2 = 15 
print("---------------------------------------------------")
print(f"Check power of 2 : {num1}",b_app.check_power_of_2(num1)) 
print(f"Check power of 2 : {num2}",b_app.check_power_of_2(num2))


b_num = "101011"
k = 3
print(f"LSB Clear till {k} bit : ",b_app.clear_lsb(b_num,k))

b_num = "111111"
k = 3
print(f"MSB Clear till {k} bit : ",b_app.clear_msb(b_num,k))
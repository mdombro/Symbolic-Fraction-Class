class fraction:
    
    def __init__(self, num, denom):
        if denom == 0:           # bounds check
            print("Division by zero!!")
        self.num, self.denom = num, denom     # store the num and denom as object variables

    def fract(self, num, denom):  
        if abs(num/denom) > 1:       # check if fraction is going to be mixed number
            whole = int(num/denom) # find the whole number
            a = denom * whole      # a is the number of times denom goes into the whole part
            new_num = num - a           # num-a is the new numerator - is smaller than denomenator
            new_num, denom = self.reduce(abs(new_num), denom)  # reduce the num and denom to GCD
            return whole, new_num, denom
        else:
            num, denom = self.reduce(num, denom)  # if fraction is not a mixed number just reduce to gcd
            whole = 0
            return whole, num, denom
        
    def reduce(self, num, denom):
        k = 1   # var to act as divisor 
        gcd_so_far = 1  # var to keep track of gcd
        while k <= num:  # do not want divisor larger than the smallest part of fraction
            if num%k == 0 and denom%k == 0:   # cehck if divisor is equally divisible into both sides of fraction
                gcd_so_far = k   # make k the gcd so far
            k+=1
        num = num / gcd_so_far   # then divide each side by gcd to reduce fraction
        denom = denom / gcd_so_far
        return num, denom

    def __str__(self):   # function to print out the result when using print command
        """
        A few changes from previous version 
	Now fract is only called for outputting the fraction, 
        The fraction is NOT stored as a whole, num, and denom
	This makes fraction operations far simpler and cuts down on repetition and redundancy
	"""

        whole, num, denom = self.fract(self.num, self.denom)
        #whole, num, denom = 0, self.num, self.denom
        if whole == 0:     # if there is no whole part do not print it
            return str(int(num)) + '/' + str(int(denom))
        elif num == 0:     # if there is no fractional part do no print it
            return str(int(whole))
        else:              # otherwise print every part of mixed number
            return str(int(whole)) + ' ' + str(int(num)) + '/' + str(int(denom))

    def __add__(self, other):
        if type(other) == int:     # if fraction being added to an integer convert that int to a fraction
				   # allows for easy manipulation of integer and fractions
            other = MyFraction(other, 1)
        num1 = self.num * other.denom   # add the fractions...
        num2 = other.num * self.denom
        common_denom = self.denom * other.denom
        num_tot = num1 + num2

        #New from previous version  
	#Now returns another object of fraction - NOT a formatted string
	#More efficient and useful

        return fraction(num_tot, common_denom)  

    # same logic for all other operators  

    def __sub__(self, other):
        if type(other) == int:
            other = MyFraction(other, 1)
        num1 = self.num * other.denom
        num2 = other.num * self.denom
        common_denom = self.denom * other.denom
        num_tot = num1 - num2
        return fraction(num_tot, common_denom)

    def __truediv__(self, other):
        if type(other) == int:
            other = MyFraction(other, 1)
        num_tot = self.num * other.denom
        denom_tot = self.denom * other.num
        return fraction(num_tot, denom_tot)
        
    def __mul__(self, other):
        if type(other) == int:
            other = MyFraction(other, 1)
        num_tot = self.num * other.num
        denom_tot = self.denom * other.denom
        return fraction(num_tot, denom_tot)

class MyFraction(fraction):
    def __init__(self, num, denom):
        fraction.__init__(self, num, denom)  # call fraction class __init__ function
        
    def __pow__(self,other):  # take the num and denom of the fraction to the power passed
        num_power = self.num ** other
        denom_power = self.denom ** other
        return MyFraction(num_power, denom_power)

    def __add__(self, other):  # return a MyFraction in order to have support for exponents - fraction objects cannot be taken to an exponent
			       # redundant but works - sould impove?
        a = fraction.__add__(self,other)
        return MyFraction(a.num, a.denom)

    def __sub__(self,other):
        a = fraction.__sub__(self,other)
        return MyFraction(a.num, a.denom)

    def __mul__(self, other):
        a = fraction.__mul__(self,other)
        return MyFraction(a.num, a.denom)

    def __truediv__(self,other):
        a = fraction.__truediv__(self,other)
        return MyFraction(a.num, a.denom)
    

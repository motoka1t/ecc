class FieldElement:

    def __init__(self, num, prime):
        if num == prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        # this should be iverse of th == operator
        return not (self == other)
 
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime) 

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in diffeent Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against.
        num = (self.num - other.num) % self.prime
        # we ewruen an element of same class
        return self.__class__(num, self.prime)
    
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Field')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        num = (self.num * other.num) % self.prime
        # we return an element of same class
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot divide two numbers in different Field")
        # use Fermat's little theorem.
        # self.num**(p-1) % p == 1
        # this means
        # 1/n == pow(n, p-2, p)
        num = self.num * pow(other.num, self.prime-2, self.prime) % self.prime
        # we return an element of same class
        return self.__class__(num, self.prime)
    
   
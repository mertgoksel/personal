import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        return Complex(self.real+no.real, self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real-no.real, self.imaginary-no.imaginary)
    def __mul__(self, no):
        if no == 0:
            return 0
        rr, rc, cr, cc = self.real*no.real, self.real*no.imaginary, self.imaginary*no.real, self.imaginary*no.imaginary
        return Complex(rr+cc*-1,rc+cr)
    def __truediv__(self, no):
        if no == 0:
            return None
        no_conjugate = Complex(no.real, no.imaginary*-1)
        a,b = self*no_conjugate, no*no_conjugate
        return Complex(a.real/b.real, a.imaginary/b.real)
    def mod(self):
        return Complex(round(math.sqrt(self.real**2+self.imaginary**2), 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result




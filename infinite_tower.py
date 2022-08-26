
import numpy
depth=18
base_raised=power=constant_base=numpy.sqrt(2)
for i in range(depth):
    print(base_raised)
    base_raised=numpy.power(constant_base,power)
    power=base_raised
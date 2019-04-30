# CC: Brooks Brickley and Hector Hernandez 2019
import math

mass = float(input('What is the mass of the weight? : ')) / 1000
period = float(input('What is the period calculated from the data? : '))

angular_frequency = (2*math.pi) / period

spring_constant = mass * angular_frequency**2

print('The angular frequency is', angular_frequency)
print('The spring constant is', spring_constant)

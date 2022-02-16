# import math
print("Let's begin")


def f(x, y):  # return answer of equation
    return x * y   # put f(x,y) here


x = 1  # initial value of x
y = 1  # initial value of y
final_x = 1.3  # the value of x which we are interested in finding his y value.
delta_x = 0.1  # the step between calculation to calculation.
array_x = [x]  # an array that contains all the obtained values of x up to the desired x .
array_y = [y]  # an array that contains all the obtained values of y up to the desired x .

print("delta x =" + str(delta_x))
# calculation
while x < final_x-0.0001:
    y = y + f(x, y) * delta_x  # formula of the Euler's method
    x += delta_x  # the value of x increases each time by the step (delta_x).
    array_y.append(y)  # adding the value y to array_y array.
    array_x.append(x)  # adding the value x to array_x array.

print(array_x)
print(array_y)

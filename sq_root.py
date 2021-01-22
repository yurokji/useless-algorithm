# x = sqrt(y)
import math
def sqroot(y):
    thres = 0.00001
    x_mid = 0
    x_begin = 0
    x_end = y
    while True:
        x_mid = (x_begin + x_end) / 2
        y_mid = x_mid * x_mid
        diff = y - y_mid
        if abs(diff) < thres:
            break
        elif diff > 0:
            x_begin = x_mid
        elif diff < 0:
            x_end = x_mid
    return x_mid

# compare my square root function with math.sqrt()
print(math.sqrt(2345), sqroot(2345))
print(math.sqrt(45654), sqroot(45654))
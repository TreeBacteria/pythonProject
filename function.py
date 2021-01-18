

def add(a,b):
    result = a+b
    return result

def sub(a,b):
    if a>b:
        return a-b
    else:
        return  abs(a-b)
    return result

def multiply(a, b):
    result = a* b
    return result

def divide(a, b):
    result = a//b
    return result

def jegop(x):
    result = x * x
    return result


result_add = add(10, 5)
result_add1 = add(100, 5)
result_add2 = add(105, 5)
result_sub = sub(7, 3)
result_multply = multiply(3, 10)
result_divide = divide(10, 3)
result_jegop = jegop(98)

print('합 : ' + str(result_add))
print('합 : ' + str(result_add1))
print('합 : ' + str(result_add2))
print('뺄셈 : ' + str(result_sub))
print('곱셈 : ' + str(result_multply))
print('나눗셈 : ' + str(result_divide))
print('제곱 : ' + str(result_jegop))
print('='*50)

def now_add(a, b):
    print('%d, %d의 합은 %d입니다' %(a, b, a+b))

now_add(9, 8)

# def say_hello_10_times():
#     for i in range(10):
#         print('안녕하세요')
#
# say_hello_10_times()
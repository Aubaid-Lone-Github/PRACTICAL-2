import numbers


def check_armstrong(num):
    # from 1 to 9
    if num in range(1,9):
        return True

    digits = len(str(num)) #length of number
    sum = 0
    original = num
    while num>0:
        digit = num % 10 
        sum += digit * digits   # * used for order
        num = num // 10

    if sum == original:
        return True
    else :
       return False        

if check_armstrong(numbers):
    print(f"{numbers} is a armstrong number")
else:
    print(f"{numbers} is not a armstrong number")
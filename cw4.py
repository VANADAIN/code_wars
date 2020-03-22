def iq_test(numbers):
    #your code here
    
    s_numbers = numbers.rsplit(" ")
    print(s_numbers)
    k = 0
    n = 0
    print(s_numbers)
    for number in s_numbers:
        number = int(number)
        if number % 2 == 0:
            k += 1
        else:
            n += 1
    if k > n:
        for number in s_numbers:
            number = int(number)
            if number % 2 == 1:
                res = numbers.index(number)
    else:
        for number in s_numbers:
            number = int(number)
            if number % 2 == 0:
                res = numbers.index(number)
    return res

arr = ("2 4 7 8 10")
iq_test(arr)
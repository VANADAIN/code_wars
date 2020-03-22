import numpy 

# def order_weight(strng):
#     # your code
#     weights = []
#     numbas = strng.split(" ")
#     for numba in numbas:
#         cifras = list(numba)
#         weight = 0
#         for cifra in cifras:
#             num = int(cifra)
#             weight = weight + num
#         weights.append(weight)  
#     total = []
#     for i in range(len(numbas)):
#         inner = []
#         inner.append(numbas[i])
#         inner.append(weights[i])
#         total.append(inner)
#     print(numbas)
#     print(total)


#     last_index = len(total) - 1 
#     for i in range(0, last_index): 
        
#         for j in range(0, last_index-i): 

#             if total[j][1] > total[j + 1][1]: 
#                 total[j], total[j+1] =  total[j+1], total[j]
#             if total[j][1] == total[j + 1][1]:
#                 if total[j][0] > total[j + 1][0]:
#                     total[j], total[j+1] =  total[j+1], total[j]

#     print(total)
#     res = []
#     for k in total:
#         res.append(k[0])
    
#     final = " ".join(res)
    
def order_weight(_str):
    zero = _str.split(' ')
    print(zero)
    s = sum(int(c) for c in zero)
    print(s)
    one = sorted(zero, key=lambda x: sum(int(c) for c in x))
    print(one)
    two = sorted(one)
    return ' '.join(two)

strng = "2000 10003 1234000 44444444 9999 11 11 22 123"
order_weight(strng)
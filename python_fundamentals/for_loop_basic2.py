# def biggie_size(l):
#     for i in range(0, len(l), 1):
#         if l[i] > 0:
#             l[i] = "big"
#     return l        
# print(biggie_size([-1, 3, 5, -5]))

# def count_positives(l):
#     val = 0
#     for i in range (0, len(l), 1):
#         if l[i] > 0:
#             val = val + l[i]
#     l[len(l) - 1] = val
#     return l    
# print(count_positives([-1, 1, 1, 1]))   

# def sum_total(l):
#     sum = 0
#     for i in range (0, len(l), 1):
#         sum = sum + l[i]
#     return sum
# print(sum_total([1,2,3,4])) 

# def average(l):
#     sum = 0
#     for i in range(0, len(l), 1):
#         sum = sum + l[i]
#     avg = sum / len(l)    
#     return avg 
# print(average([1, 2, 3, 4])) 
 
# def length(l):
#     long = 0
#     for i in range (1, len(l) + 1 , 1):
#         long = long + 1
#     return long    
# print(length([1,2,3,4]))
 
def minimum(l):
    small = [0]
    for i in range (0, len(l), 1):
        if l[i] < small:
            small = l[i]
    return small
print(minimum([1,2,3,4]))                   
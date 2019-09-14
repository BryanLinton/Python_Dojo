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
 
# def minimum(l):
#     small = l[0]
#     for i in range (0, len(l), 1):
#         if l[i] < small:
#             small = l[i]
#     return small
# print(minimum([1,-3,3,-1]))  

# def maximum(l):
#     large = l[0]
#     for i in range (0, len(l), 1):
#         if l[i] > large:
#             large = l[i]
#     return large
# print(maximum([1,-3,3,-1]))

# def ultimate_anal(l):
#     maximum = l[0]
#     minimum = l[0]
#     total = 0
#     length = len(l)
#     for i in range(0, len(l), 1):
#         if l[i] < minimum:
#             minimum = l[i]
#         elif l[i] > maximum:
#             maximum = l[i]
#         total = total + l[i] 
#         avg = total / len(l)
#         return    
# print(ultimate_anal([37, 2, 1, -9]))  

def reverse(l):
    temp = l[0]
    for i in range(len(l)):
        temp = l[i]
        l[i - 1] = temp
    return l
print(reverse([37, 2, 1, -9]))
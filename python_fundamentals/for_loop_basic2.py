def biggie_size(l):
    for i in range(0, len(l), 1):
        if l[i] > 0:
            l[i] = "big"
    return l        
print(biggie_size([-1, 3, 5, -5]))

def count_positives(l):
    val = 0
    for i in range (0, len(l), 1):
        if l[i] > 0:
            val = val + l[i]
    l[len(l) - 1] = val
    return l    
print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))   

def sum_total(l):
    sum = 0
    for i in range (0, len(l), 1):
        sum = sum + l[i]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6, 3, -2])) 

def average(l):
    total = 0
    for i in range(0, len(l), 1):
        total = total + l[i]
    float(total) / float(len(l))    
    return 
print(average([1, 2, 3, 4])) 
 
def length(l):
    long = 0
    for i in range (1, len(l) + 1 , 1):
        long = long + 1
    return long    
print(length([1,2,3,4]))
print(length([]))
 
def minimum(l):
    if len(l) == 0:
        return False

    small = l[0]
    for i in range (0, len(l), 1):
        if l[i] < small:
            small = l[i]
    return small
print(minimum([1,-3,3,-1]))
print(minimum([]))

def maximum(l):
    if len(l) == 0:
        return False

    large = l[0]
    for i in range (0, len(l), 1):
        if l[i] > large:
            large = l[i]
    return large
print(maximum([1,-3,3,-1]))
print(maximum([])

def ultimate_analysis(l):

    output = {
        "maximum": None,
        "minimum": None, 
        "total": None,
        "length": None, 
        "avg": 0, 
    }
    if len(l) == 0:
        return output
    else:
        output["total"] = 0
        output["maximum"] = l[0]    
        output["minimum"] = l[0]

    for i in range(0, len(l), 1):
        if l[i] > output["maximum"]:
            output["maximum"] = l[i]
        elif l[i] < output["minimum"]:
            output["minimum"] = l[i]

        output["total"] = output["total"] + l[i] 
    output["length"] = len(l)
    output["avg"] = output["total"] / len(l)

    return output    
print(ultimate_analysis([37, 2, 1, -9])) 
print(ultimate_analysis([])) 

def reverse(l):
    for i in range(0, len(l) // 2, 1):
        temp = l[i]
        l[i] = l[len(l) - i - 1]
        l[len(l) - i - 1] = temp
    return l
print(reverse([37, 2, 1, -9]))



def countdown(x):
    arr = []
    for i in range(x, -1, -1):
        arr.append(i)
    return arr    
li = countdown(5)
print(li)

def prnrtn(l):
    print(l[0])
    return l[1]
print(prnrtn([1,2]))    

def first_plus_len(l):
    sum = len(l) + l[0]
    return sum
print(first_plus_len([1, 2, 3, 4, 5]))  
  
def val_greater_sec(l):
    new_li = []
    for i in range (0, len(l), 1):
        if len(l) < 2:
            return False
        elif l[i] > l[1]:
            new_li.append(l[i])
    print(len(new_li))        
    return new_li        
print(val_greater_sec([5,2,3,2,1,4]))
print(val_greater_sec([5]))

def length_and_value(a, b):
    new_li = [b] * a
    return new_li
print(length_and_value(4,7))



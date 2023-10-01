def linearSearchproduct(product, n, target): 
    for i in range(0, n):  
        if (product[i] == target):  
         return i  
    return -1  
product = [1 ,3, 5, 4, 7, 9]  
target = 4 
n = len(product)  
result = linearSearchproduct(product, n, target)  
if(result == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", result)  
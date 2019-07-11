def even():  
    num1 = int(input("Enter first number"))
    num2 =int(input("Enter second number"))
    
    even_num =[]
    
    for R in range(num1,num2):
        if R % 2 ==0:
            even_num.append(R)
        
    return even_num



def reverse_event():
    
    even_nums=even()
    even_nums.reverse()
    
    return even_nums

reverses = reverse_event()
print(reverses)

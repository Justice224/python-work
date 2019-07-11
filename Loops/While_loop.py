
i= 0 
while(i<10):
    i=i+1
    print(i)

def evens():
    rangeSt = int(input("Enter range Start :" ))
    rangeStop =int(input("Enter range Stop :" ))
    while(rangeSt < rangeStop):
        if(rangeSt % 2 == 0):
            print(rangeSt)
        rangeSt+=1

evens()

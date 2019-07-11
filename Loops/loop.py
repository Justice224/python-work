def fig():
    r = 1
    me = "****"
    while r <5 :
        r = r +1
        print(me)

fig()

def pypart():
    a = [1,2,3,4,5,6,5,4,3,2,1]
    for elements in a:
        if elements == max(a):
            print(elements* "*")
        print(elements* "*")
pypart()
def show_menu() :
    print("*** Simple Calculater ***")
    print("1. String of (+ , - , * , /)")
    print("2. Power")
    print("3. Root")
    print("4. Percentage (%)")
    print("5. Factorial (!)")
    print("6. Abs")
    print("7. exit")
    print("Enter your choice :")
    b = int(input())
    return b 

def power(a , b) :
    return a**b


def root(a , b) :
    if (b==0) :
        return "Wrong Input!!!"
    else :
        return (a**(1/b))

def percentage(a , b) :
    unit = a/100
    result = unit * b
    return result

def factorial(a) :
    b=a
    result = 1
    while(b>0) :
        result *= b
        b = b-1
    return result

def abs(a) :
    if(a>=0) :
        return a
    else :
        return a * (-1)



wanna_go = False
a = show_menu()
print(a)#testing the define
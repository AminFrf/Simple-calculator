import emoji

def show_menu() :
    print("*** Simple Calculater ***")
    print(emoji.emojize("1. String of (+ , - , * , /)"))
    print(emoji.emojize("2. Power :zap:" , language="alias"))
    print(emoji.emojize("3. Root :seedling:"))
    print(emoji.emojize("4. Percentage :percent:" , language="alias"))
    print(emoji.emojize("5. Factorial :bangbang:" , language="alias"))
    print(emoji.emojize("6. Abs :straight_ruler:"))
    print(emoji.emojize("7. exit :door:"))
    print("Enter your choice :")
    b = int(input())
    return b 

def power() :

    a = int(input("enter the first number : "))
    b = int(input("enter the second number : "))
    return a**b


def root() :
    a = int(input("enter the base number : "))
    b = int(input("enter the root degree : "))
    if (b==0) :
        return "Wrong Input!!!"
    else :
        return (a**(1/b))

def percentage() :
    a = int(input("enter the base number : "))
    b = int(input("enter the percentage you want to calculate : "))
    unit = a/100
    result = unit * b
    return result

def factorial() :
    b = int(input("enter a number to calculate its factorial : "))
    result = 1
    while(b>0) :
        result *= b
        b = b-1
    return result

def abs() :
    a = int(input("Enter a number to calculate its absolute value : "))
    if(a>=0) :
        return a
    else :
        return a * (-1)



runnig = True

while(runnig) :
    a = show_menu()
    if a==1 :
        pass
    if a==2 :
        print(power())
    if a==3 :
        print(root())
    if a==4 :
        print(percentage())
    if a==5 :
        print(factorial())
    if a==6 :
        print(abs())
    if a==7 :
        print(emoji.emojize("thank you for using our app :red_heart:"))
        runnig = False
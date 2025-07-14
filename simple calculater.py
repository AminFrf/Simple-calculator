import emoji

def show_menu() :
    print()
    print()
    print(emoji.emojize("*** Simple Calculater :abacus: ***"))
    print(emoji.emojize("1. Addition or Subtraction ( :heavy_plus_sign: ,:heavy_minus_sign: )" , language="alias"))
    print(emoji.emojize("2. Multiplication or Division ( :heavy_multiplication_x:  ,:heavy_division_sign: )" , language="alias"))
    print(emoji.emojize("3. Power :zap:" , language="alias"))
    print(emoji.emojize("4. Root :seedling:"))
    print(emoji.emojize("5. Percentage :1234:", language="alias")) 
    print(emoji.emojize("6. Factorial :bangbang:" , language="alias"))
    print(emoji.emojize("7. Abs :straight_ruler:"))
    print(emoji.emojize("8. exit :door:"))
    print("Enter your choice :")
    b = int(input())
    return b 

def Addition_Subtraction() :
    print()
    s = input("Enter your operation (+,-) : ")
    if s=='+' :
        first_num = int(input("enter first number : "))
        second_num = int(input("enter second number : "))
        return first_num + second_num
    elif s=='-' :
        first_num = int(input("enter first number : "))
        second_num = int(input("enter second number : "))
        return first_num - second_num
    else :
        return "wrong input !!!"
    
def Multiplication_Division() :
    print()
    s = input("Enter your operation (*,/) : ")
    if s=='*' :
        first_num = int(input("enter first number : "))
        second_num = int(input("enter second number : "))
        return first_num * second_num
    elif s=='/' :
        first_num = int(input("enter first number : "))
        second_num = int(input("enter second number : "))
        return first_num / second_num
    else :
        return "wrong input !!!"

def power() :
    print()
    a = int(input("enter the first number : "))
    b = int(input("enter the second number : "))
    print()
    return a**b


def root() :
    print()
    a = int(input("enter the base number : "))
    b = int(input("enter the root degree : "))
    print()
    if (b==0) :        
        return "Wrong Input!!!"
    else :
        return (a**(1/b))

def percentage() :
    print()
    a = int(input("enter the base number : "))
    b = int(input("enter the percentage you want to calculate : "))
    print()
    unit = a/100
    result = unit * b
    return result

def factorial() :
    print()
    b = int(input("enter a number to calculate its factorial : "))
    print()
    result = 1
    while(b>0) :
        result *= b
        b = b-1
    return result

def abs() :
    print()
    a = int(input("Enter a number to calculate its absolute value : "))
    print()
    if(a>=0) :
        return a
    else :
        return a * (-1)



runnig = True

while(runnig) :
    a = show_menu()
    if a==1 :
        print(Addition_Subtraction())
    elif a==2 :
        print(Multiplication_Division())
    elif a==3 :
        print(power())
    elif a==4 :
        print(root())
    elif a==5 :
        print(percentage())
    elif a==6 :
        print(factorial())
    elif a==7 :
        print(abs())
    elif a==8 :
        print()
        print(emoji.emojize("thank you for using our app :red_heart:"))
        runnig = False
    else :
        print()
        print("wrong input!!!")
        print()
       
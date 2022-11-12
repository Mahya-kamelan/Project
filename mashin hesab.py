from multiprocessing.spawn import import_main_path


import math
user = int(input("how many times do you want to use it?: "))
Type_of_use = input("Basic or Advanced?: ")
if Type_of_use == "Basic":

    for i in range(user):
        first_number = float(input("enter your first number"))
        second_number = float(input("enter your second number"))
        operation_list = ["+", "-", "/", "*"]
        operation_list = input (["+",   "-" ,   "*" , "/"])

        if operation_list == "+":
            total = first_number + second_number
            print("Answer = ", total)

        elif operation_list == "-":
            total = first_number - second_number
            print("Answer = ", total)

        elif operation_list == "/":
            total = first_number / second_number
            print("Answer = ", total)
        
        elif operation_list == "*":
            total = first_number * second_number
            print("Answer = ", total)
        
        else:
            print("You are nott using the operation correctly")
            continue
        print("you are using that more than what you said!")

#Advanced
elif Type_of_use == "Advaced":
    for i in range(user):
        first_number = float(input("enter your first number"))
        second_number = float(input("enter your second number"))
        operation_list = ["//", "%", "^2",  "^n", "| |" , "sin", "cos" , "tan" , "cot" , "√ ", "pr"]
        operation_list = input ("//", "%", "^2",  "^n", "| |" , "sin", "cos" , "tan" , "cot" , "√ ", "pr")
        if operation_list == "||":
           total = math.fabs(first_number)
           print('Answer =', total)
        elif operation_list == "√ ":
            total = math.sqrt(first_number)
            print('Answer =', total)
        elif operation_list == "%":
             second_number = float(input('Enter second number:'))
             if second_number == 0:
                print('Error')
                continue
             total = first_number % second_number
             print(first_number,"%",second_number,"=","mod =" , total)
        elif operation_list == '//':
            second_number = float(input('Enter second number:'))
            if second_number == 0:
                print('Error')
                continue
            else:
                total = first_number // second_number
                print(first_number,'//',second_number,"=", total)
        elif  operation_list == '^2':
            total = math.pow(first_number,2)
            print(first_number, "^2 =",total )
        elif  operation_list == '^':
            second_number = float(input('Enter second number:'))
            total = math.pow(first_number,second_number)
            print(first_number, "^", second_number, " = " ,total)
        elif operation_list == 'pr':
            first_number = int(first_number)
            if first_number>1:
                for i in range(2,first_number//2):
                     if(first_number%i)==0:
                        print(first_number,"not pr")
                        break
                else:
                    print(first_number,"pr")
            else:
                print(first_number,"none of them")
        elif operation_list == 'sin':
             total = math.sin(first_number)
             print('Answer=', total)
        elif operation_list == 'cos':
             total = math.cos(first_number)
             print('Answer=', total)
        elif operation_list == 'tan':
             total = math.tan(first_number)
             print('Answer=', total)
        elif operation_list == 'cot':
             total = math.atan(first_number)
             print('Answer=', total)
        else:
            print('\nError!! operation is not correct')
        continue

    print('you used it more than what you said!')
else:
    print('\You are not using the operation correctly')
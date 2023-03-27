# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

#Student ID: w1810559
#Date: 11th December 2020


#initializing variables

prog = 0
trail = 0
ret = 0
exc = 0

#function for predicting the progress outcome

def progout(num1,num2,num3):
    if num1 == 120:
        print("Progression Outcome : Progress")
        global prog
        prog += 1

    elif num1 == 100 and (num2 == 20 or num3 == 20):
        print("Progression Outcome: Progress - Module Traier")
        global trail
        trail += 1

    elif num3 >= 80:
        print("Progression Outcome: Excluded")
        global exc
        exc += 1

    else:
        print("Progression Outcome: Do not progress - Module Retriever")
        global ret
        ret += 1


#program start - getting inputs from the user

while True:
    try:
        passc = int(input("Please enter your credit at Pass: \n"))
        defer = int(input("Please enter your credit at Defer: \n"))
        fail = int(input("Please enter credit at Fail: \n"))
    except:
        print("Invalid input, Integer required")    #integer check
        #loop until correct values are input
        passc = int(input("Please enter your credit at Pass: \n"))
        defer = int(input("Please enter your credit at Defer: \n"))
        fail = int(input("Please enter credit at Fail: \n"))

    if passc % 20 == 0 and defer % 20 == 0 and fail % 20 == 0:   #condition to check if inputs are in range of 20
        if (passc+defer+fail)== 120:      #check if total is 0
            progout(passc,defer,fail)  
        else:
            print("Total Incorrect")    #total not equal to 120
    else:
        print("Out of range")   #input not in range of 20


      

    
                



        

        
        

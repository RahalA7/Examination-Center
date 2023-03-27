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


#program start - getting input from the user

passc = int(input("Please enter your credit at Pass: \n"))
defer = int(input("Please enter your credit at Defer: \n"))
fail = int(input("Please enter credit at Fail: \n"))

if (passc+defer+fail)== 120:      
    progout(passc,defer,fail)
    



        

        
        

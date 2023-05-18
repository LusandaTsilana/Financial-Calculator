import math

userInput = str(input("Choose either 'investment' or 'bond' from the menu below to proceed:\ninvestment - to calculate the amount of interest you'll earn on interest\nbond       - to calculate the amount you'll have to pay on a loan\n"))

if(userInput.lower()=="investment"):
    
        deposit = float(input("Please input the amount of money you wish to deposit:\n"))

        userInput = str(input("Would you like simple or compound interest?\n"))

        if(userInput.lower()=="compound"):

                interestRate = float(input("What is the interest rate?\n"))

                time = float(input("How many years do you wish to invest?\n"))

                total_amount = float(deposit * math.pow((1+((interestRate/100) / 12)),time))

                total_amount =  "%.2f" % total_amount  

                print(f"The total value of your investment will be: R{total_amount}")

        if(userInput.lower()=="simple"):

                interestRate = float(input("What is the interest rate?\n"))

                time = float(input("How many years do you wish to invest?\n"))

                total_amount = float(deposit * (1 + (((interestRate/100) / 12))*time))

                total_amount =  "%.2f" % total_amount  

                print(f"The total value of your investment will be: R{total_amount}")

#else:
#       print("Invalid input")

elif(userInput.lower()=="bond"):
        
        present_value_house = float(input("Please input the present value of the house:\n"))

        repayment_period = int(input("Please input the duration of months over which the bond will be repaid:\n"))

        interestRateB = float(input("What is the interest rate?\n"))

        bond_repayment = ((((interestRateB/100)/12)/12)*present_value_house)/(1 - (1+((interestRateB/100)/12)/12)**(-repayment_period))

        bond_repayment = "%.2f" % bond_repayment

        print(f"The total repayment will be, R{bond_repayment} per month")

else:
        print("Invalid input")



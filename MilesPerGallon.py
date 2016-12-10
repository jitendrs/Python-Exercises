#Cesar Neri
#December 10, 2016

#Excercise 3-1 from Murach's Python Programming Book

#Data validation added, use of "if/elif/else" control statements
#Ability to run program multiple times added, use of while statement

#!/usr/bin/env python3

#Greeting
print("Miles Per Gallon Program");

#initiate respones
response = "y"

#check response
while response.lower() == "y":

    #Get user data
    print()
    miles  = round(float(input("Enter Miles Driven:\t\t")), 2)
    gallons  = round(float(input("Enter Gallons of Gas Used:\t")), 2)
    gallonCost = round(float(input("Enter Cost per Gallon:\t\t")), 3)
    print()

    #data validation
    if miles < 0 :
        print("Miles driven must be greater than zero, Please try again.")
    elif gallons < 0 :
        print("Gallons used must be greater than zero, Please try again.")
    elif gallonCost < 0 :
        print("Cost per gallon must be greater than zero, Please try again.")
    else:
    
        #Calculate Output
        mpg = round(miles / gallons, 2)
        total = round(gallons * gallonCost, 2)
        mileCost = round (gallonCost / round(miles / mpg, 2), 2)

        #Print output
        print ("Miles Per Gallon: \t" + str(mpg) )
        print ("Total Gas Cost: \t" + str(total) )
        print ("Cost Per Mile: \t\t" + str(mileCost) )

    #get new response 
    response = input("\nGet Entries for another trip(y/n)\t")
    

print("\nGoodbye!")

#variables

cost = 0
weeklyCost = 0
monthlyCost = 0

money = 0
salary = 0

budget = "y"
time = 0

costL = []
weeklyCostL = []
monthlyCostL = []

#inputs

money = float(input("What is the total amount of money you have?"))
print("")
salary = float(input("How much money do you make weekly?"))
print("")


#one time payments
c = input("How many one-time payments do you need to make?")
print("")
for i in range(int(c)):
    cost1 = float(input("What is your #" + str(i +1) + " payment?"))
    print("")
    costL.append(float(cost1))

cost = sum(costL)

#weekly payments
wc = input("How many weekly payments do you need to make?")
print("")
for i in range(int(wc)):
    weeklyCost1 = float(input("What is your #" + str(i +1) + " payment?"))
    print("")
    weeklyCostL.append(float(weeklyCost1))

weeklyCost = sum(weeklyCostL)


#monthly payments

mc = input("How many monthly payments do you need to make?")
print("")
for i in range(int(mc)):
    monthlyCost1 = float(input("What is your #" + str(i +1) + " payment?"))
    print("")
    monthlyCostL.append(float(monthlyCost1))

monthlyCost = sum(monthlyCostL)

#calculations

money = money - cost
print("Your total one-time payment costs are: $" +str(cost))
print("")
print("After all of your one-time payments are made, you will have $" + str(money) + ".")



if float(money) >= 0 and (30 * float(weeklyCost)) + (7 * float(monthlyCost)) > 30*float(salary):
    while money > 0:
        time += 1
        if time % 7 == 0:
            money += float(salary)
            money = float(money) - float(weeklyCost)
        if time % 30 == 0:
            money = float(money) - monthlyCost
            
        if time%7 == 0 or time % 30 == 0:
            print("")
            print("Your total money on day " + str(time) + " is $" + str(money) + ".")
        if money < 0:
            break
    budget = "n"
elif (30 * float(weeklyCost)) + (7 * float(monthlyCost)) <= 30*float(salary) and money >= 0:
    print("")
    print("You have enough money to sustain yourself indefinitely.")
    budget = "y"
else:
    print("")
    print("You do not have enough money to make your initial payments.")
    budget = "nn"


#final report

if budget == "n":
    print("")
    print("-----")
    print("")
    print("Your current budget will last " + str(time - 1) + " days.")
elif budget == "y":
    print("")
    print("This is a solid budget!")
else:
    print("")
    print("Your budget lasts 0 days.")
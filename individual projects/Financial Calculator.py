#WH 2nd Financial Calculator

# a function for the user_interaction takes a start_num that is False, text, and a list that is list
def user_interaction(text, list, start_num = False):
    #loop
    while True:
        #clear the screen
        #show text
        print("\033c"+text)
        #if start_num is False
        if start_num == False:
            #set offset to 0
            offset = 0
            #loop throgh list as item
            for x in list:
                #show itme
                print(x)
        #else
        else:
            #set offset to a copy of start_num
            offset = start_num
            #set count to a copy of start_num
            count = start_num
            #loop throgh list as item
            for x in list:
                #show count : item
                print(str(count)+":",x)
                #add one to count
                count += 1
        #set want to user input
        want = input().strip()
        #try 
        try:
            #returning want-offset as the list itme in list
            return list[int(want)-offset]
        #else
        except:
            #if want in list
            if want in list:
                #return want
                return want

# a functiom for user interaction whith intergers, text
def user_intergers(text):
    #loop
    while True:
        #clear the screen
        #show text
        print(text)
        #user input
        want = input().strip()
        #try
        try:
            #user input to an foat
            return float(want)
        #else
        except:
            pass

# a function for savings 
def savings():
    #clear the screen
    #show Would you like weekly of monthly deposets.
    #set weekly/monthly to user_interaction with 1 text Would you like weekly or monthly deposets? with week and month
    weekly_monthly = user_interaction("Would you like weekly or monthly deposets?",["week","month"],1)
    #set deposit to user_intergers with How much are you depositing?
    deposit = user_intergers("How much are you depositing?")
    #set save_to to user_intergers with What are you saving to?
    save_to = user_intergers("What are you saving to?")
    #clear the screen
    #show it will take you {round save_to/deposit} {weekly/monthly} to save to ${save_to}.
    print(f"\033cIt will take you {(save_to/deposit)} {weekly_monthly}s to save to ${save_to}")
    #user input
    input()

#a function for Compound Interest
def compound_interest():
    #a function for compounding that takes starting, interest, years_spent
    def compounding(starting,interest,years_spent):
        try:
            #if interest is an interger
            if interest.is_integer():
                #returns starting(1+(interest*0.01))^years_spent
                return round((starting*(1+(interest*0.01))**years_spent)*100)/100
            #else
            else:
                #returns starting(1+interest)^yesrs_spent
                return starting*(1+(interest))**years_spent
        except:
            return "BIG number"
    #set savings to user_intergers with What is your starting value?
    savings = user_intergers("\033cWhat is your starting value?")
    #set interest to user_intergers with what is the interest rate?
    interest = user_intergers("What is the interest rate?")
    #set years_spent to user_intergers with How many years?
    yaers_spent = user_intergers("How many years?")
    #show At the end of {years_spent} years you will hav ${compounding with savings, interest, years_spent}.
    print(f"\033cAt the end of {yaers_spent} years you will hav ${compounding(savings, interest, yaers_spent)}.")
    #user input
    input()

#a function for Budget_allocator
def budget_allocator():
    #clear the screen
    #set category to user_intergers with How many budget categories do you have?
    catagory = int(user_intergers("\033cHow many budget categories do you have?"))
    #set categorys as a list
    catagorys = []
    #for loop with a range of catagroy as x
    for x in range(catagory):
        #categorys add to the end user input Category {x+1}:
        catagorys.append(input(f"Category {x+1}:"))

    #set income to user_intergers with What is your monthly income?
    income = user_intergers("What is your monthly income?")
    #loop
    while True:
        #set category_numbers to a list
        catagory_numbers = []
        #for loop with categorys as x
        for x in catagorys:
            #category_numbers add to the end user_intergers with What percent is your {x}:
            catagory_numbers.append(user_intergers(f"What percent is your {x}?"))
        #set sum to 0
        sum = 0
        #for loop with category_numbers as x
        for x in catagory_numbers:
            #add x to sum
            sum += x
        #if sum is 100
        if sum == 100:
            #break out of the loop
            break
        print("\033c")

    #clear the screen
    print("\033c")
    #for loop with a range of catagroy as x
    for x in range(catagory):
        #set cat to categorys with x
        cat = catagorys[x]
        #set num to category_numbers with x
        num = catagory_numbers[0]
        #if cat -1 is s
        if cat[-1] == "s":
            #show {cat} are ${income*(num*0.01)}.
            print(f"{cat} are ${round((income*(num*.01))*100)/100}")
        #else
        else:
            #show {cat} is ${income*(num*0.01)}.
            print(f"{cat} is ${round((income*(num*.01))*100)/100}")
    input()

#a functon for discount_tip that take what
def discount_tip(what="e"):
    #a function for the caculation that takes pos, arg
    def caculation(pos,*text):
        #clear the screen
        print("\033c")
        #set money to user_intergers with arg item 0
        money = user_intergers(text[0])
        #set modifier to user_intergers with arg item 1
        modifier = user_intergers(text[1])
        #if modifier is an interger
        if modifier.is_integer():
            #set value to money*(modifier*0.01)
            value = round((money*(modifier*.01))*100)/100
        #else
        else:
            #set value to money*(modifier)
            value = round((money*(modifier))*100)/100
        #clear the screen
        print("\033c")
        #show arg item 2 + value + arg item 3 + (money + (value*pos))
        print(text[2]+str(value)+text[3]+str(money+(value*pos)))
        #user input
        input()

    #if what is tip
    if what == "tip":
        #caculation with 1 , How much is the bill? , What percent of a tip are you giving? ,The tip amount is $ , and your total is $
        caculation(1,"How much is the bill?","What percent of a tip are you giving?","The tip amount is $", " and your total is $")
    #else
    else:
        #caculation with -1 , How much does the item originally cost? , What percent is the discount? , The discount is $ , and your total is $
        caculation(-1,"How much does the item originally cost?","What percent is the discount?","The discount is $"," and your total is $")

#main loop
while True:
    #set want to user_interaction with 1 , Savings Time Calculator, Compound Interest Calculator, Budget Allocator, Sale Price Calculator, Tip Calculator, Exit
    want = user_interaction("What would you like to do?",["Savings Time Calculator", "Compound Interest Calculator","Budget Allocator", "Sale Price Calculator", "Tip Calculator", "Exit"],1)
    #if want is Savings Time Calculator
    if want == "Savings Time Calculator":
        #run savings
        savings()
    #if want is Compound Interest Calculator
    elif want == "Compound Interest Calculator":
        #run compound_interest
        compound_interest()
    #if want is Budget Allocato
    elif want == "Budget Allocato":
        #run budget_allocator
        budget_allocator()
    #if want is Sale Price Calculator
    elif want == "Price Calculator":
        #run discount_tip 
        discount_tip()
    #if want is Tip Calculator
    elif want == "Tip Calculator":
        #run discount_tip with tip
        discount_tip("tip")
    #if want is Exit
    elif want == "Exit":
        #break
        break

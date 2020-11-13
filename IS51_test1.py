"""

This program is design to determine which payment option is better (more money)
1st option is $100 per day for 10 days. 
2nd option is $1 per day and doubled each day for 10 days. 
Two function would be set to calculate the pay rate.
First function1 will calculate the amount for the first option, 
Second function2 will calculate the amount for the second option.

Function1 will output 100 * 10 days
Function2 will loop 10 tries, with each time, doubling the amount and add the amount to the total.

If the amount is equal, we output the user “option1 and option2 pays the same”
If option1 is better, we output the user “option1 is better”
If option2 is better, we output the user “option2 is better”


"""

"""
# option1
Return 100 * 10

# opton2
Amount  = 1
List1 = []
Loop 10 times
	Add amount to list1
	Amount *= 2
Sum = sum of all items in loop
Return sum
# main
	Var1 = option1
	Var2 = option1
If var1 = var2
	“option 1 and option 2 pays the same”
If var1 < var2
	“Option2 is better"
Else
	“option 1 is better”

Main
"""



def option():
    return 100 * 10


def option2():
    amount = 1
    list = []
    for 1 in range(0, 10):
        list1.append(amount)
        amount *= 2
    total = sum(list1)
    return total

def main()
    answer = ""
    var1 = option1()
    var2 = option2()
    if var1 == var2:
        answer = "option1 and option 2 pays the same."
    elif var1 < var2:
        answer = "option 2 is better."
    else:
        answer = "option 1 is better"
    print(answer)


main()
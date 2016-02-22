def cheese_and_crackers(cheese_count, box_of_crackers):
    print "you got %d cheese & %d box of crackers"%(cheese_count,box_of_crackers)
    
print "we can give function number directly"
cheese_and_crackers(5,20)

print "or we can use variable from script"
amt_cheese =10
amt_crackers = 30

cheese_and_crackers(amt_cheese, amt_crackers)

print "we can do math inside too"
cheese_and_crackers(10+2, 30+3)

print "we can combine variable and math"
cheese_and_crackers(amt_cheese + 100, amt_crackers + 1000)

print "input from user"
amt_cheese = int (raw_input("enter cheese amount: "))
amt_crackers = int (raw_input ("enter crackers amount: "))

cheese_and_crackers(amt_cheese, amt_crackers)
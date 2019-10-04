

def cheese_and_crackers(cheese_count, crackers):
    print "You have %d cheses" % cheese_count
    print "You have %d boxes of crackers" % crackers
    print "Man thats enough for a party"
    print "Get a blanket\n"


print "We can just give the function numbers directly"
cheese_and_crackers(20,30)


print "Or we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 20


cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print " We can even do math! We dont need to know the answer"

cheese_and_crackers(10+20,3*4)

print "And we can combine all the above!"

cheese_and_crackers(amount_of_cheese*2, amount_of_crackers+32)

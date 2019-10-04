ten_things = "Apples Oranges Dreams Crows Lightbulb Sugar"

stuff = ten_things.split(' ')

print "Wait you said there are 10 things but there are only %d" % len(stuff)

more_stuff = ["Day","Night","Song","Friend","Coffee", "Frisbee", "Girl"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding %r to my ten things" % next_one
    stuff.append(next_one)
    print "Now we have %d items" % len(stuff)

    print "There we go:", stuff

    print "Lets do someting with the stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print "#".join(stuff[3:5])

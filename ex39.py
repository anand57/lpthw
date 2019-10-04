states = {
    "California":"CA",
    "New Jersey":"NJ",
    "Florida":"FL",
    "Michigan":"MI"
}


cities = {
    "CA": "San Francisco",
    "MI":"Detroit",
    "NY":"New York",
    "FL":"Jacksonville"
}

#add some more cities!

cities['NV'] = "Las Vegas"
cities["OR"] = "Portland"

print "-"*10
print "NY State has: ", cities["NY"]
print "OR State has: ", cities["OR"]


print '-'*10
print "Michigans abbreviation is ", states["Michigan"]
print "Floridas abbreviation is %r" % states["Florida"]

print "-" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state,abbrev)

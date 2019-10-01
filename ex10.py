tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line"
backslash_cat = "im \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t Catnip \n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


# Adding a counter to stop infinite scroll
counter = 0
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" %i
    counter = counter + 1
    if counter > 100:
        break

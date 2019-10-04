from sys import argv


script, filename = argv

print "We're gonna eras %r"  % filename
print "if you dont wanna do that the quit"
print "if you do want that hit RETURN"


raw_input("?")

print "Opening file..."
target = open(filename, 'w')

print "Truncating the File. Goodbye"
target.truncate()

print "Now im going to ask you for three lines"

line1 = raw_input("line1:\n>")
line2 = raw_input("line2:\n>")
line3 = raw_input("line3:\n>")


target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
print "Closing Target"

target.close()

from sys import argv

script, filename = argv

txt = open(filename)

print("Heres your file %r" % filename)

print txt.read()


print "Type Filename again:"
file_again = raw_input(">")


txt_again = open(file_again)

print txt_again.read()

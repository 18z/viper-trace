import getopt

args = '-a -b -cfoo -d bar a1 a2 z5'.split()
print args

optlist, args = getopt.getopt(args, 'abc:d:')

print optlist
print args

# https://docs.python.org/2/library/getopt.html

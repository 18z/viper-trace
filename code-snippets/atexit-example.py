import atexit

def bye() :
    print "the end"
atexit.register(bye)

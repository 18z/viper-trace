import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

"""

*   First, the try clause (the statement(s) between the try and except
    keywords) is executed.

*   If no exception occurs, the except clause is skipped and execution of the try
    statement is finished.

*   If an exception occurs during execution of the try clause, the rest of the
    clause is skipped. Then if its type matches the exception named after the
    except keyword, the except clause is executed, and then execution continues
    after the try statement.

*   If an exception occurs which does not match the exception named in the except
    clause, it is passed on to outer try statements; if no handler is found, it is
    an unhandled exception and execution stops with a message as shown above."""

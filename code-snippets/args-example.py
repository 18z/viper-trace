def print_everything(*args):
    for count, thing in enumerate(args):
        print '{0}. {1}'.format(count, thing)

print_everything('apple', 'banana', 'cabbage')

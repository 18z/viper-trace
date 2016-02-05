def parse(data):
    root = ''
    args = []

    # Split words by white space.
    words = data.split()
    # First word is the root command.
    root = words[0]

    # If there are more words, populate the arguments list.
    if len(words) > 1:
        args = words[1:]

    return (root, args)

data = raw_input("please type cmds: ")

print data

root, args = parse(data)

print root
print args

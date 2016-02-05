import os

cmd1 = "!123"
cmd2 = "!date"

if cmd1.startswith('!'):
    print "gotcha"

if cmd2.startswith('!'):
    os.system(cmd2[1:])

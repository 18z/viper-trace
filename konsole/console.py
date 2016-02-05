import os
import glob
import atexit
import readline

from colors import bold, cyan, white
from session import __session__
from konsole.plugins import __modules__
from commands import Commands

class Console(object):

    def __init__(self):
        # This will keep the main loop active as long as it's set to True.
        self.active = True
        self.cmd = Commands()

    def parse(self, data):
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

    # def keywords(self, data):
    #     # Check if $self is in the user input data.
    #     if '$self' in data:
    #         data = data.replace('$self', __session__.file.path)

        return data

    def stop(self):
        # Stop main loop.
        self.active = False

    def start(self):
        # Setup shell auto-complete.
        def complete(text, state):
            return (glob.glob(text+'*')+[None])[state]

        # Auto-complete on tabs.
        readline.set_completer_delims(' \t\n;')
        readline.parse_and_bind('tab: complete')
        readline.set_completer(complete)

        # Save commands in history file.
        def save_history(path):
            readline.write_history_file(path)

        # If there is an history file, read from it and load the history
        # so that they can be loaded in the shell.
        history_path = os.path.expanduser('~/.consolehistory')
        if os.path.exists(history_path):
            readline.read_history_file(history_path)

        # Register the save history at program's exit.
        atexit.register(save_history, path=history_path)

        # Main loop.
        while self.active:
            prompt = cyan('shell > ')
            data = raw_input(prompt).strip()
            #data = self.keywords(data)

            if not data:
                continue

            if data.startswith('!'):
                os.system(data[1:])
                continue

            root, args = self.parse(data)

            if root in ('exit', 'quit'):
                self.stop()
                continue

            if root in self.cmd.commands:
                self.cmd.commands[root]['obj'](*args)
            elif root in __modules__:
                module = __modules__[root]['obj']()
                module.set_args(args)
                module.run()

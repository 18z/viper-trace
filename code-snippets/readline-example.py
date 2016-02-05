import os
import atexit
import readline

# Auto-complete on tabs.
def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]

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

while True:
    prompt = 'shell > '
    raw_input(prompt).strip()

# https://docs.python.org/2/library/readline.html
# https://docs.python.org/2/library/atexit.html

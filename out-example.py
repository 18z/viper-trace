from konsole.out import *

print_info("info message")

print_warning("warning message")

print_error("error message")

print_success("success message")

rows = [["cmd", "des"]]
#rows.append(["cmd", "des"])

print rows

print table(['Cmd', 'Description'], rows)

import os
import getopt

from out import *
from colors import bold, cyan, white
from session import __session__

class Commands(object):

    def __init__(self):
        # Map commands to their related functions.
        self.commands = dict(
            help=dict(obj=self.cmd_help, description="Show this help message"),
            open=dict(obj=self.cmd_open, description="Open a file"),
            close=dict(obj=self.cmd_close, description="Close the current session"),
            info=dict(obj=self.cmd_info, description="Show information on the opened file"),
            clear=dict(obj=self.cmd_clear, description="Clear the console"),
            geoip=dict(obj=self.cmd_geoip, description="Find country code and name"),
        )

    def cmd_clear(self, *args):

        os.system('clear')

    def cmd_help(self, *args):

        print(bold("Commands:"))

        rows = []
        for command_name, command_item in self.commands.items():
            rows.append([command_name, command_item['description']])

        print(table(['Command', 'Description'], rows))

    def cmd_open(self, *args):

        def usage():
            print("usage: open [-h] [-f] target")

        def help():
            usage()
            print("")
            print("Options:")
            print("\t--help (-h)\tShow this help message")
            print("\t--file (-f)\tThe target is a file")
            print("")

        try:
            opts, argv = getopt.getopt(args, 'hf', ['help', 'file'])
        except getopt.GetoptError as e:
            print(e)
            usage()
            return

        is_file = False

        for opt, value in opts:
            if opt in ('-h', '--help'):
                help()
                return
            elif opt in ('-f', '--file'):
                is_file = True

        if len(argv) == 0:
            usage()
            return
        else:
            target = argv[0]

        if is_file:
            target = os.path.expanduser(target)

            if not os.path.exists(target) or not os.path.isfile(target):
                print_error("File not found")
                return

            __session__.set(target)
        else:
            target = argv[0].strip().lower()
            path = get_sample_path(target)
            if path:
                __session__.set(path)

    def cmd_close(self, *args):

        __session__.clear()

    def cmd_info(self, *args):

        if __session__.is_set():
            print(table(
                ['Key', 'Value'],
                [
                    ('Name', __session__.file.name),
                    ('Path', __session__.file.path),
                    ('Size', __session__.file.size),
                    ('Type', __session__.file.type),
                    ('MD5', __session__.file.md5),
                    ('SHA1', __session__.file.sha1),
                    ('SHA256', __session__.file.sha256),
                    ('SHA512', __session__.file.sha512),
                    ('SSdeep', __session__.file.ssdeep),
                    ('CRC32', __session__.file.crc32)
                ]
            ))

    def cmd_geoip(self, *args):
        opts, argv = getopt.getopt(args, 'i')
        ip = argv[0].strip()
        __session__.set_ip(ip)

        print(table(
            ['IP', 'Country Name', 'Country Code'],
            [(ip, __session__.country_name, __session__.country_code)]

        ))


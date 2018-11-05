import sys
import argparse

from awsgen.command.configure import Configure
from awsgen.command.link import Link

class App(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='aws-gen', description='Command line interface for the aws-gen package')
        self.subparsers = self.parser.add_subparsers(description='valid subcommands', title='subcommands', help='sub-commands', dest='subparser_name')

    def run(self, args):
        self.addCommand('configure', Configure)
        self.addCommand('link', Link)

        if len(args) < 1:
            self.parser.print_usage()
            sys.exit(1)

        options = self.parser.parse_args(args)
        options.func(options)

    def addCommand(self, command, obj):
        parser = self.subparsers.add_parser(command)
        parser.set_defaults(func=obj(parser).action)
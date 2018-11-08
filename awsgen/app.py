import sys
import argparse

from awsgen.command.configure import Configure
from awsgen.command.getlink import GetLink
from awsgen.command.getkey import GetKey
from awsgen.command.createprofile import CreateProfile
from awsgen.command.listprofiles import ListProfiles
from awsgen.command.getactiveprofile import GetActiveProfile
from awsgen.command.setactiveprofile import SetActiveProfile

class App(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='aws-gen', description='Command line interface for the aws-gen package')
        self.subparsers = self.parser.add_subparsers(description='valid subcommands', title='subcommands', help='sub-commands', dest='subparser_name')


    def run(self, args):
        self.addCommand('configure', Configure)
        self.addCommand('get-link', GetLink)
        self.addCommand('get-key', GetKey)
        self.addCommand('create-profile', CreateProfile)
        self.addCommand('list-profiles', ListProfiles)
        self.addCommand('set-active-profile', SetActiveProfile)
        self.addCommand('get-active-profile', GetActiveProfile)

        if len(args) < 1:
            self.parser.print_usage()
            sys.exit(1)

        options = self.parser.parse_args(args)
        options.func(options)

    def addCommand(self, command, obj):
        parser = self.subparsers.add_parser(command)
        parser.set_defaults(func=obj(parser).action)
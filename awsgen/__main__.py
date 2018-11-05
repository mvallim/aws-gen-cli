import sys

from awsgen.cli import CLI

def main():
    return CLI()

if __name__ == '__main__':
    sys.exit(main().run(sys.argv[1:]))
import argparse


def main():
    parser = argparse.ArgumentParser(description="Application 2")
    parser.add_argument("-n", "--name", help="Specify a name") #This application should let the user set a name with the option `-n [NAME]` or `--name=[NAME]`. 
    parser.add_argument("-H", "--custom-help", action="store_true", help="Show help text") #This application should accept the flags `-h` or `--help` to print a help text. 
    ## I changed the names of: -h/--help, for another (-H/--custom-help) because it geneate the error: 'argparse.ArgumentError: argument -h/--help: conflicting option strings: -h, --help'

    args = parser.parse_args()

    if args.custom_help:
        parser.print_help()
    else:
        greeting = f"Good Morning {args.name}!" if args.name else "Good Morning folks!" #If a name is given, the application should output `Good Morning [NAME]!`. If no name is specified, it should just output `Good Morning folks!`
        print(greeting)


if __name__ == "__main__":
    main()

# run: python3 app2.py
# run: python3 app2.py --help
# run: python3 app2.py -n Pawel

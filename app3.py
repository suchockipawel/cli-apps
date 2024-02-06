import argparse

def main():
    parser = argparse.ArgumentParser(description="Application 3") #This application should support positional arguments and be called like this: `./app3.py [FIRST_NAME] [LAST_NAME] [AGE]`
    parser.add_argument("first_name", nargs="?", default="Larry", help="First name") #If the first name is not specified, should be assumed that it is "Larry".
    parser.add_argument("last_name", nargs="?", default="Hanson", help="Last name") #If the last name is not specified, it should be assumed that it is "Hanson".
    parser.add_argument("age", nargs="?", default=100, type=int, help="Age") #If age is not specified, it should be assumed that it is 100. 
    parser.add_argument("--fast", action="store_true", help="Enable fast mode") #This application should also support the option `--fast`. 

    # In the context of the `argparse` module in Python, `nargs` stands for "number of arguments." It is an argument that you can provide when defining a command-line argument using `argparse`. The `nargs` parameter specifies how many arguments should be consumed for the given option.
        ## `nargs='?'`: This means zero or one argument. The option can be specified without an argument, in which case the default value is used. If an argument is provided, it is used as the value for the option.



    args = parser.parse_args()

    if args.fast:
        print("fast mode enabled") #It should print "fast mode enabled" if this is one of the options.

    age_plus_one = args.age + 1
    greeting = f'Hello {args.first_name} {args.last_name}! I see that you have had {age_plus_one} birthdays.' #The app should then output the text "Hello [FIRST_NAME] [LAST_NAME]! I see that you have had [AGE + 1] birthdays.".
    print(greeting)


if __name__ == "__main__":
    main()

# run: python3 app3.py
# run: python3 app3.py --fast
# run: python3 app3.py Pawel Suchocki 45
# run: python3 app3.py Pawel Suchocki 45 --fast
import sys

def main():
    if "--help" in sys.argv: 
        print("Help text for app1.py") #If one of the options is `--help`, it should output a small help text.
    elif "--fast" in sys.argv:
        print("fast mode enabled") #If one of the options is `--fast` is should print the text "fast mode enabled" to the command line.
    else:
        print("slow mode enabled") #If `--fast` is not one of the options it should print the text "slow mode enabled" to the command line.


if __name__ == "__main__":
    main()

# run: python3 app1.py
# run: python3 app1.py --fast
# run: python3 app1.py --help
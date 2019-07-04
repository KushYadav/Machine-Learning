if __name__ == '__main__':
    # What to do when this module is run directly.
    print("M1 Module %s", (__name__))
else:
    #What to do when this module is imported.
    print("I am in M1, else block")

# M1 is main if we run M1.py

#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for s in dir(hidden_4):
        if s[:2] != "__" and s[:1] != " \t":
            print("{}".format(s))
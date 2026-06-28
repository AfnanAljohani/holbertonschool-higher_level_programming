#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = [x for x in dir(hidden_4) if not x.startswith("__")]
    for name in sorted(names):
        print(name)

from contextlib import contextmanager

@contextmanager
def open_file(name):
    print("Opening file")
    f = open(name, "w")
    try:
        yield f
    finally:
        print("Closing file")
        f.close()

with open_file("test.txt") as file:
    file.write("Hello Context Manager")

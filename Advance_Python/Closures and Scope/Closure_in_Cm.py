from contextlib import contextmanager

@contextmanager
def open_file(filename):
    print("📂 Opening file")
    file = open(filename, "w")

    try:
        yield file        
    finally:
        file.close()
        print("❌ File closed safely")

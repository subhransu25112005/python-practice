class filelock:
    def __enter__(self):
        print("File locked")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("File unlocked")
        
with filelock():
    print("Editing sensitive file")       
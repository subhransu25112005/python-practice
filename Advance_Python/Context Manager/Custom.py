class DatabaseConnection:
    def __enter__(self):
        print("Database connected")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Database closed")

with DatabaseConnection():
    print("Running database query")

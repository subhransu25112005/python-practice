def error_log_reader(file_path):
    
    try:
        file = open(file_path, "r")

        for line in file:         
            if "ERROR" in line:
                print(line.strip())

        file.close()

    except FileNotFoundError:
        print("Log file not found!")


error_log_reader("server.log")

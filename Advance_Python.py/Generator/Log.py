def read_logs(lines):
    for line in lines:
        yield line

def error_filter(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

def format_log(lines):
    for line in lines:
        yield f"[ALERT] {line}"


logs = [
    "INFO Server started",
    "ERROR Database failed",
    "INFO Retry",
    "ERROR Timeout"
]

pipeline = format_log(error_filter(read_logs(logs)))

for log in pipeline:
    print(log)

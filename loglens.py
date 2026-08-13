import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to the log file to be analyzed")
args = parser.parse_args()

log_counts = {}

try:
    with open(args.file) as f:
        lines = 0
        for line in f:
            lines += 1
            parts = line.split()
            category = parts[2]
            log_counts[category] = log_counts.get(category, 0) + 1
    print(f"{lines} lines read")
    for k,v in log_counts.items():
        print(f"{k}: {v}")

except FileNotFoundError:
    print(f"Error: The file '{args.file}' was not found.")
except IsADirectoryError:
    print(f"Error: The path '{args.file}' is a directory, not a file.")
except PermissionError:
    print(f"Error: Permission denied when trying to read the file '{args.file}'.")
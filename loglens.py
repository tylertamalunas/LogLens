import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to the log file to be analyzed")
args = parser.parse_args()

try:
    with open(args.file) as f:
        lines = 0
        for line in f:
            lines += 1
    print(f"{lines} lines read")
except FileNotFoundError:
    print(f"Error: The file '{args.file}' was not found.")
except IsADirectoryError:
    print(f"Error: The path '{args.file}' is a directory, not a file.")
except PermissionError:
    print(f"Error: Permission denied when trying to read the file '{args.file}'.")
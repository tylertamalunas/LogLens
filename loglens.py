import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to the log file to be analyzed")
args = parser.parse_args()


print(f"Log file: {args.file}")


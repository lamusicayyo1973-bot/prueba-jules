import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Count lines in a file.")
    parser.add_argument("file", help="Path to the file to process")
    parser.add_argument("-w", "--word", help="Only count lines containing this word")

    args = parser.parse_args()

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    count = 0
    if args.word:
        for line in lines:
            if args.word in line:
                count += 1
    else:
        count = len(lines)

    print(count)

if __name__ == "__main__":
    main()

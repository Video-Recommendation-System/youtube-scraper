import sys

def main():
    input_file = sys.argv[1]
    contents = readfile(input_file)

    print contents

def readfile(filepath):
    with open(filepath) as f:
        content = [x.strip() for x in f.readlines()]
        return content


if __name__ == "__main__":
    main()

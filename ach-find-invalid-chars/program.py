import re

invalid_pattern = re.compile(r"[^a-zA-Z0-9_\-:.@$=/ \n]")

def check_invalid_characters(lines):
    for line_number, line in enumerate(lines, start=1):
        for index, char in enumerate(line):
            if invalid_pattern.match(char):
                print(f"Invalid character '{char}' line {line_number} at position {index}")

def main():
    file_name = None
    lines = []
    try:
        file_name = input("Enter the file path: ")

        with open(file_name, 'r') as file:
            lines = file.readlines()

        check_invalid_characters(lines)
    
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()


import re
import unicodedata

valid_pattern = re.compile(r"[a-zA-Z0-9_\-:.@$=/ \n]")

def replace_homoglyphs(lines):
    for line_number, line in enumerate(lines, start=1):
        for index, char in enumerate(line):
            if not valid_pattern.match(char):
                print(f"Invalid character '{char}' line {line_number} at position {index}")
        cleaned_line = unicodedata.normalize('NFKD', line).encode('ASCII', 'ignore').decode('ASCII')
        lines[line_number - 1] = cleaned_line  # Update line

def main():
    file_name = None
    lines = []
    try:
        file_name = input("Enter the file path: ")

        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        replace_homoglyphs(lines)

        with open('names-result.txt', 'w', encoding='utf-8') as file:
            file.writelines(lines)        
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()


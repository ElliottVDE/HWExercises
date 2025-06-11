
def main():
    file_name = None
    text = ""

    try:
        file_name = input("Enter the file path: ")
        text = check_duplicates(file_name)

        with open(file_name, 'w') as f:
            f.write(text)

    except Exception as e:
        print(f"Exception: {e}")

def check_duplicates(file_path):
    seen = set()
    text = ""
    duplicates = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line in seen:
                duplicates += 1
            else:
                seen.add(line)
                text += line + '\n'
    return text



if __name__ == "__main__":
    main()


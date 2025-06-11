import re

linebreak_pattern = re.compile(r'\n')
breaks = False
          
def remove_linebreaks(text):
    return text.replace('\r\n', '').replace('\r', '').replace('\n', '')

def add_linebreaks(text):
    return '\n'.join([text[i:i+94] for i in range(0, len(text), 94)])

def main():
    file_name = None

    try:
        file_name = input("Enter the file path: ")

        with open(file_name, 'r') as file:
            lines = file.readlines()
        with open(file_name, 'r') as file:
            text = file.read()

        if(len(lines) > 1):
            text = remove_linebreaks(text)
        else:
            text = add_linebreaks(text)
            
        with open(file_name, 'w') as file:
            file.write(text)

    
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()


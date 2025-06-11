
def main():
    file_name = None
    text = ""

    try:
        incoming = input("Enter the input file path: ")
        outgoing = input("Enter the output file path: ")
        write_fixed_length_file(incoming, outgoing)



    except Exception as e:
        print(f"Exception: {e}")

def write_fixed_length_file(input_path, output_path, line_length=9):
    fields = []
    fixed_line = ""
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            fixed_line = ""
            fields = line.strip().split(',')
            for f in fields:
                fixed_line += '|' + f.ljust(line_length)[:line_length]  # Pad or trim
                
            outfile.write(fixed_line +'\n')




if __name__ == "__main__":
    main()



def main():
    file_name = None
    text = ""

    try:
        incoming = input("Enter the input file path: ")
        outgoing = 'OutputBankFile.csv'
        write_fixed_csv(incoming, outgoing)



    except Exception as e:
        print(f"Exception: {e}")

def write_fixed_csv(input_path, output_path, line_length=9):
    fields = []
    heading = True
    fixed_line = ""
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            fixed_line = ""
            fields = line.strip().split(',')
            name = fields[3] + " " + fields[2] 
            del fields[3]
            if heading:
                fields[2] = "Name"
                heading = False
            else:
                fields[2] = name
                cents = int(fields[3])
                dollars = "${:.2f}".format(cents / 100)
                fields[3] = dollars
            fixed_line = ','.join(fields)
            outfile.write(fixed_line +'\n')


if __name__ == "__main__":
    main()


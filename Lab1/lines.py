def main():
    filename = input("Enter filename: ")
    
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    if not lines:
        print(f"File not found.")
        return
    
    num_lines = len(lines)
    print(f"Number of lines in file: {num_lines}")

    while True:
        line_number_input = input(f"Enter line number (1 to {num_lines}), 0 to quit: ")
        
        line_number = int(line_number_input)
        if 1 <= line_number <= num_lines:
            print(f"Line {line_number}: {lines[line_number - 1]}")
        elif line_number == 0:
            break
        else:
            print(f"Not in range")
            
if __name__ == "__main__":
    main()

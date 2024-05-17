def read_file():
    with open("example2.txt", "r") as file1:
        lines = file1.readlines()
        return lines

def main():
    lines = read_file()
    for line in lines:
        print(line, end='')

main()

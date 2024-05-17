#we will search in a file if the word 'Hope' exists
def search_word():
    my_file = open("example2.txt", "r")
    lines = my_file.readlines()
    for row in lines:
        word = "Hope"
        if row.find(word) != -1:
            print("The word: '"+ word + "' exists in the file")
            print('line Number:', lines.index(row))
    my_file.close()

def main():
    search_word()
main() 

#we will search in a file for the longest word and print it
def longest_word():
    f = open("example2.txt", "r")
    longest_word = ''
    for line in f.readlines():
        for word in line.split():
            if len(word)>len(longest_word):
                longest_word = word
    print("The longest word in the file is: ", longest_word)
    f.close
longest_word()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = list(text)
    count_by_char = {}

    for char in chars:
        default_char = char.lower()
        if (default_char in count_by_char):
            count_by_char[default_char]+=1
        else:
            count_by_char[default_char]=1

    return count_by_char

def print_report(file):
        file_contents = file.read()

        print(f"--- Begin report of {file.name} ---")
        # print(file_contents)
        print(f"{count_words(file_contents)} words found in the document \n")
        
        char_data = count_chars(file_contents)

        for char in char_data:
            if(char.isalpha()):
                print(f"The {char} character was found {char_data[char]} times")

        print("--- End report ---")

def main():
    file_path = "./books/frankenstein.txt" 
    with open(file_path) as f:
        print_report(f)

        
main()